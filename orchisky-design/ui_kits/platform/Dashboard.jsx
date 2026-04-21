const STATUS = {
  '已完成': { sym: '✓', tone: 'solid' },
  '合格':   { sym: '✓', tone: 'solid' },
  '在产':   { sym: '→', tone: 'outline' },
  '进行中': { sym: '→', tone: 'outline' },
  '缺料':   { sym: '!', tone: 'outline' },
  '待审核': { sym: '?', tone: 'outline' },
  '已驳回': { sym: '×', tone: 'outline' },
  '异常':   { sym: '×', tone: 'outline' },
};
window.STATUS = STATUS;

function StatusTag({ status }) {
  const s = STATUS[status] || { sym: '•', tone: 'outline' };
  const solid = s.tone === 'solid';
  return (
    <span style={{
      display:'inline-flex', alignItems:'stretch', height:22, fontSize:11, fontWeight:500,
      border:'1px solid #D9D9D9', borderRadius:2, background:'#fff', color:'#1A1A1A',
      minWidth:76, lineHeight:'20px', boxSizing:'border-box', verticalAlign:'middle'
    }}>
      <span style={{
        width:20, flex:'0 0 20px', display:'inline-flex', alignItems:'center', justifyContent:'center',
        fontFamily:'Roboto Mono, monospace', fontSize:11, fontWeight:700,
        background: solid ? '#1A1A1A' : '#fff',
        color:     solid ? '#fff'   : '#64748B',
        borderRight:'1px solid #D9D9D9'
      }}>{s.sym}</span>
      <span style={{ padding:'0 8px', flex:'1', textAlign:'left' }}>{status}</span>
    </span>
  );
}
window.StatusTag = StatusTag;

function Dashboard({ onOpen }) {
  const kpis = [
    { label: '今日工单', value: '142', delta: '+8' },
    { label: '已完工', value: '26', delta: '达成率 87.2%' },
    { label: '缺料', value: '12', delta: '待补 4h' },
    { label: '异常停机', value: '3', delta: 'CNC-02-05 等' },
  ];
  const recent = [
    { id: 'WO-20260420-0038', product: '主轴轴承 A 型', qty: '1,280', status: '已完成' },
    { id: 'WO-20260420-0037', product: '齿轮筱外壳', qty: '450', status: '在产' },
    { id: 'WO-20260420-0036', product: '液压阀芯', qty: '2,100', status: '缺料' },
    { id: 'WO-20260420-0035', product: '电机定子', qty: '680', status: '在产' },
    { id: 'WO-20260420-0034', product: '铸铁底座', qty: '320', status: '已驳回' },
  ];
  return (
    <div style={{ padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <h2 style={{ margin: 0, fontSize: 20, fontWeight: 600, color: 'rgba(0,0,0,0.88)' }}>数据总览</h2>
        <div style={{ fontSize: 13, color: 'rgba(0,0,0,0.45)', fontFamily: 'Roboto Mono, monospace' }}>2026-04-20 14:08 · 自动刷新</div>
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4,1fr)', gap: 16, marginBottom: 24 }}>
        {kpis.map(k => (
          <div key={k.label} style={{ background: '#fff', border: '1px solid #F0F0F0', borderRadius: 8, padding: 20 }}>
            <div style={{ fontSize: 14, color: 'rgba(0,0,0,0.65)', marginBottom: 8 }}>{k.label}</div>
            <div style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 28, fontWeight: 600, color: '#1A1A1A', lineHeight: 1 }}>{k.value}</div>
            <div style={{ fontSize: 12, color: 'rgba(0,0,0,0.45)', marginTop: 8 }}>{k.delta}</div>
          </div>
        ))}
      </div>
      <div style={{ background: '#fff', border: '1px solid #F0F0F0', borderRadius: 8, padding: 20 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
          <h3 style={{ margin: 0, fontSize: 16, fontWeight: 600 }}>近期工单</h3>
          <a onClick={() => onOpen('orders')} style={{ fontSize: 13, color: '#1677FF', cursor: 'pointer' }}>查看全部 →</a>
        </div>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
          <thead>
            <tr>
              {['工单号', '产品', '数量', '状态', '操作'].map(h => (
                <th key={h} style={{ textAlign: 'left', padding: '12px 16px', background: '#FAFAFA', fontWeight: 600, fontSize: 13, borderTop: '1px solid #F0F0F0', borderBottom: '1px solid #F0F0F0' }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {recent.map(r => (
              <tr key={r.id}>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0', fontFamily: 'Roboto Mono, monospace', color: '#1677FF', cursor: 'pointer' }} onClick={() => onOpen('detail')}>{r.id}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}>{r.product}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0', fontFamily: 'Roboto Mono, monospace' }}>{r.qty}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}><StatusTag status={r.status} /></td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}>
                  <a onClick={() => onOpen('detail')} style={{ color: '#1677FF', fontSize: 13, cursor: 'pointer', marginRight: 12 }}>详情</a>
                  <a style={{ color: '#1677FF', fontSize: 13, cursor: 'pointer' }}>追溯</a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
window.Dashboard = Dashboard;
