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

# -*- coding: utf-8 -*-
"""
Orchisky V1.3 品牌规范常量
所有颜色、字体、尺寸的唯一真相来源
"""
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# ============ 画布 ============
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# ============ 颜色（严格按 Orchisky V1.3） ============
BRAND_BLUE = RGBColor(0x00, 0x3D, 0x7A)
BLUE_MID   = RGBColor(0x00, 0x56, 0xA8)
BLUE_LIGHT = RGBColor(0x3A, 0x7F, 0xC1)
DARK       = RGBColor(0x1A, 0x1A, 0x1A)
GRAY_333   = RGBColor(0x33, 0x33, 0x33)
GRAY_555   = RGBColor(0x55, 0x55, 0x55)
GRAY_888   = RGBColor(0x88, 0x88, 0x88)
GRAY_E2    = RGBColor(0xE2, 0xE2, 0xE2)
GRAY_F5    = RGBColor(0xF5, 0xF5, 0xF5)
GRAY_FA    = RGBColor(0xFA, 0xFA, 0xFA)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
RED        = RGBColor(0xB0, 0x1C, 0x1C)
RED_BG     = RGBColor(0xFD, 0xED, 0xED)
ORANGE     = RGBColor(0x9A, 0x52, 0x00)
ORANGE_BG  = RGBColor(0xFE, 0xF4, 0xE8)
GREEN      = RGBColor(0x1A, 0x7A, 0x42)
GREEN_BG   = RGBColor(0xEA, 0xF5, 0xEF)
INFO_BG    = RGBColor(0xE8, 0xF0, 0xFA)
DECO_BLUE_ON_DARK = RGBColor(0x1A, 0x55, 0x90)

# ============ 字体 ============
FONT_SANS  = 'Microsoft YaHei'
FONT_SERIF = '宋体-简'

# ============ 间距 / 边距 ============
MARGIN_X = Inches(0.31)
CONTENT_TOP = Inches(1.09)
CONTENT_BOTTOM = Inches(5.31)
FOOTER_Y = Inches(5.38)

# ============ 工具常量 ============
PX = 9525

def px(n):
    return Emu(int(n * PX))

def px_w(x):
    return Inches(x / 96.0)

def px_h(y):
    return Inches(y / 96.0)
