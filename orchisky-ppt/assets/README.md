# Orchisky PPT V4.0 · 代码资产目录

## V4.0 主资产（推荐使用）

### svg_to_pptx/ · SVG→原生 PPTX 工具链 ★

**用途**：把 SVG 文件批量转成原生可编辑的 PPTX 文件。

**使用方式**：

```python
from svg_to_pptx_wrapper import svg_to_native_pptx
from pathlib import Path

svg_files = sorted(Path('svg_final').glob('*.svg'))
svg_to_native_pptx(svg_files, Path('output.pptx'))
```

**只用这个 wrapper**，不要直接调用 svg_to_pptx/ 内部模块。

---

## LEGACY · V3.0 遗留资产（不主推）

| 文件 | 用途 | 何时用 |
|---|---|---|
| `flat_helpers.py` | 扁平化形状辅助 | 手工拼 1-3 页小 PPT |
| `fix_theme_fonts.py` | 修复主题字体遗漏 | 无 SVG 源时构造新 PPT |
| `apply_orchisky_theme.py` | 应用兰之天主题 | 兼容旧项目 |
| `constants.py` | 颜色/字体常量 | 了解 V3.0 的设计约束 |
| `theme1_orchisky.xml` | 主题 XML 模板 | 极少情况下修改主题 |

---

## 文件完整清单（V4.0）

```
assets/
├── README.md
├── svg_to_pptx_wrapper.py       # ★ 对外入口（V4.0）
├── svg_to_pptx/                 # ★ 工具链主体（V4.0）
├── flat_helpers.py              # ⚠️ LEGACY
├── fix_theme_fonts.py           # ⚠️ LEGACY
├── apply_orchisky_theme.py      # ⚠️ LEGACY
├── constants.py                 # ⚠️ LEGACY
└── theme1_orchisky.xml          # ⚠️ LEGACY
```

---

## 版本历史

- **V4.0** (2026-04-17)：引入 ppt-master 工具链，废弃手工 python-pptx 路径
- **V3.0** （更早）：手工 flat_helpers + 逐 shape 路径（已废弃）
