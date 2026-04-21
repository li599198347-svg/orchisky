function OrderDetail({ onClose }) {
  return (
    <div style={{ padding: 24 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13, color: 'rgba(0,0,0,0.45)', marginBottom: 12 }}>
        <a onClick={onClose} style={{ color: '#1677FF', cursor: 'pointer' }}>工单管理</a>
        <span>/</span>
        <span>工单详情</span>
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <div>
          <h2 style={{ margin: 0, fontSize: 20, fontWeight: 600, color: 'rgba(0,0,0,0.88)', display: 'flex', alignItems: 'center', gap: 12 }}>
            <span style={{ fontFamily: 'Roboto Mono, monospace' }}>WO-20260420-0037</span>
            <StatusTag status="在产" />
          </h2>
          <div style={{ fontSize: 13, color: 'rgba(0,0,0,0.45)', marginTop: 6, fontFamily: 'Roboto Mono, monospace' }}>创建 2026-04-19 10:20 · 最近更新 2026-04-20 14:02</div>
        </div>
        <div style={{ display: 'flex', gap: 8 }}>
          <button onClick={onClose} style={{ height: 32, padding: '0 16px', background: '#fff', border: '1px solid #D9D9D9', borderRadius: 6, fontSize: 14, cursor: 'pointer' }}>返回</button>
          <button style={{ height: 32, padding: '0 16px', background: '#334155', color: '#fff', border: 0, borderRadius: 6, fontSize: 14, fontWeight: 500, cursor: 'pointer' }}>编辑</button>
        </div>
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: 16 }}>
        <div style={{ background: '#fff', border: '1px solid #F0F0F0', borderRadius: 8, padding: 24 }}>
          <h3 style={{ margin: '0 0 16px', fontSize: 15, fontWeight: 600, paddingBottom: 12, borderBottom: '1px solid #F0F0F0' }}>基本信息</h3>
          <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr 120px 1fr', rowGap: 14, columnGap: 16, fontSize: 14 }}>
            {[['产品', '齿轮筱外壳'], ['产品编码', 'P-GB-2024-07'], ['计划数量', '450 件'], ['已完工', '210 件'], ['计划开工', '2026-04-20 08:00'], ['计划完工', '2026-04-23 12:00'], ['车间', '装配二车间'], ['负责人', '王组长']].map(([k, v], i) => (
              <React.Fragment key={i}>
                <span style={{ color: 'rgba(0,0,0,0.45)' }}>{k}</span>
                <span style={{ color: 'rgba(0,0,0,0.88)', fontFamily: ['产品编码', '计划开工', '计划完工'].includes(k) || v.includes('件') ? 'Roboto Mono, monospace' : undefined }}>{v}</span>
              </React.Fragment>
            ))}
          </div>
          <h3 style={{ margin: '24px 0 16px', fontSize: 15, fontWeight: 600, paddingBottom: 12, borderBottom: '1px solid #F0F0F0' }}>物料清单 (BOM)</h3>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
            <thead><tr>{['物料编码', '名称', '需求', '已领', '单位'].map(h => <th key={h} style={{ textAlign: 'left', padding: '8px 12px', background: '#FAFAFA', fontWeight: 600, borderBottom: '1px solid #F0F0F0' }}>{h}</th>)}</tr></thead>
            <tbody>{[['M-STL-A01', '合金钟棒材 45#', '450', '450', 'kg'], ['M-GSK-004', '密封庞圈', '900', '900', '件'], ['M-BLT-M12', '内六角螺栓 M12', '1,800', '1,200', '件']].map((r, i) => (
              <tr key={i}>{r.map((c, j) => <td key={j} style={{ padding: '10px 12px', borderBottom: '1px solid #F0F0F0', fontFamily: j === 0 || j === 2 || j === 3 ? 'Roboto Mono, monospace' : undefined }}>{c}</td>)}</tr>
            ))}</tbody>
          </table>
        </div>
        <div style={{ background: '#fff', border: '1px solid #F0F0F0', borderRadius: 8, padding: 24 }}>
          <h3 style={{ margin: '0 0 16px', fontSize: 15, fontWeight: 600, paddingBottom: 12, borderBottom: '1px solid #F0F0F0' }}>操作日志</h3>
          {[
            { t: '14:02', who: '王组长', act: '报工 +30 件' },
            { t: '11:40', who: '王组长', act: '报工 +80 件' },
            { t: '09:15', who: '系统', act: '工序 OP20 切换至 OP30' },
            { t: '08:03', who: '王组长', act: '开工确认' },
            { t: '昨 17:20', who: '李主管', act: '审核通过' },
          ].map((l, i) => (
            <div key={i} style={{ display: 'flex', gap: 12, paddingBottom: 12, marginBottom: 12, borderBottom: i < 4 ? '1px dashed #F0F0F0' : 0 }}>
              <span style={{ fontFamily: 'Roboto Mono, monospace', fontSize: 12, color: 'rgba(0,0,0,0.45)', minWidth: 52 }}>{l.t}</span>
              <div style={{ fontSize: 13 }}>
                <div style={{ color: 'rgba(0,0,0,0.88)' }}>{l.act}</div>
                <div style={{ color: 'rgba(0,0,0,0.45)', fontSize: 12, marginTop: 2 }}>{l.who}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
window.OrderDetail = OrderDetail;
