"""ConvertContext — shared state passed through the SVG → DrawingML pipeline."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from lxml import etree


@dataclass
class ConvertContext:
    """Mutable conversion state shared across all converter functions."""

    # Slide geometry (EMU)
    slide_width_emu: int = 9144000   # 16:9 default
    slide_height_emu: int = 5143500

    # SVG viewport
    svg_width: float = 1280.0
    svg_height: float = 720.0

    # Scale factors (EMU per SVG user unit)
    scale_x: float = field(init=False)
    scale_y: float = field(init=False)

    # Accumulated warnings
    warnings: list = field(default_factory=list)

    # Current transform stack
    transform_stack: list = field(default_factory=list)

    # Defs registry (id -> element)
    defs: dict = field(default_factory=dict)

    # Media assets (embedded images base64)
    media: dict = field(default_factory=dict)

    # verbose logging
    verbose: bool = False

    def __post_init__(self):
        self.scale_x = self.slide_width_emu / self.svg_width
        self.scale_y = self.slide_height_emu / self.svg_height

    def recalc_scale(self):
        self.scale_x = self.slide_width_emu / self.svg_width
        self.scale_y = self.slide_height_emu / self.svg_height

    def warn(self, msg: str):
        self.warnings.append(msg)
        if self.verbose:
            print(f"  [WARN] {msg}")

    def log(self, msg: str):
        if self.verbose:
            print(f"  {msg}")
