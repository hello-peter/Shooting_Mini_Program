from pathlib import Path
import re
p=Path(__file__).with_name('index.html')
s=p.read_text(encoding='utf8').replace('准星','XX')
# Remove presentation panels. Keep the product itself as the deliverable.
s=re.sub(r'<aside class="sidebar">.*?</aside>','',s,flags=re.S)
s=re.sub(r'<aside class="note-panel">.*?</aside>','',s,flags=re.S)
s=s.replace("$('#sideNav').innerHTML=navs.map", "if($('#sideNav'))$('#sideNav').innerHTML=navs.map")
s=s.replace("$('#'+id).textContent=note[i]","$('#'+id)&&($('#'+id).textContent=note[i])")
s=s.replace("$('#brand').innerHTML=icon('target')+'XX';",'')
s=s.replace('<div class="hero"><div class="art">${targetArt}</div><span class="tag dark">成人射击训练 · 新的开始</span><h1>稳住节奏<br>让专注发生。</h1><p class="sub">从第一堂课开始，找到自己的进步。</p><button class="btn lime" data-action="nav" data-id="2">预约下一堂课 ${icon(\'arrow\')}</button></div>', '<div class="hero dashboard"><div class="art">${targetArt}</div><div class="row between"><h3>我的训练</h3><span class="tag dark">会员</span></div><div class="row" style="gap:32px;margin:20px 0"><div><div class="price">${wallet.reduce((s,w)=>s+w.left,0)}<small> 次</small></div><span class="small sub">可用课次</span></div><div><div class="price">${bookings.length+1}<small> 节</small></div><span class="small sub">待上课程</span></div></div><button class="btn lime" data-action="nav" data-id="2">立即预约 ${icon(\'arrow\')}</button></div>')
s=s.replace('<div class="pageintro"><div class="overline">YOUR TRAINING PLAN</div><h1>把进步，安排进日常</h1><p class="muted">选择适合你的课型与训练次数</p></div>','<div class="pageintro"><h1>会员卡</h1></div>')
s=s.replace('<div class="pageintro"><div class="overline">MAKE TIME FOR YOURSELF</div><h1>为自己，留一堂课</h1></div>','<div class="pageintro"><h1>预约课程</h1></div>')
s=s.replace('<div class="overline">GEAR UP</div><h1>为热爱，备齐所需</h1>','<h1>商城</h1>')
s=s.replace('<p class="muted small">保持专注，进步自有回响。</p>','<p class="muted small">138 **** 0000</p>')
s=s.replace('<p class="small muted center" style="margin-top:20px">每一次专注，都是向前一步。</p>','')
s=s.replace('<p class="prototype center">XX · 让热爱成为习惯</p>','')
for a,b in [('和专业教练一起进步','教练'),('选择你的训练计划','会员卡推荐'),('一起开始，更有动力','拼团'),('循序渐进，找到适合你的训练节奏','小班课 · 精品课'),('把进步，安排进日常','会员卡'),('确认你的训练计划','确认购卡'),('训练计划，准备好了','购卡成功'),('已为你留好位置','预约成功'),('好装备，正在准备中','支付成功'),('与你好友，一起开始','拼团'),('与好友，一起开始','拼团'),('还差一位同行者','开团成功'),('这一天，留一点自由','暂无排课'),('你的训练装备清单','购物车'),('熟悉的专业，在你身边。',''),('认识你的教练','教练详情'),('适合规律训练的你','按课型扣次')]:s=s.replace(a,b)
s=s.replace('<div class="row between"><span class="overline">${i?\'PROGRESS\':\'STARTER\'} / ${cardType}</span>','<div class="row between"><span>${cardType}专属</span>')
css='''
/* Product-only layout and prominent central booking action. */
.shell{display:flex;justify-content:center;max-width:none;padding:24px;gap:0}
.phone{height:min(900px,calc(100dvh - 48px));min-height:640px}
.tabbar{height:88px;overflow:visible;position:relative;padding-top:12px;align-items:flex-start}
.tabbar button{min-height:56px;position:relative;z-index:2}
.tabbar button:nth-child(3){transform:translateY(-30px);min-width:76px;gap:8px;color:var(--ink);font-weight:600}
.tabbar button:nth-child(3) svg,.tabbar button:nth-child(3).active svg{width:68px;height:68px;padding:20px;border-radius:50%;background:var(--lime);box-shadow:0 0 0 7px var(--paper),0 8px 20px #193d2825;stroke-width:1.9}
.tabbar button:nth-child(3).active svg{background:var(--ink);color:var(--lime)}
.scroll{padding-bottom:44px}.hero.dashboard{min-height:208px}.hero.dashboard .art{opacity:.22;right:-40px;top:16px}.hero.dashboard .btn{margin:0;padding:8px 16px}.pageintro{margin:12px 0 20px}.pageintro h1{font-size:24px}
@media(max-width:720px){.shell{padding:0}.phone{height:100dvh;min-height:0;max-width:480px}.tabbar{height:88px;padding-bottom:12px}.homebar{display:none}}
'''
s=s.replace('</style>',css+'</style>')
p.write_text(s,encoding='utf8')
