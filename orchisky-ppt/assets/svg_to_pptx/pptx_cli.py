"""CLI entry point for svg_to_pptx."""

from __future__ import annotations

import sys
import argparse
from datetime import datetime
from pathlib import Path

from .pptx_dimensions import CANVAS_FORMATS, get_project_info
from .pptx_discovery import find_svg_files, find_notes_files
from .pptx_builder import create_pptx_with_native_svg
from .pptx_slide_xml import TRANSITIONS


def main() -> None:
    transition_choices = (
        ['none'] + (list(TRANSITIONS.keys()) if TRANSITIONS
                    else ['fade', 'push', 'wipe', 'split', 'strips', 'cover', 'random'])
    )

    parser = argparse.ArgumentParser(
        description='PPT Master - SVG to PPTX Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument('project_path', type=str)
    parser.add_argument('-o', '--output', type=str, default=None)
    parser.add_argument('-s', '--source', type=str, default='output')
    parser.add_argument('-f', '--format', type=str, choices=list(CANVAS_FORMATS.keys()), default=None)
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('--no-compat', action='store_true')

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--only', type=str, choices=['native', 'legacy'], default=None)
    mode_group.add_argument('--native', action='store_true', default=False)

    parser.add_argument('-t', '--transition', type=str, choices=transition_choices, default='fade')
    parser.add_argument('--transition-duration', type=float, default=0.4)
    parser.add_argument('--auto-advance', type=float, default=None)
    parser.add_argument('--no-notes', action='store_true')

    args = parser.parse_args()

    project_path = Path(args.project_path)
    if not project_path.exists():
        print(f"Error: Path does not exist: {project_path}")
        sys.exit(1)

    try:
        project_info = get_project_info(str(project_path))
        project_name = project_info.get('name', project_path.name)
        detected_format = project_info.get('format')
    except Exception:
        project_name = project_path.name
        detected_format = None

    canvas_format = args.format
    if canvas_format is None and detected_format and detected_format != 'unknown':
        canvas_format = detected_format

    svg_files, source_dir_name = find_svg_files(project_path, args.source)
    if not svg_files:
        print("Error: No SVG files found")
        sys.exit(1)

    only_mode = args.only
    gen_native = only_mode in (None, 'native')
    gen_legacy = only_mode in (None, 'legacy')
    if args.native and only_mode is None:
        gen_legacy = False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if args.output:
        output_base = Path(args.output)
        native_path = output_base
        stem = output_base.stem
        legacy_path = output_base.parent / f"{stem}_svg{output_base.suffix}"
    else:
        exports_dir = project_path / "exports"
        exports_dir.mkdir(parents=True, exist_ok=True)
        native_path = exports_dir / f"{project_name}_{timestamp}.pptx"
        legacy_path = exports_dir / f"{project_name}_{timestamp}_svg.pptx"

    native_path.parent.mkdir(parents=True, exist_ok=True)
    verbose = not args.quiet
    enable_notes = not args.no_notes
    notes: dict[str, str] = {}
    if enable_notes:
        notes = find_notes_files(project_path, svg_files)

    transition = args.transition if args.transition != 'none' else None

    shared_kwargs = dict(
        svg_files=svg_files, canvas_format=canvas_format, verbose=verbose,
        transition=transition, transition_duration=args.transition_duration,
        auto_advance=args.auto_advance, use_compat_mode=not args.no_compat,
        notes=notes, enable_notes=enable_notes,
    )

    success = True
    if gen_native:
        ok = create_pptx_with_native_svg(output_path=native_path, use_native_shapes=True, **shared_kwargs)
        success = success and ok
    if gen_legacy:
        ok = create_pptx_with_native_svg(output_path=legacy_path, use_native_shapes=False, **shared_kwargs)
        success = success and ok

    sys.exit(0 if success else 1)
