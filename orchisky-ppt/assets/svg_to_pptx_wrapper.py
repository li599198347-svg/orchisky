# -*- coding: utf-8 -*-
"""
svg_to_pptx_wrapper.py — V4.0 对外统一入口

将 SVG 文件列表转换为原生可编辑的 PPTX。
底层调用 svg_to_pptx/ 目录下的工具链。

使用示例:
    from svg_to_pptx_wrapper import svg_to_native_pptx
    from pathlib import Path

    svg_files = sorted(Path('svg_final').glob('*.svg'))
    svg_to_native_pptx(svg_files, Path('output.pptx'))
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional


def svg_to_native_pptx(
    svg_files: list,
    output_path: Path,
    canvas_format: str = 'ppt169',
    verbose: bool = True,
    notes: Optional[dict] = None,
) -> bool:
    """
    将 SVG 文件列表转换为原生可编辑的 PPTX。

    Args:
        svg_files: SVG 文件路径列表（按顺序对应 PPT 的各页）
        output_path: 输出 PPTX 路径
        canvas_format: 画布格式（默认 ppt169 即 16:9）
        verbose: 是否输出转换日志
        notes: 可选的讲稿字典

    Returns:
        bool: 全部转换成功返回 True,有失败返回 False
    """
    wrapper_dir = Path(__file__).parent
    if str(wrapper_dir) not in sys.path:
        sys.path.insert(0, str(wrapper_dir))

    from svg_to_pptx.pptx_builder import create_pptx_with_native_svg

    svg_files = [Path(p) if not isinstance(p, Path) else p for p in svg_files]
    output_path = Path(output_path) if not isinstance(output_path, Path) else output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    return create_pptx_with_native_svg(
        svg_files=svg_files,
        output_path=output_path,
        canvas_format=canvas_format,
        verbose=verbose,
        transition=None,
        use_compat_mode=False,
        enable_notes=bool(notes),
        notes=notes,
        use_native_shapes=True,
    )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='SVG 批量转原生可编辑 PPTX')
    parser.add_argument('svg_dir', type=str, help='SVG 文件目录')
    parser.add_argument('output', type=str, help='输出 .pptx 路径')
    parser.add_argument('--format', default='ppt169', help='画布格式')
    args = parser.parse_args()
    svg_files = sorted(Path(args.svg_dir).glob('*.svg'))
    ok = svg_to_native_pptx(svg_files, Path(args.output))
    sys.exit(0 if ok else 1)
