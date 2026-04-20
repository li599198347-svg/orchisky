# Components · 兰之天 现场工业端 V1.0

> 本文件与 `design-tokens.md` 同源，定义 **16 个核心组件**的结构、尺寸、状态与 HTML 片段。
> 所有片段都可直接复制进 PDA / Pad 原型，无需再改色值。

---

## 组件索引

| # | 组件 | 设备 | 关键特征 |
|---|---|---|---|
| 01 | PDA StatusBar | PDA | 24px，黑底白字 |
| 02 | PDA Topbar | PDA | 56px，蓝底白字，左返回右功能 |
| 03 | Pad AppBar | Pad | 56px，白底蓝字，禁止做 Hero |
| 04 | Tabbar / 侧边 Tab | Pad | 56px，图标+标签，选中左边条 4px |
| 05 | KPI 卡片 | PDA/Pad | 数字 mono，无阴影 |
| 06 | 列表项（行） | PDA/Pad | 44px 高，1px ink-200 分隔线 |
| 07 | 表格 | Pad | 表头 ink-100，无竖线 |
| 08 | 输入框 Field | PDA/Pad | 40px 高，白底 ink-300 边 |
| 09 | 按钮系 | PDA/Pad | ≥48px，无圆胶囊 |
| 10 | 扫码区 Scan Frame | PDA | 64% 屏宽，4 角 L 标记 |
| 11 | 状态 Chip | PDA/Pad | 2px 圆角，浅底 600 字 |
| 12 | 底部 CTA 条 | PDA/Pad | 48px，白底上边框，≤3 按钮 |
| 13 | Drawer / 抽屉 | Pad | 右侧 480px，shadow-overlay |
| 14 | 空状态 | PDA/Pad | 线框图 + 一句话，禁 emoji |
| 15 | Toast / 提示 | PDA/Pad | 顶部 3s，左 3px 边条 |
| 16 | Badge / 数字角标 | PDA/Pad | 18px 圆，ink-0 底 blue-500 字 |

---

## 01 · PDA StatusBar

```html
<div class="pda-statusbar">
  <span class="num">09:42</span>
  <span class="sb-icons">
    <span>5G</span><span>Wi-Fi</span><span class="num">87%</span>
  </span>
</div>
```

```css
.pda-statusbar{
  height: var(--h-statusbar); padding: 0 var(--sp-4);
  display:flex; justify-content:space-between; align-items:center;
  background: var(--ink-800); color: var(--ink-0);
  font-size: var(--fs-pda-micro);
}
.sb-icons{ display:flex; gap: var(--sp-2); }
```

**严禁**：彩色背景、装饰图形、企业 logo。

---

## 02 · PDA Topbar

```html
<header class="pda-topbar">
  <button class="tb-back" aria-label="返回">←</button>
  <h1 class="tb-title">入库申请单扫码</h1>
  <button class="tb-action" aria-label="菜单">⋮</button>
</header>
```

```css
.pda-topbar{
  height: var(--h-topbar); padding: 0 var(--sp-4);
  display:flex; align-items:center; justify-content:space-between;
  background: var(--blue-500); color: var(--ink-0);
}
.tb-title{ font-size: var(--fs-pda-page); font-weight: 500; margin: 0; }
.tb-back, .tb-action{
  width: 40px; height: 40px;
  background: transparent; border: 0; color: var(--ink-0); font-size: 20px;
}
```

**只有 Topbar 允许用 blue-500 大面积底色。**

---

## 03 · Pad AppBar

```html
<header class="pad-appbar">
  <div class="ab-left">
    <span class="ab-brand">Orchisky 现场端</span>
    <span class="ab-crumb">设备管理 / 点检执行</span>
  </div>
  <div class="ab-right">
    <span>张师傅 · 机修班</span>
    <button class="ab-logout" aria-label="退出">⎋</button>
  </div>
</header>
```

```css
.pad-appbar{
  height: var(--h-appbar); padding: 0 var(--sp-5);
  display:flex; align-items:center; justify-content:space-between;
  background: var(--ink-0); border-bottom: 1px solid var(--ink-200); color: var(--ink-700);
}
.ab-brand{ font-size: var(--fs-pad-body); font-weight: 700; color: var(--blue-500); margin-right: var(--sp-5); }
.ab-crumb{ font-size: var(--fs-pad-small); color: var(--ink-500); }
.ab-right{ display:flex; align-items:center; gap: var(--sp-4); font-size: var(--fs-pad-small); color: var(--ink-600); }
.ab-logout{ width:40px; height:40px; border:0; background:transparent; color:var(--ink-500); }
```

**内页严禁演化为 Hero 大标题区。**

---

## 04 · Tabbar（Pad 左侧导航）

```html
<nav class="pad-sidebar">
  <a class="sb-item active"><span class="sb-ico">◨</span><span>工单</span></a>
  <a class="sb-item"><span class="sb-ico">⚙</span><span>设备</span></a>
</nav>
```

```css
.pad-sidebar{ width: 80px; background: var(--ink-50); border-right: 1px solid var(--ink-200); }
.sb-item{
  height: var(--h-tabbar);
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap: 2px;
  color: var(--ink-600); font-size: var(--fs-pad-small); border-left: 3px solid transparent; text-decoration:none;
}
.sb-item.active{ color: var(--blue-500); background: var(--blue-50); border-left-color: var(--blue-500); }
.sb-ico{ font-size: 20px; }
```

---

## 05 · KPI 卡片

```html
<div class="kpi-card">
  <div class="kpi-label">今日待点检</div>
  <div class="kpi-value"><span class="num kpi-num">18</span><span class="kpi-unit">台</span></div>
  <div class="kpi-sub">已完成 <span class="num">12</span></div>
</div>
```

```css
.kpi-card{ padding: var(--sp-4); background: var(--ink-0); border: 1px solid var(--ink-200); border-radius: var(--radius-md); }
.kpi-label{ font-size: var(--fs-pad-small); color: var(--ink-500); }
.kpi-value{ margin: var(--sp-2) 0 var(--sp-1); display:flex; align-items:baseline; gap: var(--sp-2); }
.kpi-num{ font-size: var(--fs-pad-kpi); font-weight: 700; color: var(--ink-800); line-height: 1; }
.kpi-unit{ font-size: var(--fs-pad-small); color: var(--ink-500); }
.kpi-sub{ font-size: var(--fs-pad-small); color: var(--ink-500); }
```

---

## 06 · 列表项

```html
<ul class="list">
  <li class="list-item">
    <div class="li-main">
      <div class="li-title">PO2026-04-0123 · 轴承 6205-2RS</div>
      <div class="li-sub">华瑞 · <span class="num">200</span>pcs</div>
    </div>
    <div class="li-meta"><span class="chip chip-success">已到</span><span class="li-arrow">›</span></div>
  </li>
</ul>
```

```css
.list{ list-style:none; margin:0; padding:0; }
.list-item{
  min-height: var(--h-row); padding: var(--sp-3) var(--sp-4);
  display:flex; align-items:center; justify-content:space-between; gap: var(--sp-3);
  background: var(--ink-0); border-bottom: 1px solid var(--ink-200);
}
.li-title{ font-size: var(--fs-pad-body); color: var(--ink-800); }
.li-sub{ font-size: var(--fs-pad-small); color: var(--ink-500); margin-top: 2px; }
.li-meta{ display:flex; align-items:center; gap: var(--sp-3); }
.li-arrow{ color: var(--ink-400); font-size: 18px; }
```

---

## 07 · 表格（Pad 专用）

```css
.pad-table{ width:100%; border-collapse:collapse; }
.pad-table thead th{
  height:40px; padding:0 var(--sp-4); text-align:left;
  font-weight:500; font-size:var(--fs-pad-small); color:var(--ink-600);
  background:var(--ink-100); border-bottom:1px solid var(--ink-200);
}
.pad-table tbody td{
  height:var(--h-row); padding:0 var(--sp-4);
  font-size:var(--fs-pad-body); color:var(--ink-800); border-bottom:1px solid var(--ink-200);
}
.pad-table tbody tr:hover td{ background: var(--ink-50); }
.align-right{ text-align: right; }
```

**严禁**：竖向分割线、斑马纹、彩色表头。

---

## 08 · 输入框 Field

```css
.field{ display:flex; flex-direction:column; gap:var(--sp-1); }
.field-label{ font-size:var(--fs-pad-small); color:var(--ink-600); }
.req{ color:var(--danger-600); font-style:normal; margin-left:2px; }
.field-input{
  height:var(--h-field); padding:0 var(--sp-3);
  font-size:var(--fs-pad-body); color:var(--ink-800);
  background:var(--ink-0); border:1px solid var(--ink-300); border-radius:var(--radius-md); outline:none;
}
.field-input:focus{ border-color:var(--blue-500); box-shadow:var(--focus-ring); }
.field-input[aria-invalid="true"]{ border-color:var(--danger-600); }
```

---

## 09 · 按钮系

```css
.btn{
  height:var(--h-btn); min-width:88px; padding:0 var(--sp-4);
  font-size:var(--fs-pad-body); font-weight:500; border-radius:var(--radius-md);
  border:1px solid transparent; background:transparent; cursor:pointer;
  display:inline-flex; align-items:center; justify-content:center; gap:var(--sp-2);
}
.btn-primary{ background:var(--blue-500); color:var(--ink-0); }
.btn-primary:hover{ background:var(--blue-600); }
.btn-secondary{ background:var(--ink-0); border-color:var(--ink-300); color:var(--ink-700); }
.btn-danger{ background:var(--ink-0); border-color:var(--danger-600); color:var(--danger-600); }
.btn-ghost{ background:transparent; color:var(--ink-600); }
.btn-sm{ height:var(--h-btn-sm); min-width:64px; font-size:var(--fs-pad-small); }
```

---

## 10 · 扫码区（PDA）

```css
.scan-frame{ position:relative; width:64%; aspect-ratio:1/1; margin:var(--sp-5) auto; background:var(--ink-800); }
.sf-corner{ position:absolute; width:24px; height:24px; border-color:var(--blue-500); border-style:solid; border-width:0; }
.sf-corner.tl{ top:0; left:0; border-top-width:3px; border-left-width:3px; }
.sf-corner.tr{ top:0; right:0; border-top-width:3px; border-right-width:3px; }
.sf-corner.bl{ bottom:0; left:0; border-bottom-width:3px; border-left-width:3px; }
.sf-corner.br{ bottom:0; right:0; border-bottom-width:3px; border-right-width:3px; }
.sf-hint{ position:absolute; bottom:var(--sp-4); left:0; right:0; text-align:center; color:var(--ink-0); font-size:var(--fs-pda-small); }
```

---

## 11 · 状态 Chip

```css
.chip{
  display:inline-flex; align-items:center; gap:var(--sp-1);
  padding:2px var(--sp-2); border-radius:var(--radius-sm);
  font-size:var(--fs-pad-small); line-height:1.4; border:1px solid transparent;
}
.chip-neutral{ background:var(--ink-100); color:var(--ink-700); }
.chip-info   { background:var(--blue-50);  color:var(--blue-600); }
.chip-success{ background:var(--success-50); color:var(--success-600); }
.chip-warning{ background:var(--warning-50); color:var(--warning-600); }
.chip-danger { background:var(--danger-50);  color:var(--danger-600); }
```

---

## 12 · 底部 CTA 条

```html
<footer class="bottom-cta">
  <button class="btn btn-ghost">取消</button>
  <div class="cta-right">
    <button class="btn btn-secondary">暂存</button>
    <button class="btn btn-primary">提交入库</button>
  </div>
</footer>
```

```css
.bottom-cta{
  position:sticky; bottom:0; height:var(--h-bottombar); padding:0 var(--sp-4);
  display:flex; align-items:center; justify-content:space-between;
  background:var(--ink-0); border-top:1px solid var(--ink-200);
}
.cta-right{ display:flex; gap:var(--sp-2); }
.bottom-cta .btn{ height:40px; }
```

---

## 13 · Drawer（Pad）

```css
.drawer{
  position:fixed; top:0; right:0; width:480px; height:100%;
  background:var(--ink-0); box-shadow:var(--shadow-overlay);
  display:flex; flex-direction:column;
}
.drawer-head{
  height:var(--h-appbar); padding:0 var(--sp-5);
  display:flex; align-items:center; justify-content:space-between;
  border-bottom:1px solid var(--ink-200);
}
.drawer-body{ flex:1; padding:var(--sp-5); overflow:auto; }
.drawer-foot{
  height:var(--h-bottombar); padding:0 var(--sp-5);
  display:flex; align-items:center; justify-content:flex-end; gap:var(--sp-2);
  border-top:1px solid var(--ink-200);
}
```

---

## 14 · 空状态

```css
.empty{ padding:var(--sp-5); text-align:center; color:var(--ink-500); }
.empty-illu{ width:96px; height:96px; opacity:.7; }
.empty-title{ font-size:var(--fs-pad-body); color:var(--ink-700); margin-top:var(--sp-3); }
.empty-sub{ font-size:var(--fs-pad-small); margin-top:var(--sp-1); }
```

**严禁** emoji、卡通图形做空状态图。

---

## 15 · Toast

```css
.toast{
  position:fixed; top:88px; left:50%; transform:translateX(-50%);
  padding:var(--sp-3) var(--sp-4);
  background:var(--ink-0); border-left:3px solid var(--blue-500);
  border-radius:var(--radius-md); box-shadow:var(--shadow-overlay);
  font-size:var(--fs-pad-body); color:var(--ink-800);
  display:flex; align-items:center; gap:var(--sp-2);
}
.toast-success{ border-left-color:var(--success-600); }
.toast-warning{ border-left-color:var(--warning-600); }
.toast-danger { border-left-color:var(--danger-600); }
```

---

## 16 · Badge

```css
.badge-wrap{ position:relative; display:inline-block; }
.badge{
  position:absolute; top:-4px; right:-8px;
  min-width:18px; height:18px; padding:0 5px; border-radius:9px;
  background:var(--blue-500); color:var(--ink-0);
  font-size:11px; display:inline-flex; align-items:center; justify-content:center;
}
.badge-danger{ background:var(--danger-600); }
```

> Badge 圆形是极少数允许 border-radius 50% 的场景，其它按钮/卡片不得用胶囊。

---

## 图标（V2.0 §7）

- 全部线性 Lucide，24×24，2px 描边
- 禁止填充彩色、多色渐变、3D
- 默认 `--ink-600`，激活 `--blue-500`

---

## 质检清单

| 项 | 通过条件 |
|---|---|
| Topbar/AppBar 高度 | = 56px，不出现 Hero |
| 列表行高 | ≥44px |
| 按钮主操作高度 | ≥48px |
| Chip | 浅底+600字，不仅靠颜色 |
| 输入框 | 白底+ink-300边，焦点 blue-500 |
| 空状态 | 线框图+灰字，无 emoji |
| Drawer 阴影 | `--shadow-overlay`，卡片内部不得有 |
| 图标 | Lucide 线性 24px 2px |
