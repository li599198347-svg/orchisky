"""Markdown to plain text conversion and notes slide XML generation."""

from __future__ import annotations
import re
from typing import Optional


def md_to_plain(md: str) -> str:
    """
    Strip Markdown formatting from *md* and return plain text
    suitable for a PowerPoint notes placeholder.
    """
    # Remove headings
    text = re.sub(r'^#{1,6}\s+', '', md, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r'[*_]{1,3}(.+?)[*_]{1,3}', r'\1', text)
    # Remove inline code
    text = re.sub(r'`(.+?)`', r'\1', text)
    # Remove links
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    # Remove images
    text = re.sub(r'!\[.*?\]\(.+?\)', '', text)
    # Remove horizontal rules
    text = re.sub(r'^[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
    # Collapse multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def build_notes_slide_xml(notes_text: str, slide_rid: str = 'rId1') -> bytes:
    """
    Build the XML bytes for a notes slide containing *notes_text*.
    *slide_rid* is the relationship ID pointing to the parent slide.
    """
    # Escape XML special chars
    safe = (notes_text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))

    xml = f"""<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<p:notes xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
         xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
         xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr/>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="2" name="Slide Image Placeholder 1"/>
          <p:cNvSpPr><a:spLocks noGrp="1" noRot="1" noChgSz="1"/></p:cNvSpPr>
          <p:nvPr><p:ph type="sldImg"/></p:nvPr>
        </p:nvSpPr>
        <p:spPr/>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="3" name="Notes Placeholder 2"/>
          <p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>
          <p:nvPr><p:ph type="body" idx="1"/></p:nvPr>
        </p:nvSpPr>
        <p:spPr/>
        <p:txBody>
          <a:bodyPr/>
          <a:lstStyle/>
          <a:p><a:r><a:t>{safe}</a:t></a:r></a:p>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:notes>"""
    return xml.encode('utf-8')
