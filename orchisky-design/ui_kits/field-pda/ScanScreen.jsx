function ScanScreen({ onGo, onLogout }) {
  const tiles = [
    { id: 'receive', label: '入库扫码', icon: '↓', color: '#1070F0' },
    { id: 'putaway', label: '上架', icon: '⤒', color: '#1070F0' },
    { id: 'pick',    label: '拣货', icon: '⤓', color: '#1070F0' },
    { id: 'count',   label: '盘点', icon: '≡', color: '#1070F0' },
    { id: 'move',    label: '移库', icon: '⇄', color: '#1070F0' },
    { id: 'print',   label: '标签打印', icon: '□', color: '#1070F0' },
  ];

  return (
    <div style={{ display:'flex', flexDirection:'column', height:'100%', background:'#FAFAFA' }}>
      {/* StatusBar */}
      <div style={{ height:24, background:'#1A1A1A', color:'#fff', fontSize:12,
        fontFamily:'"Roboto Mono",monospace', display:'flex',
        justifyContent:'space-between', alignItems:'center', padding:'0 12px' }}>
        <span>09:42</span><span>5G 87%</span>
      </div>

      {/* AppBar */}
      <div style={{ height:56, background:'#1070F0', display:'flex', alignItems:'center',
        justifyContent:'space-between', padding:'0 12px', flexShrink:0 }}>
        <span style={{ color:'#fff', fontSize:18, fontWeight:500 }}>Orchisky WMS</span>
        <button onClick={onLogout} style={{ background:'none', border:'none',
          color:'#A8C8F9', fontSize:12, cursor:'pointer' }}>退出</button>
      </div>

      {/* User bar */}
      <div style={{ padding:'12px', background:'#EAF2FE', borderBottom:'1px solid #D0E1FC' }}>
        <div style={{ fontSize:14, color:'#074499', fontWeight:500 }}>王建国 · 仓管员</div>
        <div style={{ fontSize:12, color:'#555', marginTop:2 }}>1# 原料库 · 早班 08:00-16:00</div>
      </div>

      {/* Grid */}
      <div style={{ flex:1, padding:12, display:'grid',
        gridTemplateColumns:'repeat(3,1fr)', gap:8, overflow:'auto' }}>
        {tiles.map(t => (
          <button key={t.id} onClick={() => onGo && onGo(t.id)}
            style={{ background:'#fff', border:'1px solid #E2E2E2', borderRadius:4,
              padding:'16px 8px', display:'flex', flexDirection:'column',
              alignItems:'center', gap:8, cursor:'pointer', fontSize:14 }}>
            <span style={{ fontSize:28, color:t.color }}>{t.icon}</span>
            <span style={{ color:'#333' }}>{t.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
export default ScanScreen;
