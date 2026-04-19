"""Core SVG -> DrawingML dispatcher, group handling, and main entry point."""

from __future__ import annotations

import re
from pathlib import Path
from xml.etree import ElementTree as ET

from .drawingml_context import ConvertContext, ShapeResult
from .drawingml_utils import (
    SVG_NS,
    _extract_inheritable_styles, resolve_url_id,
)
from .drawingml_styles import build_effect_xml
from .drawingml_elements import (
    convert_rect, convert_circle, convert_ellipse,
    convert_line, convert_path,
    convert_polygon, convert_polyline,
    convert_text, convert_image,
)


def parse_transform(transform_str: str) -> tuple:
    """Parse SVG transform string -> (dx, dy, sx, sy, angle_deg)."""
    if not transform_str:
        return 0.0, 0.0, 1.0, 1.0, 0.0
    dx, dy = 0.0, 0.0
    sx, sy = 1.0, 1.0
    angle_deg = 0.0
    m = re.search(r'translate\(\s*([-\d.]+)[\s,]+([-\d.]+)\s*\)', transform_str)
    if m:
        dx = float(m.group(1))
        dy = float(m.group(2))
    m = re.search(r'scale\(\s*([-\d.]+)(?:[\s,]+([-\d.]+))?\s*\)', transform_str)
    if m:
        sx = float(m.group(1))
        sy = float(m.group(2)) if m.group(2) else sx
    m = re.search(r'rotate\(\s*([-\d.]+)', transform_str)
    if m:
        angle_deg = float(m.group(1))
    return dx, dy, sx, sy, angle_deg


def convert_g(elem: ET.Element, ctx: ConvertContext):
    """Convert SVG <g> to DrawingML group shape."""
    transform = elem.get('transform', '')
    dx, dy, sx, sy, angle_deg = parse_transform(transform)
    filter_id = resolve_url_id(elem.get('filter', ''))
    style_overrides = _extract_inheritable_styles(elem)
    child_ctx = ctx.child(dx, dy, sx, sy, filter_id, style_overrides)

    child_results = []
    for child in elem:
        result = convert_element(child, child_ctx)
        if result:
            child_results.append(result)
    ctx.sync_from_child(child_ctx)

    if not child_results:
        return None
    if len(child_results) == 1:
        return child_results[0]

    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    for child_result in child_results:
        bounds = child_result.bounds_emu
        if bounds is None:
            continue
        min_x = min(min_x, bounds[0])
        min_y = min(min_y, bounds[1])
        max_x = max(max_x, bounds[2])
        max_y = max(max_y, bounds[3])

    if min_x == float('inf'):
        return ShapeResult(xml='\n'.join(result.xml for result in child_results))

    group_x = int(min_x)
    group_y = int(min_y)
    group_w = max(int(max_x - min_x), 1)
    group_h = max(int(max_y - min_y), 1)
    shapes_xml = '\n'.join(result.xml for result in child_results)
    group_id = ctx.next_id()

    group_effect = ''
    if filter_id and filter_id in ctx.defs:
        group_effect = build_effect_xml(ctx.defs[filter_id])

    rot_emu = int(angle_deg * 60000)
    rot_attr = f' rot="{rot_emu}"' if rot_emu else ''

    return ShapeResult(
        xml=f'''<p:grpSp>
<p:nvGrpSpPr>
<p:cNvPr id="{group_id}" name="Group {group_id}"/>
<p:cNvGrpSpPr/>
<p:nvPr/>
</p:nvGrpSpPr>
<p:grpSpPr>
<a:xfrm{rot_attr}>
<a:off x="{group_x}" y="{group_y}"/>
<a:ext cx="{group_w}" cy="{group_h}"/>
<a:chOff x="{group_x}" y="{group_y}"/>
<a:chExt cx="{group_w}" cy="{group_h}"/>
</a:xfrm>
{group_effect}
</p:grpSpPr>
{shapes_xml}
</p:grpSp>''',
        bounds_emu=(group_x, group_y, group_x + group_w, group_y + group_h)
    )


_NON_VISUAL_TAGS = frozenset(('defs', 'title', 'desc', 'metadata', 'style'))

_CONVERTERS = {
    'rect': convert_rect,
    'circle': convert_circle,
    'ellipse': convert_ellipse,
    'line': convert_line,
    'path': convert_path,
    'polygon': convert_polygon,
    'polyline': convert_polyline,
    'text': convert_text,
    'image': convert_image,
    'g': convert_g,
}


def collect_defs(root: ET.Element) -> dict:
    """Collect all <defs> children into {id: element}."""
    defs = {}
    for defs_elem in root.iter(f'{{{SVG_NS}}}defs'):
        for child in defs_elem:
            elem_id = child.get('id')
            if elem_id:
                defs[elem_id] = child
    for defs_elem in root.iter('defs'):
        for child in defs_elem:
            elem_id = child.get('id')
            if elem_id:
                defs[elem_id] = child
    return defs


def convert_element(elem: ET.Element, ctx: ConvertContext):
    """Dispatch an SVG element to the appropriate converter."""
    tag = elem.tag.replace(f'{{{SVG_NS}}}', '')
    converter = _CONVERTERS.get(tag)
    if converter:
        try:
            return converter(elem, ctx)
        except Exception as e:
            print(f'  Warning: Failed to convert <{tag}>: {e}')
            return None
    return None


def _preprocess_svg_text(svg_text: str, svg_name: str = '') -> str:
    """Pre-process raw SVG text before XML parsing. Implements Three-Gate system.

    Gate 3: Auto-fix bare & characters; warn on rgb()/hsl() colors.
    Gate 2: Warn if CJK text exceeds 20 characters per line.
    Gate 1: Warn if empty <text> elements found.
    """
    label = f'[{svg_name}] ' if svg_name else ''

    # Gate 3: Fix bare &
    cleaned = re.sub(
        r'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)',
        '&amp;',
        svg_text,
    )

    # Gate 3: Warn on unsupported color formats
    rgb_matches = re.findall(r'(?:fill|stroke)\s*=\s*"((?:rgb|hsl)\([^"]+\))"', cleaned)
    for color_val in set(rgb_matches):
        print(f'  Warning: {label}Color "{color_val}" uses rgb()/hsl() format. Use hex instead.')

    # Gate 2: Warn on long CJK lines
    text_contents = re.findall(r'<text[^>]*>([^<]*)', cleaned)
    for raw_text in text_contents:
        line = raw_text.strip()
        cjk_count = sum(1 for ch in line if '\u4e00' <= ch <= '\u9fff')
        if cjk_count > 20:
            print(f'  Warning: {label}Text line has {cjk_count} CJK chars. May overflow.')

    # Gate 1: Warn on empty text
    empty_texts = re.findall(r'<text[^>]*>\s*(?:<tspan[^>]*>\s*</tspan>\s*)*\s*</text>', cleaned)
    if empty_texts:
        print(f'  Warning: {label}Found {len(empty_texts)} empty <text> element(s).')

    return cleaned


def convert_svg_to_slide_shapes(svg_path: Path, slide_num: int = 1, verbose: bool = False) -> tuple:
    """Convert an SVG file to DrawingML slide XML.

    Returns:
        (slide_xml, media_files, rel_entries)
    """
    try:
        raw_text = Path(svg_path).read_text(encoding='utf-8')
    except UnicodeDecodeError:
        raw_text = Path(svg_path).read_text(encoding='latin-1')

    cleaned_text = _preprocess_svg_text(raw_text, svg_name=Path(svg_path).name)

    try:
        root = ET.fromstring(cleaned_text)
    except ET.ParseError as e:
        print(f'  Error: Failed to parse SVG {Path(svg_path).name}: {e}')
        empty_slide = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"\n'
            '       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"\n'
            '       xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">\n'
            '<p:cSld><p:spTree>\n'
            '<p:nvGrpSpPr><p:cNvPr id="1" name=""/>'
            '<p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>\n'
            '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>\n'
            '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>\n'
            '</p:spTree></p:cSld>\n'
            '<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>\n'
            '</p:sld>'
        )
        return empty_slide, {}, []

    defs = collect_defs(root)
    ctx = ConvertContext(defs=defs, slide_num=slide_num, svg_dir=Path(svg_path).parent)

    shapes = []
    converted = 0
    skipped = 0
    for child in root:
        tag = child.tag.replace(f'{{{SVG_NS}}}', '')
        if tag == 'defs':
            continue
        result = convert_element(child, ctx)
        if result:
            shapes.append(result.xml)
            converted += 1
        else:
            if tag not in _NON_VISUAL_TAGS:
                skipped += 1

    if verbose:
        print(f'  Converted {converted} elements, skipped {skipped}')

    shapes_xml = '\n'.join(shapes)
    slide_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
       xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
       xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:cSld>
<p:spTree>
<p:nvGrpSpPr>
<p:cNvPr id="1" name=""/>
<p:cNvGrpSpPr/><p:nvPr/>
</p:nvGrpSpPr>
<p:grpSpPr>
<a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>
<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm>
</p:grpSpPr>
{shapes_xml}
</p:spTree>
</p:cSld>
<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''

    return slide_xml, ctx.media_files, ctx.rel_entries
