"""Slide XML and slide relationship XML generation."""

from __future__ import annotations
from lxml import etree

NSMAP = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'xdr': 'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing',
}


def build_slide_xml(spTree_children: list, bg_color: str = 'FFFFFF') -> bytes:
    """
    Wrap *spTree_children* (lxml Element list) into a complete
    slide XML document and return UTF-8 bytes.
    """
    root = etree.Element(
        '{http://schemas.openxmlformats.org/presentationml/2006/main}sld',
        nsmap=NSMAP,
    )
    cSld = etree.SubElement(root, '{http://schemas.openxmlformats.org/presentationml/2006/main}cSld')

    # Background
    bg = etree.SubElement(cSld, '{http://schemas.openxmlformats.org/presentationml/2006/main}bg')
    bgPr = etree.SubElement(bg, '{http://schemas.openxmlformats.org/presentationml/2006/main}bgPr')
    solidFill = etree.SubElement(bgPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill')
    srgbClr = etree.SubElement(solidFill, '{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr')
    srgbClr.set('val', bg_color)

    # Shape tree
    spTree = etree.SubElement(cSld, '{http://schemas.openxmlformats.org/presentationml/2006/main}spTree')

    # Required nvGrpSpPr
    nvGrpSpPr = etree.SubElement(spTree, '{http://schemas.openxmlformats.org/presentationml/2006/main}nvGrpSpPr')
    cNvPr = etree.SubElement(nvGrpSpPr, '{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr')
    cNvPr.set('id', '1')
    cNvPr.set('name', '')
    etree.SubElement(nvGrpSpPr, '{http://schemas.openxmlformats.org/presentationml/2006/main}cNvGrpSpPr')
    etree.SubElement(nvGrpSpPr, '{http://schemas.openxmlformats.org/presentationml/2006/main}nvPr')

    # grpSpPr
    grpSpPr = etree.SubElement(spTree, '{http://schemas.openxmlformats.org/presentationml/2006/main}grpSpPr')
    xfrm = etree.SubElement(grpSpPr, '{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm')
    for tag, attrs in [('off', {'x': '0', 'y': '0'}),
                       ('ext', {'cx': '0', 'cy': '0'}),
                       ('chOff', {'x': '0', 'y': '0'}),
                       ('chExt', {'cx': '0', 'cy': '0'})]:
        el = etree.SubElement(xfrm, '{http://schemas.openxmlformats.org/drawingml/2006/main}' + tag)
        for k, v in attrs.items():
            el.set(k, v)

    for child in spTree_children:
        spTree.append(child)

    clrMapOvr = etree.SubElement(root, '{http://schemas.openxmlformats.org/presentationml/2006/main}clrMapOvr')
    etree.SubElement(clrMapOvr, '{http://schemas.openxmlformats.org/drawingml/2006/main}masterClrMapping')

    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)


def build_slide_rels_xml(media_rids: dict[str, str]) -> bytes:
    """
    Build the .rels XML for a slide.
    *media_rids*: {rId: target_path}
    """
    NS = 'http://schemas.openxmlformats.org/package/2006/relationships'
    root = etree.Element('{%s}Relationships' % NS)
    for rid, target in media_rids.items():
        rel = etree.SubElement(root, '{%s}Relationship' % NS)
        rel.set('Id', rid)
        rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
        rel.set('Target', target)
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
