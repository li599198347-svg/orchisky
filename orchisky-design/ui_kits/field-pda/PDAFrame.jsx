function PDAFrame({ title, onBack, children, bottomCTA }) {
  return (
    <div style={{ display:'flex', flexDirection:'column', height:'100%',
      background:'#FAFAFA', overflow:'hidden' }}>

      {/* StatusBar */}
      <div style={{ height:24, background:'#1A1A1A', display:'flex',
        alignItems:'center', justifyContent:'space-between', padding:'0 12px',
        color:'#fff', fontSize:12, fontFamily:'"Roboto Mono",monospace' }}>
        <span>09:42</span>
        <span>5G   Wi-Fi   87%</span>
      </div>

      {/* Topbar */}
      <div style={{ height:56, background:'#1070F0', display:'flex',
        alignItems:'center', padding:'0 12px', gap:8, flexShrink:0 }}>
        {onBack && (
          <button onClick={onBack} style={{ background:'none', border:'none',
            color:'#fff', fontSize:20, cursor:'pointer', width:40, height:40 }}>
            ←
          </button>
        )}
        <h1 style={{ color:'#fff', fontSize:18, fontWeight:500, margin:0, flex:1 }}>
          {title}
        </h1>
      </div>

      {/* Body */}
      <div style={{ flex:1, overflow:'auto' }}>{children}</div>

      {/* Bottom CTA */}
      {bottomCTA && (
        <div style={{ height:48, background:'#fff', borderTop:'1px solid #E2E2E2',
          display:'flex', alignItems:'center', justifyContent:'space-between',
          padding:'0 12px', gap:8, flexShrink:0 }}>
          {bottomCTA}
        </div>
      )}
    </div>
  );
}
export default PDAFrame;
