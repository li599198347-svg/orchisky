"""Coordinate helpers, color parsing, and font utilities for DrawingML conversion."""

from __future__ import annotations

import re
from xml.etree import ElementTree as ET

from .drawingml_context import ConvertContext

SVG_NS = 'http://www.w3.org/2000/svg'
XLINK_NS = 'http://www.w3.org/1999/xlink'
EMU_PER_PX = 9525
FONT_PX_TO_HUNDREDTHS_PT = 75
ANGLE_UNIT = 60000

INHERITABLE_ATTRS = [
    'fill', 'stroke', 'stroke-width', 'stroke-dasharray', 'stroke-linecap',
    'stroke-linejoin', 'opacity', 'fill-opacity', 'stroke-opacity',
    'font-family', 'font-size', 'font-weight', 'font-style',
    'text-anchor', 'letter-spacing', 'text-decoration',
]

EA_FONTS = {
    'PingFang SC', 'PingFang TC', 'PingFang HK', 'Microsoft YaHei', 'Microsoft JhengHei',
    'SimSun', 'SimHei', 'FangSong', 'KaiTi', 'STKaiti', 'STHeiti', 'STSong',
    'STFangsong', 'STXihei', 'STZhongsong', 'Hiragino Sans', 'Hiragino Sans GB',
    'Hiragino Mincho ProN', 'Noto Sans SC', 'Noto Sans TC', 'Noto Serif SC', 'Noto Serif TC',
    'Source Han Sans SC', 'Source Han Sans TC', 'Source Han Serif SC', 'Source Han Serif TC',
    'WenQuanYi Micro Hei', 'WenQuanYi Zen Hei', 'YouYuan', 'LiSu', 'HuaWenKaiTi',
    'Songti SC', 'Songti TC',
}
SYSTEM_FONTS = {'system-ui', '-apple-system', 'BlinkMacSystemFont'}

FONT_FALLBACK_WIN = {
    'PingFang SC': 'Microsoft YaHei', 'PingFang TC': 'Microsoft JhengHei',
    'PingFang HK': 'Microsoft JhengHei', 'Hiragino Sans': 'Microsoft YaHei',
    'Hiragino Sans GB': 'Microsoft YaHei', 'Hiragino Mincho ProN': 'SimSun',
    'STHeiti': 'SimHei', 'STSong': 'SimSun', 'STKaiti': 'KaiTi',
    'STFangsong': 'FangSong', 'STXihei': 'Microsoft YaHei', 'STZhongsong': 'SimSun',
    'Songti SC': 'SimSun', 'Songti TC': 'SimSun',
    'Noto Sans SC': 'Microsoft YaHei', 'Noto Sans TC': 'Microsoft JhengHei',
    'Noto Serif SC': 'SimSun', 'Noto Serif TC': 'SimSun',
    'Source Han Sans SC': 'Microsoft YaHei', 'Source Han Sans TC': 'Microsoft JhengHei',
    'Source Han Serif SC': 'SimSun', 'Source Han Serif TC': 'SimSun',
    'WenQuanYi Micro Hei': 'Microsoft YaHei', 'WenQuanYi Zen Hei': 'Microsoft YaHei',
    'SF Pro': 'Segoe UI', 'SF Pro Display': 'Segoe UI', 'SF Pro Text': 'Segoe UI',
    'SF Mono': 'Consolas', 'Menlo': 'Consolas', 'Monaco': 'Consolas',
    'Helvetica Neue': 'Arial', 'Helvetica': 'Arial', 'Roboto': 'Segoe UI',
    'Ubuntu': 'Segoe UI', 'Liberation Sans': 'Arial',
    'Liberation Serif': 'Times New Roman', 'Liberation Mono': 'Consolas',
    'DejaVu Sans': 'Segoe UI', 'DejaVu Serif': 'Times New Roman',
    'DejaVu Sans Mono': 'Consolas',
}

GENERIC_FONT_MAP = {'monospace': 'Consolas', 'sans-serif': 'Segoe UI', 'serif': 'Times New Roman'}

_SERIF_LATIN = {
    'Times New Roman', 'Georgia', 'Garamond', 'Palatino', 'Palatino Linotype',
    'Book Antiqua', 'Cambria', 'SimSun', 'Liberation Serif', 'DejaVu Serif',
}

DASH_PRESETS = {
    '4,4': 'dash', '4 4': 'dash', '6,3': 'dash', '6 3': 'dash',
    '2,2': 'sysDot', '2 2': 'sysDot', '8,4': 'lgDash', '8 4': 'lgDash',
    '8,4,2,4': 'lgDashDot', '8 4 2 4': 'lgDashDot',
}


def px_to_emu(px: float) -> int:
    return round(px * EMU_PER_PX)

def _f(val: str | None, default: float = 0.0) -> float:
    if val is None: return default
    try: return float(val)
    except (ValueError, TypeError): return default

def _extract_inheritable_styles(elem: ET.Element) -> dict[str, str]:
    return {attr: elem.get(attr) for attr in INHERITABLE_ATTRS if elem.get(attr) is not None}

def _get_attr(elem: ET.Element, attr: str, ctx: ConvertContext) -> str | None:
    val = elem.get(attr)
    if val is not None: return val
    return ctx.inherited_styles.get(attr)

def ctx_x(val: float, ctx: ConvertContext) -> float: return val * ctx.scale_x + ctx.translate_x
def ctx_y(val: float, ctx: ConvertContext) -> float: return val * ctx.scale_y + ctx.translate_y
def ctx_w(val: float, ctx: ConvertContext) -> float: return val * ctx.scale_x
def ctx_h(val: float, ctx: ConvertContext) -> float: return val * ctx.scale_y

def parse_hex_color(color_str: str) -> str | None:
    if not color_str: return None
    color_str = color_str.strip()
    if color_str.startswith('#'): color_str = color_str[1:]
    if len(color_str) == 3: color_str = ''.join(c * 2 for c in color_str)
    if len(color_str) == 6 and all(c in '0123456789abcdefABCDEF' for c in color_str):
        return color_str.upper()
    return None

def parse_stop_style(style_str: str) -> tuple[str | None, float]:
    color, opacity = None, 1.0
    if not style_str: return color, opacity
    for part in style_str.split(';'):
        part = part.strip()
        if part.startswith('stop-color:'):
            color = parse_hex_color(part.split(':', 1)[1].strip())
        elif part.startswith('stop-opacity:'):
            try: opacity = float(part.split(':', 1)[1].strip())
            except ValueError: pass
    return color, opacity

def resolve_url_id(url_str: str) -> str | None:
    if not url_str: return None
    m = re.match(r'url\(#([^)]+)\)', url_str.strip())
    return m.group(1) if m else None

def get_effective_filter_id(elem: ET.Element, ctx: ConvertContext) -> str | None:
    filt = elem.get('filter')
    if filt: return resolve_url_id(filt)
    return ctx.filter_id

def parse_font_family(font_family_str: str) -> dict[str, str]:
    if not font_family_str: return {'latin': 'Segoe UI', 'ea': 'Microsoft YaHei'}
    fonts = [f.strip().strip("'\")") for f in font_family_str.split(',')]
    latin_font, ea_font = None, None
    for font in fonts:
        if font in SYSTEM_FONTS: continue
        if font in GENERIC_FONT_MAP:
            resolved = GENERIC_FONT_MAP[font]
            latin_font = latin_font or resolved
            continue
        win_font = FONT_FALLBACK_WIN.get(font, font)
        if font in EA_FONTS: ea_font = ea_font or win_font
        else: latin_font = latin_font or win_font
    if not latin_font and ea_font: latin_font = ea_font
    final_latin = latin_font or 'Segoe UI'
    if not ea_font:
        ea_font = 'SimSun' if final_latin in _SERIF_LATIN else 'Microsoft YaHei'
    return {'latin': final_latin, 'ea': ea_font}

def is_cjk_char(ch: str) -> bool:
    cp = ord(ch)
    return (0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF or
            0x2E80 <= cp <= 0x2EFF or 0x3000 <= cp <= 0x303F or
            0xFF00 <= cp <= 0xFFEF or 0xF900 <= cp <= 0xFAFF or
            0x20000 <= cp <= 0x2A6DF)

def estimate_text_width(text: str, font_size: float, font_weight: str = '400') -> float:
    width = 0.0
    for ch in text:
        if is_cjk_char(ch): width += font_size
        elif ch == ' ': width += font_size * 0.3
        elif ch in 'mMwWOQ': width += font_size * 0.75
        elif ch in 'iIlj1!|': width += font_size * 0.3
        else: width += font_size * 0.55
    if font_weight in ('bold', '600', '700', '800', '900'): width *= 1.05
    return width

def _xml_escape(text: str) -> str:
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))
