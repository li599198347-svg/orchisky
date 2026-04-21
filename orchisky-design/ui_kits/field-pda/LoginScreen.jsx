function LoginScreen({ onLogin }) {
  const [user, setUser] = React.useState('E10284');
  const [pwd, setPwd] = React.useState('••••••');
  const [focus, setFocus] = React.useState('user');

  const F = (v) => {
    const base = {
      height: 40, borderRadius: 4, fontSize: 14, fontFamily: 'inherit',
      outline: 'none', background: '#fff', boxSizing: 'border-box', width: '100%',
      padding: '0 10px',
    };
    return v === focus
      ? { ...base, border: '1px solid #1070F0', boxShadow: '0 0 0 2px #6FA3F5' }
      : { ...base, border: '1px solid #CCC' };
  };

  return (
    <div style={{ display:'flex', flexDirection:'column', height:'100%', background:'#F5F5F5' }}>
      {/* status bar */}
      <div style={{ height:24, background:'#1A1A1A', display:'flex',
        alignItems:'center', justifyContent:'space-between', padding:'0 12px',
        color:'#fff', fontSize:12, fontFamily:'"Roboto Mono",monospace' }}>
        <span>09:12</span>
        <span>5G   87%</span>
      </div>

      {/* brand hero */}
      <div style={{ background:'#1070F0', padding:'32px 24px 24px', textAlign:'center' }}>
        <div style={{ color:'#fff', fontSize:22, fontWeight:700, letterSpacing:1 }}>Orchisky</div>
        <div style={{ color:'#A8C8F9', fontSize:12, marginTop:4 }}>兰之天现场端</div>
      </div>

      {/* form card */}
      <div style={{ margin:'24px 16px', background:'#fff', borderRadius:4,
        border:'1px solid #E2E2E2', padding:'24px 16px', display:'flex',
        flexDirection:'column', gap:16 }}>

        <div style={{ display:'flex', flexDirection:'column', gap:4 }}>
          <label style={{ fontSize:13, color:'#555' }}>工号</label>
          <input style={F('user')} value={user}
            onFocus={() => setFocus('user')} onChange={e => setUser(e.target.value)} />
        </div>

        <div style={{ display:'flex', flexDirection:'column', gap:4 }}>
          <label style={{ fontSize:13, color:'#555' }}>密码</label>
          <input type="password" style={F('pwd')} value={pwd}
            onFocus={() => setFocus('pwd')} onChange={e => setPwd(e.target.value)} />
        </div>

        <button
          onClick={() => onLogin && onLogin()}
          style={{ height:48, background:'#1070F0', color:'#fff', border:'none',
            borderRadius:4, fontSize:16, fontWeight:500, cursor:'pointer', marginTop:4 }}>
          登录
        </button>
      </div>

      <div style={{ textAlign:'center', fontSize:12, color:'#888', marginTop:4 }}>
        v2.3.1 · 兰之天软件
      </div>
    </div>
  );
}
export default LoginScreen;
