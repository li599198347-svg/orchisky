function AppHeader({ user = '张工程师' }) {
  return (
    <header style={{ height: 56, background: '#001529', color: '#fff', display: 'flex', alignItems: 'center', padding: '0 24px' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12, width: 220 - 24 }}>
        <div style={{ width: 28, height: 28, background: '#334155', borderRadius: 4, display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontWeight: 700, fontSize: 14 }}>O</div>
        <span style={{ fontSize: 15, fontWeight: 600 }}>Orchisky 平台</span>
      </div>
      <nav style={{ display: 'flex', gap: 0, flex: 1, marginLeft: 24, height: '100%' }}>
        {['工作台', '生产', '质量', '仓储', '设置'].map((t, i) => (
          <a key={t} style={{ padding: '0 20px', display: 'flex', alignItems: 'center', fontSize: 14, color: i === 0 ? '#fff' : 'rgba(255,255,255,0.65)', background: i === 0 ? 'rgba(255,255,255,0.08)' : 'transparent', borderBottom: i === 0 ? '2px solid #fff' : '2px solid transparent', cursor: 'pointer' }}>{t}</a>
        ))}
      </nav>
      <div style={{ display: 'flex', alignItems: 'center', gap: 16, color: 'rgba(255,255,255,0.85)', fontSize: 13 }}>
        <span style={{ width: 28, height: 28, background: '#334155', borderRadius: '50%', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', fontSize: 12, fontWeight: 600 }}>{user[0]}</span>
        <span>{user}</span>
      </div>
    </header>
  );
}
window.AppHeader = AppHeader;
