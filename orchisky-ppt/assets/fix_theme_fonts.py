"""fix_theme_fonts.py — 修复 PPTX 主题字体映射。"""

import zipfile
import shutil
import os
import re
from pathlib import Path


def fix_theme_fonts(pptx_path: str) -> bool:
    """将 PPTX 主题中的英文字体将5小为中文兼容字体。"""
    path = Path(pptx_path)
    if not path.exists():
        print(f"File not found: {pptx_path}")
        return False

    backup = path.with_suffix('.bak.pptx')
    shutil.copy2(path, backup)

    try:
        with zipfile.ZipFile(path, 'r') as z:
            names = z.namelist()
            theme_files = [n for n in names if 'theme' in n.lower() and n.endswith('.xml')]

        for theme_file in theme_files:
            with zipfile.ZipFile(path, 'r') as z:
                content = z.read(theme_file).decode('utf-8')

            # Replace Latin/EA font references
            content = re.sub(r'<a:latin typeface="[^"]*"', '<a:latin typeface="Microsoft YaHei"', content)
            content = re.sub(r'<a:ea typeface="[^"]*"', '<a:ea typeface="Microsoft YaHei"', content)

            # Write back
            import tempfile
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pptx') as tmp:
                tmp_path = tmp.name

            shutil.copy2(path, tmp_path)
            with zipfile.ZipFile(tmp_path, 'a') as z:
                z.writestr(theme_file, content.encode('utf-8'))

            shutil.move(tmp_path, path)

        print(f"Fixed fonts in {pptx_path}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        shutil.copy2(backup, path)
        return False
    finally:
        if backup.exists():
            backup.unlink()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        fix_theme_fonts(sys.argv[1])
