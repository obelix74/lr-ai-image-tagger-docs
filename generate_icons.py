#!/usr/bin/env python3
"""Generate plugin icons for AI Image Tagger"""

import subprocess
import os

# SVG template for the icon (black and white, AI + image tagging theme)
svg_template = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{size}" height="{size}" fill="white"/>

  <!-- Photo/Image frame -->
  <rect x="{margin}" y="{margin}" width="{frame_width}" height="{frame_height}"
        fill="none" stroke="black" stroke-width="{stroke_width}" rx="{corner_radius}"/>

  <!-- Mountain/landscape inside frame (representing image) -->
  <path d="M {img_start},{img_bottom} L {peak1_x},{peak1_y} L {valley_x},{valley_y} L {peak2_x},{peak2_y} L {img_end},{img_bottom} Z"
        fill="black"/>

  <!-- Sun/circle in top right of image -->
  <circle cx="{sun_x}" cy="{sun_y}" r="{sun_radius}" fill="black"/>

  <!-- AI brain icon in bottom right corner -->
  <g transform="translate({brain_x}, {brain_y})">
    <!-- Brain outline -->
    <path d="M {b_path}" fill="none" stroke="black" stroke-width="{ai_stroke}" stroke-linecap="round" stroke-linejoin="round"/>
    <!-- Neural network nodes inside brain -->
    <circle cx="{node1_x}" cy="{node1_y}" r="{node_r}" fill="black"/>
    <circle cx="{node2_x}" cy="{node2_y}" r="{node_r}" fill="black"/>
    <circle cx="{node3_x}" cy="{node3_y}" r="{node_r}" fill="black"/>
  </g>

  <!-- Tag icon in top left corner -->
  <g transform="translate({tag_x}, {tag_y}) rotate(-45)">
    <path d="M 0,{tag_h} L {tag_w},0 L {tag_w},{tag_t} L {tag_t},{tag_w} L 0,{tag_w} Z"
          fill="none" stroke="black" stroke-width="{tag_stroke}"/>
    <circle cx="{tag_hole_x}" cy="{tag_hole_y}" r="{tag_hole_r}" fill="black"/>
  </g>
</svg>'''

def calculate_dimensions(size):
    """Calculate all dimensions based on icon size"""
    margin = size * 0.15
    frame_width = size * 0.7
    frame_height = size * 0.7
    stroke_width = max(2, size * 0.03)
    corner_radius = size * 0.05

    # Image content (mountains)
    img_start = margin + stroke_width
    img_end = margin + frame_width - stroke_width
    img_bottom = margin + frame_height - stroke_width
    img_top = margin + frame_height * 0.5

    peak1_x = margin + frame_width * 0.25
    peak1_y = margin + frame_height * 0.4
    valley_x = margin + frame_width * 0.45
    valley_y = margin + frame_height * 0.65
    peak2_x = margin + frame_width * 0.75
    peak2_y = margin + frame_height * 0.35

    # Sun
    sun_x = margin + frame_width * 0.75
    sun_y = margin + frame_height * 0.25
    sun_radius = size * 0.06

    # AI brain (bottom right)
    brain_size = size * 0.25
    brain_x = size - brain_size * 1.2
    brain_y = size - brain_size * 1.2

    # Brain path (simplified brain shape)
    b_scale = brain_size / 20
    b_path = f"M {2*b_scale},{10*b_scale} Q {0},{8*b_scale} {2*b_scale},{6*b_scale} Q {1*b_scale},{4*b_scale} {3*b_scale},{3*b_scale} Q {4*b_scale},{1*b_scale} {7*b_scale},{2*b_scale} Q {10*b_scale},{0} {13*b_scale},{2*b_scale} Q {16*b_scale},{1*b_scale} {17*b_scale},{3*b_scale} Q {19*b_scale},{4*b_scale} {18*b_scale},{6*b_scale} Q {20*b_scale},{8*b_scale} {18*b_scale},{10*b_scale} Q {19*b_scale},{13*b_scale} {17*b_scale},{15*b_scale} Q {15*b_scale},{17*b_scale} {12*b_scale},{16*b_scale} Q {10*b_scale},{18*b_scale} {8*b_scale},{16*b_scale} Q {5*b_scale},{17*b_scale} {3*b_scale},{15*b_scale} Q {1*b_scale},{13*b_scale} {2*b_scale},{10*b_scale}"

    ai_stroke = max(1, size * 0.015)
    node_r = max(1, size * 0.01)
    node1_x = 6 * b_scale
    node1_y = 8 * b_scale
    node2_x = 10 * b_scale
    node2_y = 8 * b_scale
    node3_x = 14 * b_scale
    node3_y = 8 * b_scale

    # Tag (top left)
    tag_size = size * 0.2
    tag_x = tag_size * 0.3
    tag_y = tag_size * 0.8
    tag_w = tag_size
    tag_h = tag_size * 0.3
    tag_t = tag_size * 0.15
    tag_stroke = max(1, size * 0.015)
    tag_hole_x = tag_w * 0.75
    tag_hole_y = tag_h * 0.5
    tag_hole_r = max(1, size * 0.015)

    return {
        'size': size,
        'margin': margin,
        'frame_width': frame_width,
        'frame_height': frame_height,
        'stroke_width': stroke_width,
        'corner_radius': corner_radius,
        'img_start': img_start,
        'img_end': img_end,
        'img_bottom': img_bottom,
        'peak1_x': peak1_x,
        'peak1_y': peak1_y,
        'valley_x': valley_x,
        'valley_y': valley_y,
        'peak2_x': peak2_x,
        'peak2_y': peak2_y,
        'sun_x': sun_x,
        'sun_y': sun_y,
        'sun_radius': sun_radius,
        'brain_x': brain_x,
        'brain_y': brain_y,
        'b_path': b_path,
        'ai_stroke': ai_stroke,
        'node_r': node_r,
        'node1_x': node1_x,
        'node1_y': node1_y,
        'node2_x': node2_x,
        'node2_y': node2_y,
        'node3_x': node3_x,
        'node3_y': node3_y,
        'tag_x': tag_x,
        'tag_y': tag_y,
        'tag_w': tag_w,
        'tag_h': tag_h,
        'tag_t': tag_t,
        'tag_stroke': tag_stroke,
        'tag_hole_x': tag_hole_x,
        'tag_hole_y': tag_hole_y,
        'tag_hole_r': tag_hole_r,
    }

def generate_icon(size, output_path):
    """Generate an icon of specified size"""
    dims = calculate_dimensions(size)
    svg_content = svg_template.format(**dims)

    # Write SVG file
    svg_path = output_path.replace('.png', '.svg')
    with open(svg_path, 'w') as f:
        f.write(svg_content)

    print(f"Generated SVG: {svg_path}")

    # Try to convert to PNG using available tools
    converters = [
        ['rsvg-convert', '-w', str(size), '-h', str(size), svg_path, '-o', output_path],
        ['inkscape', '--export-type=png', f'--export-width={size}', f'--export-height={size}', svg_path, '--export-filename=' + output_path],
        ['convert', '-background', 'white', '-flatten', svg_path, output_path],
        ['magick', '-background', 'white', '-flatten', svg_path, output_path],
    ]

    converted = False
    for converter in converters:
        try:
            result = subprocess.run(converter, capture_output=True, text=True)
            if result.returncode == 0 and os.path.exists(output_path):
                print(f"Generated PNG: {output_path}")
                converted = True
                break
        except FileNotFoundError:
            continue

    if not converted:
        print(f"Note: Could not convert to PNG automatically. SVG created at {svg_path}")
        print(f"You can convert manually using: rsvg-convert, inkscape, or ImageMagick")

    return svg_path, output_path if converted else None

if __name__ == '__main__':
    sizes = [48, 96, 192]

    print("Generating plugin icons...")
    for size in sizes:
        output_file = f'icon-{size}x{size}.png'
        generate_icon(size, output_file)

    print("\nDone!")
