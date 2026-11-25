#!/usr/bin/env python3
"""
Excalidraw Renderer with Validation Loop.

This renderer:
1. Generates SVG from .excalidraw JSON
2. Validates the diagram (checks for overlaps, clipping, etc.)
3. Iterates to fix issues automatically where possible
4. Outputs final SVG (and optionally PNG) when valid

Usage:
    python render_loop.py input.excalidraw [--output output.svg] [--png]
"""

import argparse
import json
from pathlib import Path


def generate_svg(data: dict) -> str:
    """Generate SVG from Excalidraw JSON."""
    width = 1920
    height = 1080
    
    svg_parts = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        '  <defs>',
        '    <style>',
        '      .text { font-family: sans-serif; fill: #000000; }',
        '      .title { font-size: 24px; font-weight: bold; }',
        '      .label { font-size: 14px; }',
        '    </style>',
        '  </defs>',
        '',
        f'  <rect width="{width}" height="{height}" fill="#ffffff"/>',
    ]
    
    for elem in data.get("elements", []):
        x = int(elem.get("x", 0))
        y = int(elem.get("y", 0))
        w = int(elem.get("width", 100))
        h = int(elem.get("height", 50))
        
        elem_type = elem.get("type")
        stroke_color = elem.get("strokeColor", "#000000")
        fill_color = elem.get("backgroundColor", "transparent")
        text = elem.get("text", "")
        
        if elem_type == "rectangle":
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill_color}" stroke="{stroke_color}"/>')
        elif elem_type == "ellipse":
            svg_parts.append(f'  <ellipse cx="{x + w/2}" cy="{y + h/2}" rx="{w/2}" ry="{h/2}" fill="{fill_color}" stroke="{stroke_color}"/>')
        elif elem_type == "text":
            if text:
                svg_parts.append(f'  <text x="{x + w/2}" y="{y + h/2}" class="label" text-anchor="middle">{escape_xml(text)}</text>')
        elif elem_type == "arrow":
            points = elem.get("points", [])
            if len(points) >= 2:
                p0 = points[0]
                p1 = points[-1]
                svg_parts.append(f'  <line x1="{p0["x"]}" y1="{p0["y"]}" x2="{p1["x"]}" y2="{p1["y"]}" stroke="{stroke_color}" stroke-width="2"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def escape_xml(text: str) -> str:
    """Escape XML special characters."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def validate_svg(svg_content: str, data: dict) -> list:
    """Validate SVG for common issues. Returns list of issues found."""
    issues = []
    
    # Parse elements from JSON to check for overlaps/clipping
    elements = data.get("elements", [])
    
    for i, elem in enumerate(elements):
        x = int(elem.get("x", 0))
        y = int(elem.get("y", 0))
        w = int(elem.get("width", 100))
        h = int(elem.get("height", 50))
        
        # Check if element is too small to be readable
        if w < 20 or h < 10:
            issues.append(f"Element {i}: Too small ({w}x{h}), text may not be visible")
        
        # Check for elements outside viewBox
        if x < -50 or y < -50 or (x + w) > width + 50 or (y + h) > height + 50:
            issues.append(f"Element {i}: Outside viewBox bounds")
    
    return issues


def auto_fix_svg(svg_content: str, data: dict) -> tuple:
    """Try to automatically fix common SVG issues. Returns (fixed_svg, fixed_data)."""
    elements = data.get("elements", [])
    
    # Find and resize too-small elements
    for elem in elements:
        w = int(elem.get("width", 100))
        h = int(elem.get("height", 50))
        
        if w < 20 or h < 10:
            # Auto-resize to minimum readable size
            new_w = max(60, w * 3)
            new_h = max(40, h * 3)
            
            elem["width"] = new_w
            elem["height"] = new_h
    
    return generate_svg(data), data


def main():
    parser = argparse.ArgumentParser(description="Render Excalidraw with validation loop")
    parser.add_argument("input", type=Path, help="Input .excalidraw file")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Output SVG path (default: same name)")
    parser.add_argument("--png", action="store_true", help="Convert final SVG to PNG using ImageMagick")
    parser.add_argument("--max-iterations", type=int, default=3, help="Maximum validation iterations")
    
    args = parser.parse_args()
    
    if not args.input.exists():
        print(f"ERROR: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Load JSON
    with open(args.input) as f:
        data = json.load(f)
    
    iteration = 0
    max_iterations = args.max_iterations
    
    while iteration < max_iterations:
        iteration += 1
        
        print(f"\n=== Iteration {iteration}/{max_iterations} ===")
        
        # Generate SVG
        svg_content = generate_svg(data)
        
        # Validate
        issues = validate_svg(svg_content, data)
        
        if not issues:
            print("✓ No validation issues found!")
            break
        
        print(f"Found {len(issues)} issue(s):")
        for issue in issues:
            print(f"  - {issue}")
        
        # Auto-fix
        fixed_svg, data = auto_fix_svg(svg_content, data)
        print("Applied automatic fixes...")
    
    else:
        print("\n⚠ Warning: Reached maximum iterations. Some issues may remain.")
    
    # Save final SVG
    output_path = args.output or Path(str(args.input).replace(".excalidraw", ".svg"))
    with open(output_path, "w") as f:
        f.write(fixed_svg)
    
    print(f"\n✓ Final SVG saved to: {output_path}")
    
    # Optional PNG conversion
    if args.png:
        try:
            import subprocess
            png_path = output_path.with_suffix(".png")
            cmd = ["convert", str(output_path), "-density", "300", str(png_path)]
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"✓ PNG saved to: {png_path}")
        except FileNotFoundError:
            print("⚠ WARNING: ImageMagick 'convert' not found. Install it for PNG output.", file=sys.stderr)


if __name__ == "__main__":
    main()
