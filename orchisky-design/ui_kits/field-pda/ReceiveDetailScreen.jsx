function ReceiveDetailScreen({ order, onBack, onSubmit }) {
  const [qty, setQty] = React.useState(order?.expected ?? 200);
  const [lot, setLot] = React.useState('LOT-20260420-01');
  const [focus, setFocus] = React.useState(null);

  const inp = (k) => ({
    height: 40, borderRadius: 4, fontSize: 14, fontFamily: 'inherit',
    padding: '0 10px', outline: 'none', width: '100%', boxSizing: 'border-box',
    background: '#fff',
    border: focus === k ? '1px solid #1070F0' : '1px solid #CCC',
    boxShadow: focus === k ? '0 0 0 2px #6FA3F5' : 'none',
  });

  return (
    <div style={{ display:'flex', flexDirection:'column', height:'100%', background:'#FAFAFA' }}>
      {/* StatusBar */}
      <div style={{ height:24, background:'#1A1A1A', color:'#fff', fontSize:12,
        fontFamily:'"Roboto Mono",monospace', display:'flex',
        justifyContent:'space-between', alignItems:'center', padding:'0 12px' }}>
        <span>09:44</span><span>5G 87%</span>
      </div>

      {/* Topbar */}
      <div style={{ height:56, background:'#1070F0', display:'flex',
        alignItems:'center', padding:'0 12px', gap:8, flexShrink:0 }}>
        <button onClick={onBack} style={{ background:'none', border:'none',
          color:'#fff', fontSize:20, cursor:'pointer', width:40, height:40 }}>←</button>
        <h1 style={{ color:'#fff', fontSize:18, fontWeight:500, margin:0 }}>入库明细录入</h1>
      </div>

      {/* Body */}
      <div style={{ flex:1, overflow:'auto', padding:'12px 12px 0' }}>

        {/* order header */}
        <div style={{ background:'#fff', border:'1px solid #E2E2E2', borderRadius:4,
          padding:'12px', marginBottom:12 }}>
          <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center' }}>
            <span style={{ fontSize:16, fontWeight:500, fontFamily:'"Roboto Mono",monospace' }}>
              {order?.id ?? 'RK-20260420-0038'}
            </span>
            <span style={{ background:'#EAF2FE', color:'#0A5AC8', fontSize:12,
              borderRadius:2, padding:'2px 8px' }}>进行中</span>
          </div>
          <div style={{ fontSize:12, color:'#888', marginTop:6 }}>
            应到：<span style={{ fontFamily:'"Roboto Mono",monospace' }}>{order?.expected ?? 200}</span> pcs · 华瑞机电
          </div>
        </div>

        {/* fields */}
        <div style={{ display:'flex', flexDirection:'column', gap:12 }}>
          <div style={{ display:'flex', flexDirection:'column', gap:4 }}>
            <label style={{ fontSize:13, color:'#555' }}>批号 <span style={{color:'#B01C1C'}}>*</span></label>
            <input style={inp('lot')} value={lot}
              onFocus={() => setFocus('lot')} onChange={e => setLot(e.target.value)} />
          </div>

          <div style={{ display:'flex', flexDirection:'column', gap:4 }}>
            <label style={{ fontSize:13, color:'#555' }}>实到数量 <span style={{color:'#B01C1C'}}>*</span></label>
            <div style={{ display:'flex', gap:8, alignItems:'center' }}>
              <button onClick={() => setQty(q => Math.max(0, q-1))}
                style={{ width:40, height:40, borderRadius:4, border:'1px solid #CCC',
                  background:'#fff', fontSize:18, cursor:'pointer' }}>-</button>
              <input style={{ ...inp('qty'), flex:1, textAlign:'center',
                fontFamily:'"Roboto Mono",monospace', fontSize:18, fontWeight:500 }}
                value={qty} onFocus={() => setFocus('qty')}
                onChange={e => setQty(Number(e.target.value) || 0)} />
              <button onClick={() => setQty(q => q+1)}
                style={{ width:40, height:40, borderRadius:4, border:'1px solid #CCC',
                  background:'#fff', fontSize:18, cursor:'pointer' }}>+</button>
            </div>
            <span style={{ fontSize:12, color:'#888' }}>单位 pcs · 预期 {order?.expected ?? 200}</span>
          </div>
        </div>
      </div>

      {/* Bottom CTA */}
      <div style={{ height:48, background:'#fff', borderTop:'1px solid #E2E2E2',
        display:'flex', alignItems:'center', gap:8, padding:'0 12px', flexShrink:0 }}>
        <button onClick={onBack}
          style={{ flex:1, height:38, border:'1px solid #CCC', borderRadius:4,
            background:'#fff', fontSize:14, cursor:'pointer', color:'#333' }}>
          取消
        </button>
        <button onClick={onSubmit}
          style={{ flex:2, height:38, background:'#1A7A42', color:'#fff',
            border:'none', borderRadius:4, fontSize:14, fontWeight:500, cursor:'pointer' }}>
          ✓ 确认入库
        </button>
      </div>
    </div>
  );
}
export default ReceiveDetailScreen;
