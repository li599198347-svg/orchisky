# -*- coding: utf-8 -*-
"""
orchisky-ppt constants.py
需要 python-pptx：pip install python-pptx --break-system-packages
"""
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# 画布
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# 颜色
BRAND_BLUE = RGBColor(0x00, 0x3D, 0x7A)
BLUE_MID   = RGBColor(0x00, 0x56, 0xA8)
BLUE_LIGHT = RGBColor(0x3A, 0x7F, 0xC1)
DARK       = RGBColor(0x1A, 0x1A, 0x1A)
GRAY_333   = RGBColor(0x33, 0x33, 0x33)
GRAY_555   = RGBColor(0x55, 0x55, 0x55)
GRAY_888   = RGBColor(0x88, 0x88, 0x88)
GRAY_E2    = RGBColor(0xE2, 0xE2, 0xE2)
GRAY_F5    = RGBColor(0xF5, 0xF5, 0xF5)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
RED        = RGBColor(0xB0, 0x1C, 0x1C)
GREEN      = RGBColor(0x1A, 0x7A, 0x42)

# 字体
FONT_SANS  = 'Microsoft YaHei'
FONT_SERIF = '宋体-简'

# 间距
MARGIN_X = Inches(0.31)
CONTENT_TOP = Inches(1.09)

# 工具
PX = 9525

def px(n):
    return Emu(int(n * PX))

def px_w(x):
    return Inches(x / 96.0)

def px_h(y):
    return Inches(y / 96.0)
