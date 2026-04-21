function SideNav({ active, onNav }) {
  const items = [
    { id: 'dashboard', label: '数据总览', icon: '◧' },
    { id: 'orders', label: '工单管理', icon: '▤' },
    { id: 'materials', label: '物料主数据', icon: '◍' },
    { id: 'quality', label: '质量检验', icon: '✓' },
    { id: 'equipment', label: '设备管理', icon: '⚙' },
    { id: 'reports', label: '报表中心', icon: '▦' },
  ];
  return (
    <aside style={{ width: 220, background: '#fff', borderRight: '1px solid #F0F0F0',
      padding: '8px 0', flexShrink: 0, minHeight: 'calc(100vh - 56px)' }}>
      {items.map(it => {
        const on = it.id === active;
        return (
          <div key={it.id} onClick={() => onNav(it.id)}
            style={{
              height: 40, margin: '2px 8px', padding: '0 16px',
              display: 'flex', alignItems: 'center', gap: 12,
              borderRadius: 6, cursor: 'pointer',
              background: on ? '#EFF6FF' : 'transparent',
              color: on ? '#1677FF' : 'rgba(0,0,0,0.88)',
              fontWeight: on ? 600 : 400, fontSize: 14,
            }}>
            <span style={{ width: 14, textAlign: 'center', fontSize: 14 }}>{it.icon}</span>
            <span>{it.label}</span>
          </div>
        );
      })}
    </aside>
  );
}
window.SideNav = SideNav;
