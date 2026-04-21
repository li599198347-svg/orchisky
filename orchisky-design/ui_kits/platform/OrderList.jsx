function OrderList({ onOpen }) {
  const [query, setQuery] = React.useState('');
  const all = [
    { id: 'WO-20260420-0038', product: '主轴轴承 A 型', qty: '1,280', due: '2026-04-22 18:00', owner: '李主管', status: '已完成' },
    { id: 'WO-20260420-0037', product: '齿轮筱外壳', qty: '450', due: '2026-04-23 12:00', owner: '王组长', status: '在产' },
    { id: 'WO-20260420-0036', product: '液压阀芯', qty: '2,100', due: '2026-04-25 09:00', owner: '王组长', status: '缺料' },
    { id: 'WO-20260420-0035', product: '电机定子', qty: '680', due: '2026-04-26 18:00', owner: '陈班长', status: '在产' },
    { id: 'WO-20260420-0034', product: '铸铁底座', qty: '320', due: '2026-04-26 18:00', owner: '陈班长', status: '已驳回' },
    { id: 'WO-20260420-0033', product: '精密齿轮', qty: '1,540', due: '2026-04-28 08:00', owner: '李主管', status: '待审核' },
  ].filter(r => !query || r.id.includes(query) || r.product.includes(query));
  return (
    <div style={{ padding: 24 }}>
      <h2 style={{ margin: '0 0 20px', fontSize: 20, fontWeight: 600, color: 'rgba(0,0,0,0.88)' }}>工单管理</h2>
      <div style={{ background: '#fff', border: '1px solid #F0F0F0', borderRadius: 8 }}>
        <div style={{ padding: 16, display: 'flex', gap: 12, alignItems: 'center', borderBottom: '1px solid #F0F0F0' }}>
          <input value={query} onChange={e => setQuery(e.target.value)} placeholder="搜索工单号 / 产品名称" style={{ flex: 1, height: 32, padding: '0 12px', border: '1px solid #D9D9D9', borderRadius: 6, fontSize: 14, outline: 'none', fontFamily: 'inherit' }} />
          <button style={{ height: 32, padding: '0 16px', background: '#fff', border: '1px solid #D9D9D9', borderRadius: 6, fontSize: 14, cursor: 'pointer' }}>筛选</button>
          <button style={{ height: 32, padding: '0 16px', background: '#334155', color: '#fff', border: 0, borderRadius: 6, fontSize: 14, fontWeight: 500, cursor: 'pointer' }}>+ 新建工单</button>
        </div>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 14 }}>
          <thead>
            <tr>
              {['工单号', '产品', '数量', '计划完工', '负责人', '状态', '操作'].map(h => (
                <th key={h} style={{ textAlign: 'left', padding: '12px 16px', background: '#FAFAFA', fontWeight: 600, fontSize: 13, borderBottom: '1px solid #F0F0F0' }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {all.map(r => (
              <tr key={r.id}>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0', fontFamily: 'Roboto Mono, monospace', color: '#1677FF', cursor: 'pointer' }} onClick={() => onOpen('detail')}>{r.id}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}>{r.product}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0', fontFamily: 'Roboto Mono, monospace' }}>{r.qty}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0', fontFamily: 'Roboto Mono, monospace', whiteSpace: 'nowrap' }}>{r.due}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}>{r.owner}</td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}><StatusTag status={r.status} /></td>
                <td style={{ padding: '12px 16px', borderBottom: '1px solid #F0F0F0' }}>
                  <a onClick={() => onOpen('detail')} style={{ color: '#1677FF', fontSize: 13, cursor: 'pointer', marginRight: 12 }}>详情</a>
                  <a style={{ color: '#1677FF', fontSize: 13, cursor: 'pointer' }}>编辑</a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <div style={{ padding: 12, display: 'flex', justifyContent: 'flex-end', alignItems: 'center', gap: 8, fontSize: 13, color: 'rgba(0,0,0,0.65)' }}>
          共 <span style={{ color: 'rgba(0,0,0,0.88)', fontFamily: 'Roboto Mono, monospace' }}>{all.length}</span> 条
          <button style={{ width: 32, height: 32, border: '1px solid #D9D9D9', background: '#fff', borderRadius: 6, cursor: 'pointer' }}>‹</button>
          <span style={{ width: 32, height: 32, lineHeight: '32px', textAlign: 'center', background: '#334155', color: '#fff', borderRadius: 6 }}>1</span>
          <button style={{ width: 32, height: 32, border: '1px solid #D9D9D9', background: '#fff', borderRadius: 6, cursor: 'pointer' }}>›</button>
        </div>
      </div>
    </div>
  );
}
window.OrderList = OrderList;
