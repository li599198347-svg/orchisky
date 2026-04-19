# -*- coding: utf-8 -*-
"""
⚠️ LEGACY · V3.0 老路径资产 · V4.0 不主推使用

当 SVG → PPT 转换需求出现时,请使用:
  /mnt/skills/user/orchisky-ppt/assets/svg_to_pptx_wrapper.py

本文件保留,仅供以下场景参考:
- 零散快速拼几个形状(<10 个元素)
- 无 SVG 源时手工构造 PPT 页
- 了解 V3.0 的扁平化主题思路

具体见 references/engineering-lessons.md 场景 22 的说明。
"""

from apply_orchisky_theme import apply_orchisky_theme, fix_theme_fonts

__all__ = ['apply_orchisky_theme', 'fix_theme_fonts']
