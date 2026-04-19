"""svg_to_pptx — SVG to PPTX conversion package.

Public API:
    - main(): CLI entry point
    - create_pptx_with_native_svg(): primary conversion function
"""
from .pptx_builder import create_pptx_with_native_svg
from .pptx_cli import main

__all__ = ['create_pptx_with_native_svg', 'main']
