function CaseTable() {
  const rows = [
    { id: 'C-2025-018', client: '苏州某汽车轴承厂', industry: '汽车零部件', modules: 'MES · WMS · QMS', period: '2024-03 → 2024-11', result: '良品率 94.0% → 98.2%' },
    { id: 'C-2025-012', client: '无锡某半导体封测厂', industry: '半导体', modules: 'APS · MES', period: '2023-09 → 2024-06', result: '计划周期缩短 42%' },
    { id: 'C-2024-037', client: '常州某生物医药集团', industry: '生物医药', modules: 'WMS · QMS', period: '2023-01 → 2023-08', result: '库存准确率 99.6%' },
    { id: 'C-2024-021', client: '上海某精密机械企业', industry: '通用装备', modules: 'MES · 设备 OEE', period: '2022-11 → 2023-05', result: '设备 OEE 64% → 78%' },
  ];
  return (
    <section style={{ background: '#fff', padding: '80px 0' }}>
      <div style={{ maxWidth: 1200, margin: '0 auto', padding: '0 24px' }}>
        <div style={{ marginBottom: 32 }}>
          <div style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 12, color: '#1677FF', letterSpacing: 1, marginBottom: 8 }}>CASES · 46</div>
          <h2 style={{ margin: 0, fontSize: 36, fontWeight: 700, color: '#1A1A1A' }}>精选客户案例</h2>
        </div>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
          <thead>
            <tr>
              {['编号', '客户', '行业', '交付模块', '周期', '核心成果'].map(h => (
                <th key={h} style={{ background: '#1A1A1A', color: '#fff', textAlign: 'left', padding: '12px 14px', fontWeight: 600, fontSize: 12, borderBottom: '3px solid #1677FF' }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((r, i) => (
              <tr key={r.id} style={{ background: i % 2 ? '#FAFAFA' : '#fff' }}>
                <td style={{ padding: '14px', borderBottom: '0.5px solid #E2E2E2', fontFamily: 'Roboto Mono, monospace', color: '#1677FF', fontWeight: 500 }}>{r.id}</td>
                <td style={{ padding: '14px', borderBottom: '0.5px solid #E2E2E2', fontWeight: 500 }}>{r.client}</td>
                <td style={{ padding: '14px', borderBottom: '0.5px solid #E2E2E2', color: '#555' }}>{r.industry}</td>
                <td style={{ padding: '14px', borderBottom: '0.5px solid #E2E2E2', color: '#555' }}>{r.modules}</td>
                <td style={{ padding: '14px', borderBottom: '0.5px solid #E2E2E2', color: '#555', fontFamily: 'Roboto Mono, monospace' }}>{r.period}</td>
                <td style={{ padding: '14px', borderBottom: '0.5px solid #E2E2E2', color: '#2E6B3E', fontWeight: 500 }}>{r.result}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
window.CaseTable = CaseTable;
