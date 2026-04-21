function TopBar({ active = 'home', onNav }) {
  const items = [
    { id: 'home', label: '首页' },
    { id: 'solutions', label: '解决方案' },
    { id: 'cases', label: '客户案例' },
    { id: 'about', label: '关于我们' },
    { id: 'contact', label: '联系我们' },
  ];
  return (
    <header style={{ position: 'sticky', top: 0, zIndex: 10, background: '#fff',
      borderTop: '3px solid #1677FF', borderBottom: '1px solid #E2E2E2' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', height: 56, padding: '0 24px',
        display: 'flex', alignItems: 'center', gap: 40 }}>
        <span style={{ fontSize: 18, fontWeight: 700, color: '#1A1A1A' }}>Orchisky</span>
        <nav style={{ display: 'flex', gap: 28, flex: 1 }}>
          {items.map(it => (
            <a key={it.id} onClick={() => onNav?.(it.id)}
              style={{
                fontSize: 14,
                fontWeight: active === it.id ? 700 : 500,
                color: active === it.id ? '#1677FF' : '#333',
                cursor: 'pointer',
                paddingBottom: 2,
                borderBottom: active === it.id ? '2px solid #1677FF' : '2px solid transparent',
              }}>{it.label}</a>
          ))}
        </nav>
        <button onClick={() => onNav?.('contact')}
          style={{ height: 32, padding: '0 16px', background: '#1677FF', color: '#fff',
            border: 0, borderRadius: 4, fontSize: 13, fontWeight: 500, cursor: 'pointer' }}>
          预约咋询
        </button>
      </div>
    </header>
  );
}
window.TopBar = TopBar;
