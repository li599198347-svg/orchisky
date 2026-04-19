"""Find SVG and notes files in a project directory."""

from __future__ import annotations
from pathlib import Path
from typing import Optional


def discover_svg_files(directory: Path, pattern: str = '*.svg') -> list[Path]:
    """Return sorted list of SVG files in *directory*."""
    return sorted(directory.glob(pattern))


def discover_notes_files(directory: Path, pattern: str = '*.md') -> dict[str, Path]:
    """
    Return a dict mapping stem -> Path for every Markdown file
    found alongside SVG files.  Used for presenter notes.
    """
    result = {}
    for md in directory.glob(pattern):
        result[md.stem] = md
    return result


def pair_svg_with_notes(
    svg_files: list[Path],
    notes_dir: Optional[Path] = None,
) -> list[tuple[Path, Optional[Path]]]:
    """
    Pair each SVG with an optional Markdown notes file.

    Args:
        svg_files: ordered list of SVG paths
        notes_dir: directory containing .md files; if None, same dir as SVGs

    Returns:
        list of (svg_path, notes_path_or_None)
    """
    pairs = []
    for svg in svg_files:
        search_dir = notes_dir or svg.parent
        notes = search_dir / f"{svg.stem}.md"
        pairs.append((svg, notes if notes.exists() else None))
    return pairs
