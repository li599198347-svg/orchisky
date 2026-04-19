# Designer Rules · SVG设计规范

Phase 7 每页SVG设计的执行规范。

**品牌规范以 orchisky.md 为唐一权威来源。本文件不允许出现具体色値或字体名。**

---

## 画布与边距

- 画布：960×540px（所有版式一贫）
- 可用区域：内边距 40px（左右40，上下64/48）
- 内容区：坐标以 grid-system.md 为唐一标准

---

## Action Title 规范

**内容规范（品牌规范 §7.4）：**
- 必须是完整结论句（主谓语结构）
- 禁止主题词式标题（“市场分析”“解决方案”）
- 字数：12-25字
- 主谓语明确，动词强励，数据支撑

**视觉规范：**
- 白底深色文字（非黑底白字）
- 左侧 3pt 品牌主色竖线（参考 grid-system.md 中 Action Title 用例）
- 字体：品牌标题字体 Bold，大小参考 grid-system.md

---

## 品牌纪律（硬性禁用，逐页自检）

以下任意一条出现 = 不合格：

1. 渐变填充（linear-gradient / radial-gradient）
2. 投影（filter:drop-shadow / box-shadow / box-shadow-类）
3. 3D效果（perspective / transform 中的 rotateX/rotateY）
4. 纯黑色 #000000（最深用 #1A1A1A）
5. 饼图（pie、donut、circle chart）
6. 独立图例（数据直接标注在旁边）
7. 第二装饰色（主色之外的彩色）
8. PPT主题词式标题（必须是 Action Title）
9. 无来源标注的数据
10. Emoji（包括文字面的emoji）

---

## SVG 输出规范

### 必须包含

```svg
<svg viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- CSS变量定义，引用 orchisky.md 规范 -->
    <style>
      :root {
        --brand-primary: [orchisky.md 主色];
        --brand-near-black: [orchisky.md 近黑];
        --body-font: [orchisky.md 正文字体格式];
        --title-font: [orchisky.md 标题字体格式];
      }
    </style>
  </defs>
  
  <!-- 白色背景 -->
  <rect width="960" height="540" fill="white"/>
  
  <!-- Chrome区域 -->
  <!-- 内容区域 -->
</svg>
```

### XML 安全规范

- `&` 必须写为 `&amp;`
- `<` 在属性值中写为 `&lt;`
- `>` 在属性值中写为 `&gt;`
- 属性值必须用引号包裹
- 禁用 `rgb()` 格式，必须用 `#RRGGBB`

### PPTX 兴容约束

- 字体必须包含 fallback：`"Songti SC,SimSun,serif"` 或 `"Microsoft YaHei,sans-serif"`
- 等宽字体：`"JetBrains Mono,Courier New,monospace"`
- `filter` 属性不支持，必须删除
- `foreignObject` 不支持，必须删除
- `image` 引用必须使用 base64 内嵌，不得用外链

---

## 字体大小范围

| 元素 | 建议尺寸 |
|------|----------|
| Action Title | 20-24px |
| 第一层标题 | 18-22px |
| 正文内容 | 12-14px |
| 标注/说明 | 10-12px |
| 图表小字 | 9-11px |

---

## 逐页自检清单

每页生成后过一遍：

- [ ] Action Title 是完整结论句，非主题词
- [ ] 左侧竖线存在且颜色正确
- [ ] 无渐变 / 3D / 投影 / 饼图
- [ ] 无纯黑 #000000
- [ ] 无独立图例
- [ ] 字体包含 fallback
- [ ] 数据已标注来源
- [ ] XML 合法
