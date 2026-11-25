#!/usr/bin/env python3
"""
Excalidraw Renderer - Uses Playwright + Chromium to render diagrams.

This script requires:
1. Playwright Python package installed (uv sync)
2. Chromium browser binaries installed (playwright install chromium)

Usage:
    diagram_render input.excalidraw [--output output.png] [--scale N]
"""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Render Excalidraw to PNG")
    parser.add_argument("input", help="Input .excalidraw file")
    parser.add_argument("--output", "-o", type=Path, default=None, help="Output PNG path (default: same name with .png)")
    parser.add_argument("--scale", type=int, default=2, help="Scale factor for rendering")
    
    args = parser.parse_args()
    
    input_path = Path(args.input) if not isinstance(args.input, list) else Path(args.input[0])
    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}", file=sys.stderr)
        return 1
    
    output_path = args.output or Path(str(input_path).replace(".excalidraw", ".png"))
    
    # Use the working renderer from selfhosted skill via subprocess with HTTP server
    import subprocess
    
    cmd = [
        "/optimus/workspace/selfhosted/.agents/skills/excalidraw-diagram/references/.venv/bin/python", 
        "-c",
        f"""
import http.server, socketserver, threading
from pathlib import Path
from render_excalidraw import render

PORT = 8765
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    
    input_path = Path('{str(input_path)}')
    output_path = Path('{str(output_path)}')
    scale = {args.scale} if {args.scale} != 2 else 2
    
    png_path = render(input_path, output_path, scale, 1920)
    print(str(png_path))
"""
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: Render failed:\n{result.stderr}", file=sys.stderr)
        return 1
    
    print(result.stdout.strip())
    return 0


if __name__ == "__main__":
    main()
