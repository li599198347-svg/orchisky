# PPTX Native Rules · SVG转原生PPT规范

> **核心原则**：SVG 是唯一真源，原生 PPT 由机器从 SVG 转换得到，不手写。

---

## 执行步骤

### 步骤1 · 调用工具链

```python
import sys
sys.path.insert(0, '/mnt/skills/user/orchisky-ppt/assets')
from svg_to_pptx_wrapper import svg_to_native_pptx
from pathlib import Path

svg_files = sorted(Path('./workspace/svg_final').glob('*.svg'))
output = Path('./workspace/deliverables/方案.pptx')

success = svg_to_native_pptx(
    svg_files=svg_files,
    output_path=output,
    canvas_format='ppt169',
    verbose=True,
)
assert success, "转换失败,检查 SVG 是否规范"
```

### 步骤2 · 验证产物

```
文件大小：正常范围 50-300 KB
LibreOffice 转 PDF 抖点：
  libreoffice --headless --convert-to pdf output.pptx
抄南3页进行目测检查
```

### 步骤3 · 交付三件套

1. `方案.pptx` · 原生可编辑 PPT
2. `方案.pdf` · 打印分发版
3. `svg_final/` · SVG 真源

---

## 支持的 SVG 元素

| 元素 | 支持度 | 说明 |
|---|---|---|
| `<rect>` | ✅ 完整 | 支持圆角、填充、描边 |
| `<circle>/<ellipse>` | ✅ 完整 | |
| `<line>/<polygon>/<polyline>` | ✅ 完整 | **箭头用`<polygon>`** |
| `<path>` | ✅ 完整 | 贝塞尔曲线通过细分近似 |
| `<text>/<tspan>` | ✅ 完整 | CJK自动双字体，可编辑 |
| `<image>` | ✅ 完整 | base64内嵌 |
| `<marker>` on `<path>` | ❌ 不支持 | 静默丢失，改用`<polygon>` |
| `<g transform="rotate">` | ⚠️ 有风险 | 子元素坐标偏移，禁用 |
| 满色/投影滤镜 | ⚠️ 有限 | 不稳定，避免 |

---

## 常见问题排查

| 现象 | 最可能原因 | 快速修复 |
|---|---|---|
| 整页空白 | SVG含未转义`&`或XML损坏 | 工具链已自动修复`&` |
| 箭头消失 | 用了`<marker>`在`<path>`上 | 改用`<polygon>`画箭头 |
| 多行文字变一行 | 用了`\n`换行 | 改用`<tspan dy>`或独立`<text>` |
| 颜色变黑 | 用了`rgb()`格式颜色 | 改为hex格式 |
| 元素位置偏移 | `<g transform="rotate">`坐标偏移 | 用元素级绝对坐标替代 |
| 文字无法编辑 | 非原生模式转换 | 确认通过wrapper调用 |

---

## 硬性约束

- 回到修改 SVG 原文，重新转换（不直接改 PPT）
- 箭头必须用 `<polygon>` 画头部
- 字体包含 fallback：`"Songti SC,SimSun,serif"`
- 禁用 `rgb()` 颜色格式，必须用 hex
