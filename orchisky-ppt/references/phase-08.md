# Phase 8 · 质检与交付

> 可插拔模块。独立升级不影响其他Phase。
> 本Phase执行五层质检，打包交付PPTX+SVG预览。

---

## 入场条件

- Phase 7完成卡已确认
- 全部SVG文件已生成

---

## 阶段提示卡

```
┌─────────────────────────────────────────┐
│ Phase 8 · 质检与交付                    │
├─────────────────────────────────────────┤
│ 这一步要做什么                           │
│   五层质检 + 转换PPTX + 打包交付        │
│                                         │
│ 用什么方法                               │
│   对照quality-audit-protocol.md执行     │
│                                         │
│ 你需要做的                               │
│   确认最终交付物满足需求                 │
└─────────────────────────────────────────┘
```

---

## 执行步骤

### 步骤1：质检执行

读取 `quality-audit-protocol.md`，执行三级Gate质检：

- **Gate 1**：内容完整性（空内容检测）
- **Gate 2**：排版规范（单行字数、字体）
- **Gate 3**：XML合法性（特殊字符、颜色格式）

输出质检报告：ERROR / WARNING 数量及清单。

### 步骤2：SVG → PPTX 转换

调用 `svg_to_pptx_wrapper.py`：

```python
from svg_to_pptx_wrapper import svg_to_native_pptx
success = svg_to_native_pptx(
    svg_files=svg_files,
    output_path='/mnt/user-data/outputs/presentation.pptx',
    canvas_format='ppt169'
)
```

### 步骤3：交付打包

交付物清单：
1. `presentation.pptx` — 可编辑PPTX
2. `slide_XX.svg` × N — SVG预览版（可在浏览器查看）
3. QC报告 — 质检结果摘要

调用 `present_files` 呈现给用户。

---

## 完成卡

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Phase 8 · 质检与交付 完成
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
入场条件    Phase 7 ✓
本阶段输出  PPTX + SVG预览版 + QC报告
关键结论    质检：ERROR [N] / WARNING [N]
待确认      交付物是否满足需求？
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
全部8个Phase已完成，演示文稿已交付。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
