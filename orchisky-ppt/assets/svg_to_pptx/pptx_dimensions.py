"""Slide dimensions, format detection, EMU conversion, and constants."""

from __future__ import annotations
from dataclasses import dataclass

# EMU per inch
EMU_PER_INCH = 914400
# EMU per point
EMU_PER_PT = 12700

# Standard SVG canvas size assumed by the Orchisky skill
SVG_CANVAS_W = 1280
SVG_CANVAS_H = 720


@dataclass(frozen=True)
class SlideFormat:
    """Slide width/height in EMU."""
    width: int
    height: int
    name: str


# Built-in formats
FORMATS: dict[str, SlideFormat] = {
    'ppt169': SlideFormat(9144000, 5143500, '16:9 Standard'),
    'ppt43':  SlideFormat(6858000, 5143500, '4:3 Standard'),
    'pptwide': SlideFormat(12192000, 6858000, '16:9 Widescreen'),
}


def get_format(name: str) -> SlideFormat:
    """Return a SlideFormat by name, falling back to ppt169."""
    return FORMATS.get(name, FORMATS['ppt169'])


def px_to_emu(px: float, scale: float) -> int:
    """Convert SVG pixels to EMU using a scale factor."""
    return int(round(px * scale))


def pt_to_emu(pt: float) -> int:
    """Convert points to EMU."""
    return int(round(pt * EMU_PER_PT))


def emu_to_px(emu: int, scale: float) -> float:
    """Convert EMU back to SVG pixels."""
    return emu / scale if scale else 0.0
