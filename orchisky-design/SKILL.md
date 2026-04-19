---
name: orchisky-design
description: |
  Orchisky 品牌视觉规范强制执行器。当用户说"按兰之天规范""用公司规范""Orchisky 风格""强制规范"，
  或要求生成任何视觉交付物（Word、PPT、Excel、PDF、HTML、网页、界面、图表、看板）时触发。
  触发后强制读取 references/orchisky.md，所有视觉输出必须 100% 符合 Orchisky V1.0 规范，不询问用户风格偏好。

  触发关键词（以下任一）：
  - "按公司规范" / "按兰之天规范" / "Orchisky风格" / "强制规范" / "用我们的规范"
  - 生成 Word / PPT / Excel / PDF / HTML / 网页 / 界面 / 图表 / 看板 / 报告 / 方案
  - 任何视觉交付物，即使未说明风格
---

# Orchisky Design Skill

江苏兰之天软件技术有限公司官方视觉规范强制执行技能。

---

## 执行流程

```
用户触发
    ↓
Step 1: view references/orchisky.md（必须完整读取，不跳过）
    ↓
Step 2: 确认输出类型 → 读取对应文档技能
        Word  → /mnt/skills/public/docx/SKILL.md
        PPT   → /mnt/skills/public/pptx/SKILL.md
        Excel → /mnt/skills/public/xlsx/SKILL.md
        PDF   → /mnt/skills/public/pdf/SKILL.md
        网页/界面 → /mnt/skills/public/frontend-design/SKILL.md
    ↓
Step 3: 按规范生成
    ↓
Step 4: 输出前逐项自检（见下方清单）
```

---

## 输出前必检清单

- [ ] 唯一强调色 `#003D7A`，无第二装饰彩色
- [ ] 无渐变、无投影、无 3D 效果
- [ ] 字体仅微软雅黑 + 宋体-简，不超过两种
- [ ] 表格无竖线，横线 0.5pt `#E2E2E2`
- [ ] 状态标记符号 + 颜色双通道
- [ ] PPT Action Title 是完整结论句（非主题词）
- [ ] PPT Action Title 白底深色文字 + 左侧 3pt `#003D7A` 竖线（非黑底白字）
- [ ] 未使用纯黑 `#000000`，统一用 `#1A1A1A`
- [ ] 图表直接标注数值，无独立图例
- [ ] 数据有来源标注

---

## 速查核心参数

| 项目 | 值 |
|------|-----|
| 唯一强调色 | `#003D7A` |
| 近黑 | `#1A1A1A` |
| 正文色 | `#333333` |
| 辅助灰 | `#555555` |
| 注释灰 | `#888888` |
| 背景灰 | `#F5F5F5` |
| 浅蓝底 | `#E8F0FA` |
| 标题字体 | 微软雅黑 Microsoft YaHei |
| 正文字体 | 宋体-简 SimSun |
| Word 纸张 | A4，左3cm/右2.2cm/上2.5cm/下2cm |
| PPT 尺寸 | 16:9（33.87×19.05cm）或 A4 横向 |

完整规范见 `references/orchisky.md`。
