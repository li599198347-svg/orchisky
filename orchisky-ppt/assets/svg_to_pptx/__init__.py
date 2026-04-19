"""svg_to_pptx — SVG to PPTX conversion package.

Public API:
    svg_to_pptx(svg_files, output_path, canvas_format='ppt169') -> bool
"""

from .pptx_builder import svg_to_pptx

__all__ = ['svg_to_pptx']
