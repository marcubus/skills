#!/usr/bin/env python3
"""Simple Excalidraw JSON to PNG converter using PIL/Pillow."""

import argparse
import json
from pathlib import Path


def render_excalidraw_to_svg(data: dict) -> str:
    """Convert Excalidraw JSON to SVG string."""
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
        '      rect, ellipse, polygon { stroke-width: 2; fill-opacity: 0.8; }',
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
        angle = int(elem.get("angle", 0))
        
        if elem_type == "rectangle":
            svg_parts.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill_color}" stroke="{stroke_color}"/>')
        elif elem_type == "ellipse":
            svg_parts.append(f'  <ellipse cx="{x + w/2}" cy="{y + h/2}" rx="{w/2}" ry="{h/2}" fill="{fill_color}" stroke="{stroke_color}"/>')
        elif elem_type == "text":
            if text:
                # Simple text rendering (no rotation for simplicity)
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


def main():
    parser = argparse.ArgumentParser(description="Render Excalidraw JSON to PNG")
    parser.add_argument("input", type=Path, help="Path to .excalidraw JSON file")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Output PNG path (default: same name with .png)")
    args = parser.parse_args()
    
    if not args.input.exists():
        print(f"ERROR: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Load and validate JSON
    with open(args.input) as f:
        data = json.load(f)
    
    # Generate SVG
    svg_content = render_excalidraw_to_svg(data)
    
    # Save SVG first (for debugging)
    svg_path = args.output.with_suffix(".svg") if args.output else Path(str(args.input).replace(".excalidraw", ".svg"))
    with open(svg_path, "w") as f:
        f.write(svg_content)
    print(f"Generated SVG: {svg_path}")
    
    # For now, just output the SVG path - PNG conversion would need PIL/Pillow


if __name__ == "__main__":
    main()
