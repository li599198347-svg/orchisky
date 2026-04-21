function Footer() {
  return (
    <footer style={{ background: '#1A1A1A', color: '#CCC' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '48px 24px 24px',
        display: 'grid', gridTemplateColumns: '2fr 1fr 1fr 1fr', gap: 40 }}>
        <div>
          <div style={{ color: '#fff', fontWeight: 700, fontSize: 18, marginBottom: 12 }}>江苏兰之天软件技术有限公司</div>
          <div style={{ fontSize: 13, lineHeight: 1.8, color: '#888' }}>
            Orchisky · 以咋询公司的严谨，交付制造业可信赖的数字化成果。
          </div>
        </div>
        {[
          { h: '解决方案', items: ['生产计划 APS', '车间执行 MES', '仓储物流 WMS', '质量追溯 QMS'] },
          { h: '客户与行业', items: ['汽车零部件', '半导体', '生物医药', '通用装备'] },
          { h: '资源', items: ['白皮书下载', '产品手册', '技术博客', '招聘'] },
        ].map(col => (
          <div key={col.h}>
            <div style={{ color: '#fff', fontWeight: 600, fontSize: 13, marginBottom: 12 }}>{col.h}</div>
            {col.items.map(it => (
              <div key={it} style={{ fontSize: 12, color: '#888', padding: '4px 0', cursor: 'pointer' }}>{it}</div>
            ))}
          </div>
        ))}
      </div>
      <div style={{ borderTop: '1px solid #333', padding: '16px 24px', maxWidth: 1200, margin: '0 auto',
        fontSize: 11, color: '#555', display: 'flex', justifyContent: 'space-between',
        fontFamily: 'Roboto Mono, monospace' }}>
        <span>© 2014–2026 Orchisky</span>
        <span>v2.0 · 2026-04</span>
      </div>
    </footer>
  );
}
window.Footer = Footer;
