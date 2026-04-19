"""CLI entry point for svg_to_pptx."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv=None):
    """
    Convert SVG files to a native PPTX.

    Usage:
        python -m svg_to_pptx input_dir/ output.pptx [options]
    """
    parser = argparse.ArgumentParser(
        prog='svg_to_pptx',
        description='Convert SVG slides to native editable PPTX (Orchisky V4.0)',
    )
    parser.add_argument(
        'input',
        help='Directory containing SVG files, or a glob pattern',
    )
    parser.add_argument(
        'output',
        help='Output .pptx path',
    )
    parser.add_argument(
        '--format', '-f',
        default='ppt169',
        choices=['ppt169', 'ppt43', 'pptwide'],
        help='Slide canvas format (default: ppt169)',
    )
    parser.add_argument(
        '--notes-dir', '-n',
        default=None,
        help='Directory containing .md notes files (stem must match SVG stem)',
    )
    parser.add_argument(
        '--compat', '-c',
        action='store_true',
        default=False,
        help='Enable compatibility mode (embed PNG fallback)',
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        default=False,
        help='Verbose output',
    )
    parser.add_argument(
        '--pattern', '-p',
        default='*.svg',
        help='Glob pattern for SVG files (default: *.svg)',
    )

    args = parser.parse_args(argv)

    input_path = Path(args.input)
    output_path = Path(args.output)

    # Discover SVG files
    if input_path.is_dir():
        from .pptx_discovery import discover_svg_files
        svg_files = discover_svg_files(input_path, args.pattern)
    elif '*' in str(input_path) or '?' in str(input_path):
        import glob
        svg_files = sorted(Path(p) for p in glob.glob(str(input_path)))
    else:
        svg_files = [input_path]

    if not svg_files:
        print(f"[Error] No SVG files found in: {args.input}", file=sys.stderr)
        return 1

    if args.verbose:
        print(f"Found {len(svg_files)} SVG file(s)")

    # Optional notes
    notes = None
    if args.notes_dir:
        notes_path = Path(args.notes_dir)
        from .pptx_discovery import discover_notes_files
        notes_map = discover_notes_files(notes_path)
        notes = {svg.stem: notes_map[svg.stem].read_text(encoding='utf-8')
                 for svg in svg_files
                 if svg.stem in notes_map}

    # Build PPTX
    from .pptx_builder import create_pptx_with_native_svg
    ok = create_pptx_with_native_svg(
        svg_files=svg_files,
        output_path=output_path,
        canvas_format=args.format,
        verbose=args.verbose,
        transition=None,
        use_compat_mode=args.compat,
        enable_notes=bool(notes),
        notes=notes,
        use_native_shapes=True,
    )

    if ok:
        if args.verbose:
            print(f"[OK] Output: {output_path}")
        return 0
    else:
        print(f"[FAIL] Some slides failed to convert. Check warnings above.", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
