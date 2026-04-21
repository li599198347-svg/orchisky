function ReceiveScreen({ onOpen, onBack }) {
  const orders = [
    { id: 'RK-20260420-0038', vendor: '华瑞机电', expected: 200, status: '进行中', statusKey: 'info' },
    { id: 'RK-20260420-0039', vendor: '东方重工', expected: 480, status: '待开始', statusKey: 'neutral' },
    { id: 'RK-20260420-0040', vendor: '嘉华电子', expected: 120, status: '待开始', statusKey: 'neutral' },
  ];

  const CHIP = {
    info:    { bg:'#EAF2FE', color:'#0A5AC8' },
    neutral: { bg:'#F5F5F5', color:'#555' },
    success: { bg:'#EAF5EF', color:'#1A7A42' },
  };

  return (
    <div style={{ display:'flex', flexDirection:'column', height:'100%', background:'#FAFAFA' }}>
      <div style={{ height:24, background:'#1A1A1A', color:'#fff', fontSize:12,
        fontFamily:'"Roboto Mono",monospace', display:'flex',
        justifyContent:'space-between', alignItems:'center', padding:'0 12px' }}>
        <span>09:43</span><span>5G 87%</span>
      </div>
      <div style={{ height:56, background:'#1070F0', display:'flex', alignItems:'center',
        padding:'0 12px', gap:8, flexShrink:0 }}>
        <button onClick={onBack} style={{ background:'none', border:'none',
          color:'#fff', fontSize:20, cursor:'pointer', width:40, height:40 }}>←</button>
        <h1 style={{ color:'#fff', fontSize:18, fontWeight:500, margin:0 }}>入库单列表</h1>
      </div>

      <div style={{ flex:1, overflow:'auto', padding:'0 12px' }}>
        <div style={{ marginTop:12, marginBottom:8, fontSize:12, color:'#888' }}>
          待处理 <span style={{ fontFamily:'"Roboto Mono",monospace' }}>{orders.length}</span> 单
        </div>
        {orders.map(o => (
          <div key={o.id}
            onClick={() => onOpen && onOpen(o)}
            style={{ background:'#fff', border:'1px solid #E2E2E2', borderRadius:4,
              padding:'12px', marginBottom:8, cursor:'pointer' }}>
            <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
              <span style={{ fontSize:16, fontWeight:500,
                fontFamily:'"Roboto Mono",monospace' }}>{o.id}</span>
              <span style={{ ...CHIP[o.statusKey], fontSize:12,
                borderRadius:2, padding:'2px 8px' }}>{o.status}</span>
            </div>
            <div style={{ fontSize:12, color:'#888', marginTop:6, display:'flex', gap:16 }}>
              <span>供应商：{o.vendor}</span>
              <span>应到：<span style={{ fontFamily:'"Roboto Mono",monospace' }}>{o.expected}</span> pcs</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
export default ReceiveScreen;
