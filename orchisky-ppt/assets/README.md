# Orchisky PPT V5.0 · 代码资产目录

## V4.0 主资产（推荐使用）

### svg_to_pptx/ · SVG→原生 PPTX 工具链 ★

**用途**：把 SVG 文件转换为原生可编辑的 PPT

**入口**：`svg_to_pptx_wrapper.py` 中的 `svg_to_native_pptx()` 函数

**包含**：
- `svg_to_pptx/` — 底层转换工具链（ppt-master 项目）
- `apply_orchisky_theme.py` — 应用 Orchisky 品牌主题
- `flat_helpers.py` — 工具函数
- `constants.py` — 品牌色彩、字体、尺寸常量
- `theme1_orchisky.xml` — PPT 主题 XML 文件

## 使用方式

```python
from svg_to_pptx_wrapper import svg_to_native_pptx
from pathlib import Path

svg_files = sorted(Path('svg_final').glob('*.svg'))
success = svg_to_native_pptx(svg_files, Path('output.pptx'))
```

## 重要提示

- **不要直接调用** `svg_to_pptx/` 内部模块
- 统一通过 `svg_to_pptx_wrapper.py` 使用
- `constants.py` 为 V3.0 遗留资产，V4.0 主要用于参考

---

*Orchisky PPT V5.0 · 内部技术资产*
