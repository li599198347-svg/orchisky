# Iconography — Orchisky

## One library, one style

Across all Orchisky surfaces there is exactly *one* icon library: **Lucide Icons** (open-source, MIT).
No mixing with Font Awesome, Material Icons, Heroicons, or emoji substitutes.

---

## Grid & stroke

| Property | Value |
|----------|-------|
| Grid | 24 × 24 px |
| Stroke width | **2 px** (default UI) |
| Stroke width | **1.5 px** (dense / small contexts) |
| Style | Outlined only — no Filled variants |
| Corner radius | 2 px on strokes (Lucide default) |

---

## Sizing by context

| Context | Size |
|---------|------|
| Button (inline) | 16 × 16 px |
| List item leading icon | 20 × 20 px |
| Card / section header | 24 × 24 px |
| Empty state illustration | 48 × 48 px or 96 × 96 px |

---

## Color

- Default: inherit parent text color (`ink-600 #555555` for secondary UI)
- Interactive (hover / active): `blue-500 #1070F0`
- Destructive actions: `#B01C1C`
- Disabled: `ink-400 #BBBBBB`

Icons **never** carry their own decorative color; they reflect the semantic role of the surrounding element.

---

## Prohibited

| Prohibited | Why |
|------------|-----|
| Filled / solid variants | Breaks visual consistency |
| Multi-color icons | Violates single-accent rule |
| 3D / skeuomorphic icons | Conflicts with flat design principle |
| Emoji as functional icons | Inaccessible, unscalable |
| Mixing Lucide with another library | Inconsistent stroke weight |
| Custom gradient fills | Not permitted in any Orchisky surface |

---

## Import (HTML / JSX)

```html
<!-- CDN (HTML prototype) -->
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="package" style="width:20px;height:20px;"></i>
<script>lucide.createIcons();</script>
```

```jsx
// React / JSX
import { Package, ChevronRight, AlertTriangle } from 'lucide-react';
<Package size={20} strokeWidth={2} />
```

---

## Common icon vocabulary

| Action | Icon name |
|--------|-----------|
| Add / New | `plus`, `plus-circle` |
| Edit | `pencil`, `edit-2` |
| Delete | `trash-2` |
| Search | `search` |
| Filter | `filter`, `sliders-horizontal` |
| Export | `download`, `file-down` |
| Print | `printer` |
| Refresh | `refresh-cw` |
| Settings | `settings-2` |
| Close / Cancel | `x` |
| Confirm / Done | `check`, `check-circle-2` |
| Warning | `alert-triangle` |
| Info | `info` |
| Error | `x-circle` |
| Scan (PDA) | `scan-line`, `qr-code` |
| Warehouse | `warehouse` |
| Package | `package`, `box` |
| User / Worker | `user`, `hard-hat` |
| Chart | `bar-chart-2`, `line-chart` |

---

*Orchisky Iconography · V2.0 · 2026-04*
