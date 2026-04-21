function SolutionGrid() {
  const items = [
    { code: '01', title: '生产计划与排程', desc: '从预测到工单、从主计划到工序计划，覆盖 8 个执行模块。', stat: '平均缩短计划周期 42%' },
    { code: '02', title: '车间执行 MES', desc: '工单、报工、检验、追溯、设备 OEE 一体化，支持 PDA / Pad 现场采集。', stat: '试点车间良品率 +4.2pp' },
    { code: '03', title: '物料与仓储 WMS', desc: '收货、上架、拣选、盘点、配送全流程扫码；支持多仓多货主。', stat: '库存准确率 99.6%' },
    { code: '04', title: '质量与追溯 QMS', desc: 'IPQC / OQC / 客诉 / 8D 闭环；批次-工单-操作员-设备四维追溯。', stat: '客诉响应时间 -58%' },
  ];
  return (
    <section style={{ background: '#FAFAFA', padding: '80px 0', borderBottom: '1px solid #E2E2E2' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '0 24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 40, borderBottom: '1px solid #E2E2E2', paddingBottom: 24 }}>
          <div>
            <div style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 12, color: '#1677FF', letterSpacing: 1, marginBottom: 8 }}>SOLUTIONS · 04</div>
            <h2 style={{ margin: 0, fontSize: 36, fontWeight: 700, color: '#1A1A1A' }}>四大解决方案</h2>
          </div>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 1, background: '#E2E2E2', border: '1px solid #E2E2E2' }}>
          {items.map(it => (
            <div key={it.code} style={{ background: '#fff', padding: 28, cursor: 'pointer' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 16 }}>
                <span style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 11, color: '#888', letterSpacing: 1 }}>{it.code}</span>
                <span style={{ fontSize: 12, color: '#1677FF', fontWeight: 500 }}>→</span>
              </div>
              <h3 style={{ margin: 0, fontSize: 22, fontWeight: 700, color: '#1A1A1A' }}>{it.title}</h3>
              <p style={{ fontSize: 14, color: '#555', lineHeight: 1.7, marginTop: 12, marginBottom: 20 }}>{it.desc}</p>
              <div style={{ display: 'inline-block', padding: '4px 10px', background: '#E6F4FF', color: '#0958D9', fontSize: 12, fontWeight: 500, fontFamily: 'Roboto Mono, monospace', borderRadius: 2 }}>{it.stat}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
window.SolutionGrid = SolutionGrid;
