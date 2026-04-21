function Hero({ onCTA }) {
  return (
    <section style={{ background: '#fff', borderBottom: '1px solid #E2E2E2' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '96px 24px 80px' }}>
        <div style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 12, color: '#1677FF', letterSpacing: 1, marginBottom: 20 }}>
          ORCHISKY · 制造业数字化 · Est. 2014
        </div>
        <h1 style={{ fontSize: 56, fontWeight: 700, color: '#1A1A1A', lineHeight: 1.15, margin: 0, maxWidth: 900 }}>
          以咋询公司的严谨，<br />交付制造业可信赖的<br />数字化成果。
        </h1>
        <p style={{ fontFamily: 'Noto Serif SC, serif', fontSize: 17, color: '#555', maxWidth: 640, lineHeight: 1.7, marginTop: 28 }}>
          深耕长三角中大型制造业 11 年，为汽车零部件、半导体、生物医药客户交付计划、执行、追溯、质量一体化的软件解决方案。
        </p>
        <div style={{ marginTop: 40, display: 'flex', gap: 12 }}>
          <button onClick={onCTA} style={{ height: 40, padding: '0 22px', background: '#1677FF', color: '#fff', border: 0, borderRadius: 4, fontSize: 14, fontWeight: 500, cursor: 'pointer' }}>查看解决方案</button>
          <button style={{ height: 40, padding: '0 22px', background: '#fff', color: '#333', border: '1px solid #CCC', borderRadius: 4, fontSize: 14, fontWeight: 500, cursor: 'pointer' }}>下载行业白皮书 (PDF)</button>
        </div>
        <div style={{ marginTop: 64, display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', borderTop: '1px solid #E2E2E2', borderBottom: '1px solid #E2E2E2' }}>
          {[
            { k: '11', u: '年', l: '制造业深耕' },
            { k: '46', u: '家', l: '中大型客户' },
            { k: '98.2', u: '%', l: '试点车间良品率' },
            { k: '¥1.2', u: '亿', l: '累计交付价値' },
          ].map((x, i) => (
            <div key={i} style={{ padding: '24px 0', borderLeft: i ? '1px solid #E2E2E2' : 0 }}>
              <div style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 36, fontWeight: 700, color: '#1A1A1A', lineHeight: 1 }}>
                {x.k}<span style={{ fontSize: 16, color: '#888', marginLeft: 4, fontWeight: 500 }}>{x.u}</span>
              </div>
              <div style={{ fontSize: 13, color: '#555', marginTop: 8 }}>{x.l}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
window.Hero = Hero;
