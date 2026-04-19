"""Fill, stroke, and shadow XML builders for DrawingML conversion."""

from __future__ import annotations

import math
import re
from xml.etree import ElementTree as ET

from .drawingml_context import ConvertContext
from .drawingml_utils import (
    SVG_NS, ANGLE_UNIT, DASH_PRESETS,
    px_to_emu, _f, resolve_url_id,
    parse_hex_color,
)


def _get_attr(elem, attr, ctx=None):
    val = elem.get(attr)
    if val is not None:
        return val
    if ctx and hasattr(ctx, 'inherited_styles'):
        return ctx.inherited_styles.get(attr)
    return None


def parse_stop_style(style_str: str) -> tuple:
    color = None
    opacity = 1.0
    if not style_str:
        return color, opacity
    for part in style_str.split(';'):
        part = part.strip()
        if part.startswith('stop-color:'):
            color = parse_hex_color(part.split(':', 1)[1].strip())
        elif part.startswith('stop-opacity:'):
            try:
                opacity = float(part.split(':', 1)[1].strip())
            except ValueError:
                pass
    return color, opacity


def build_solid_fill(color: str, opacity=None) -> str:
    alpha = ''
    if opacity is not None and opacity < 1.0:
        alpha = f'<a:alpha val="{int(opacity * 100000)}"/>'
    return f'<a:solidFill><a:srgbClr val="{color}">{alpha}</a:srgbClr></a:solidFill>'


def build_gradient_fill(grad_elem: ET.Element, opacity=None) -> str:
    tag = grad_elem.tag.replace(f'{{{SVG_NS}}}', '')
    stops_xml = []
    for child in grad_elem:
        child_tag = child.tag.replace(f'{{{SVG_NS}}}', '')
        if child_tag != 'stop':
            continue
        offset_str = child.get('offset', '0').strip().rstrip('%')
        try:
            offset = float(offset_str)
            if offset > 1.0:
                offset = offset / 100.0
        except ValueError:
            offset = 0.0
        pos = int(offset * 100000)

        style = child.get('style', '')
        color, stop_opacity = parse_stop_style(style)
        if not color:
            color = parse_hex_color(child.get('stop-color', '#000000'))
        if color is None:
            color = '000000'

        direct_stop_op = child.get('stop-opacity')
        if direct_stop_op is not None:
            try:
                stop_opacity = float(direct_stop_op)
            except ValueError:
                pass

        effective_opacity = stop_opacity
        if opacity is not None:
            effective_opacity *= opacity
        alpha_xml = ''
        if effective_opacity < 1.0:
            alpha_xml = f'<a:alpha val="{int(effective_opacity * 100000)}"/>'
        stops_xml.append(f'<a:gs pos="{pos}"><a:srgbClr val="{color}">{alpha_xml}</a:srgbClr></a:gs>')

    if not stops_xml:
        return ''
    gs_list = '\n'.join(stops_xml)

    if tag == 'linearGradient':
        def parse_coord(val_str, default=0.0):
            val_str = val_str.strip()
            if val_str.endswith('%'):
                return float(val_str.rstrip('%')) / 100.0
            v = float(val_str)
            return v / 100.0 if v > 1.0 else v

        x1 = parse_coord(grad_elem.get('x1', '0'))
        y1 = parse_coord(grad_elem.get('y1', '0'))
        x2 = parse_coord(grad_elem.get('x2', '1'))
        y2 = parse_coord(grad_elem.get('y2', '1'))
        angle_rad = math.atan2(y2 - y1, x2 - x1)
        angle_deg = math.degrees(angle_rad)
        dml_angle = int((angle_deg % 360) * ANGLE_UNIT)
        return f'<a:gradFill>\n<a:gsLst>{gs_list}</a:gsLst>\n<a:lin ang="{dml_angle}" scaled="1"/>\n</a:gradFill>'

    elif tag == 'radialGradient':
        return f'<a:gradFill>\n<a:gsLst>{gs_list}</a:gsLst>\n<a:path path="circle">\n<a:fillToRect l="50000" t="50000" r="50000" b="50000"/>\n</a:path>\n</a:gradFill>'

    return ''


def build_fill_xml(elem: ET.Element, ctx: ConvertContext, opacity=None) -> str:
    fill = _get_attr(elem, 'fill', ctx)
    if fill is None:
        fill = '#000000'
    if fill == 'none':
        return '<a:noFill/>'
    grad_id = resolve_url_id(fill)
    if grad_id and grad_id in ctx.defs:
        return build_gradient_fill(ctx.defs[grad_id], opacity)
    color = parse_hex_color(fill)
    if color:
        return build_solid_fill(color, opacity)
    return '<a:noFill/>'


def build_stroke_xml(elem: ET.Element, ctx: ConvertContext, opacity=None) -> str:
    stroke = _get_attr(elem, 'stroke', ctx)
    if not stroke or stroke == 'none':
        return '<a:ln><a:noFill/></a:ln>'

    width = _f(_get_attr(elem, 'stroke-width', ctx), 1.0)
    width_emu = px_to_emu(width)

    dash_xml = ''
    dasharray = _get_attr(elem, 'stroke-dasharray', ctx)
    if dasharray and dasharray != 'none':
        preset = DASH_PRESETS.get(dasharray.strip())
        if preset:
            dash_xml = f'<a:prstDash val="{preset}"/>'
        else:
            try:
                parts = re.split(r'[\s,]+', dasharray.strip())
                d_raw = float(parts[0])
                sp_raw = float(parts[1]) if len(parts) > 1 else d_raw
                sw = max(width, 0.001)
                d_pct = int(d_raw / sw * 100000)
                sp_pct = int(sp_raw / sw * 100000)
                dash_xml = f'<a:custDash><a:ds d="{d_pct}" sp="{sp_pct}"/></a:custDash>'
            except (ValueError, IndexError):
                dash_xml = '<a:prstDash val="sysDash"/>'

    cap_map = {'round': 'rnd', 'square': 'sq', 'butt': 'flat'}
    cap_attr = ''
    linecap = _get_attr(elem, 'stroke-linecap', ctx)
    if linecap and linecap in cap_map:
        cap_attr = f' cap="{cap_map[linecap]}"'

    join_xml = ''
    linejoin = _get_attr(elem, 'stroke-linejoin', ctx)
    if linejoin == 'round':
        join_xml = '<a:round/>'
    elif linejoin == 'bevel':
        join_xml = '<a:bevel/>'
    elif linejoin == 'miter':
        join_xml = '<a:miter lim="800000"/>'

    grad_id = resolve_url_id(stroke)
    if grad_id and grad_id in ctx.defs:
        grad_fill = build_gradient_fill(ctx.defs[grad_id], opacity)
        return f'<a:ln w="{width_emu}"{cap_attr}>{grad_fill}{dash_xml}{join_xml}</a:ln>'

    color = parse_hex_color(stroke)
    if not color:
        return '<a:ln><a:noFill/></a:ln>'

    alpha_xml = ''
    if opacity is not None and opacity < 1.0:
        alpha_xml = f'<a:alpha val="{int(opacity * 100000)}"/>'

    return f'<a:ln w="{width_emu}"{cap_attr}>\n<a:solidFill><a:srgbClr val="{color}">{alpha_xml}</a:srgbClr></a:solidFill>{dash_xml}{join_xml}\n</a:ln>'


def _parse_filter_params(filter_elem: ET.Element) -> dict:
    std_dev = 4.0
    dx, dy = 0.0, 0.0
    opacity = 0.3
    color = '000000'
    has_offset = False
    for child in filter_elem.iter():
        tag = child.tag.replace(f'{{{SVG_NS}}}', '')
        if tag == 'feDropShadow':
            std_dev = _f(child.get('stdDeviation'), 4.0)
            dx = _f(child.get('dx'), 0.0)
            dy = _f(child.get('dy'), 0.0)
            if abs(dx) > 0.01 or abs(dy) > 0.01:
                has_offset = True
            opacity = _f(child.get('flood-opacity'), 0.3)
            raw = child.get('flood-color', '').strip().lstrip('#')
            if len(raw) == 6:
                color = raw.upper()
        elif tag == 'feGaussianBlur':
            std_dev = _f(child.get('stdDeviation'), 4.0)
        elif tag == 'feOffset':
            dx = _f(child.get('dx'), 0.0)
            dy = _f(child.get('dy'), 0.0)
            if abs(dx) > 0.01 or abs(dy) > 0.01:
                has_offset = True
        elif tag == 'feFlood':
            opacity = _f(child.get('flood-opacity'), 0.3)
            raw = child.get('flood-color', '').strip().lstrip('#')
            if len(raw) == 6:
                color = raw.upper()
    return {'std_dev': std_dev, 'dx': dx, 'dy': dy, 'opacity': opacity, 'color': color, 'has_offset': has_offset}


def build_shadow_xml(filter_elem: ET.Element) -> str:
    if filter_elem is None:
        return ''
    p = _parse_filter_params(filter_elem)
    dx, dy = p['dx'], p['dy'] if p['has_offset'] else (0, 4.0)
    blur_rad = px_to_emu(p['std_dev'] * 2)
    dist = px_to_emu(math.sqrt(dx * dx + dy * dy))
    dir_angle = int(((90 + math.degrees(math.atan2(dy, max(dx, 0.001)))) % 360) * ANGLE_UNIT)
    alpha_val = int(p['opacity'] * 100000)
    return f'<a:effectLst>\n<a:outerShdw blurRad="{blur_rad}" dist="{dist}" dir="{dir_angle}" algn="tl" rotWithShape="0">\n<a:srgbClr val="{p["color"]}"><a:alpha val="{alpha_val}"/></a:srgbClr>\n</a:outerShdw>\n</a:effectLst>'


def build_glow_xml(filter_elem: ET.Element) -> str:
    if filter_elem is None:
        return ''
    p = _parse_filter_params(filter_elem)
    rad = px_to_emu(p['std_dev'] * 2)
    alpha_val = int(p['opacity'] * 100000)
    return f'<a:effectLst>\n<a:glow rad="{rad}">\n<a:srgbClr val="{p["color"]}"><a:alpha val="{alpha_val}"/></a:srgbClr>\n</a:glow>\n</a:effectLst>'


def build_effect_xml(filter_elem: ET.Element) -> str:
    if filter_elem is None:
        return ''
    p = _parse_filter_params(filter_elem)
    if p['has_offset']:
        return build_shadow_xml(filter_elem)
    return build_glow_xml(filter_elem)


def get_element_opacity(elem: ET.Element):
    op = elem.get('opacity')
    if op is None:
        return None
    try:
        val = float(op)
        return val if val < 1.0 else None
    except ValueError:
        return None


def get_fill_opacity(elem: ET.Element, ctx=None):
    base = 1.0
    op = _get_attr(elem, 'opacity', ctx) if ctx else elem.get('opacity')
    if op:
        try:
            base = float(op)
        except ValueError:
            pass
    fill_op = _get_attr(elem, 'fill-opacity', ctx) if ctx else elem.get('fill-opacity')
    if fill_op:
        try:
            base *= float(fill_op)
        except ValueError:
            pass
    return base if base < 1.0 else None


def get_stroke_opacity(elem: ET.Element, ctx=None):
    base = 1.0
    op = _get_attr(elem, 'opacity', ctx) if ctx else elem.get('opacity')
    if op:
        try:
            base = float(op)
        except ValueError:
            pass
    stroke_op = _get_attr(elem, 'stroke-opacity', ctx) if ctx else elem.get('stroke-opacity')
    if stroke_op:
        try:
            base *= float(stroke_op)
        except ValueError:
            pass
    return base if base < 1.0 else None
