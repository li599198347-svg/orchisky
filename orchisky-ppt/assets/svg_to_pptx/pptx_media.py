"""SVG to PNG conversion for Office compatibility mode."""

from __future__ import annotations
from pathlib import Path
from typing import Optional
import base64
import re


def extract_base64_image(data_uri: str) -> tuple[str, bytes]:
    """
    Extract media type and bytes from a data URI.
    E.g. 'data:image/png;base64,ABC123' -> ('image/png', b'...')
    """
    m = re.match(r'data:([^;]+);base64,(.+)', data_uri, re.DOTALL)
    if not m:
        raise ValueError(f"Not a valid data URI: {data_uri[:60]}...")
    media_type = m.group(1)
    data = base64.b64decode(m.group(2))
    return media_type, data


def media_ext_for_type(media_type: str) -> str:
    """Return file extension for a given MIME type."""
    mapping = {
        'image/png': '.png',
        'image/jpeg': '.jpg',
        'image/jpg': '.jpg',
        'image/gif': '.gif',
        'image/webp': '.webp',
        'image/svg+xml': '.svg',
    }
    return mapping.get(media_type, '.bin')


def ooxml_content_type(ext: str) -> str:
    """Return the Office Open XML content type for an image extension."""
    mapping = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml',
    }
    return mapping.get(ext.lower(), 'application/octet-stream')
