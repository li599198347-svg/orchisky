# orchisky-ppt assets

## 目录结构

```
assets/
├── README.md                  ← 本文件
├── apply_orchisky_theme.py    ← 应用品牌主题到PPTX
├── constants.py               ← 全局常量定义
├── fix_theme_fonts.py         ← 修复主题字体
├── flat_helpers.py            ← SVG扁平化辅助工具
├── svg_to_pptx_wrapper.py     ← 工具链入口（唯一调用方式）
├── theme1_orchisky.xml        ← Orchisky品牌PPTX主题文件
└── svg_to_pptx/               ← 底层SVG→PPTX转换算法库
    ├── __init__.py
    ├── drawingml_context.py
    ├── drawingml_converter.py
    ├── drawingml_elements.py
    ├── drawingml_paths.py
    ├── drawingml_styles.py
    ├── drawingml_utils.py
    ├── pptx_builder.py
    ├── pptx_cli.py
    ├── pptx_dimensions.py
    ├── pptx_discovery.py
    ├── pptx_media.py
    ├── pptx_notes.py
    └── pptx_slide_xml.py
```

## 使用方式

```python
import sys
sys.path.insert(0, '/mnt/skills/user/orchisky-ppt/assets')
from svg_to_pptx_wrapper import svg_to_native_pptx
from pathlib import Path

svg_files = sorted(Path('./svg_output').glob('*.svg'))
success = svg_to_native_pptx(
    svg_files=svg_files,
    output_path=Path('./output.pptx'),
    canvas_format='ppt169',
    verbose=True,
)
```
