from pathlib import Path
p=Path(__file__).with_name('index.html')
s=p.read_text(encoding='utf-8')
s=s.replace('认识教练','教练预约').replace("section('教练','coach','了解教练')","section('教练预约','coach','全部教练')")
start=s.index('<button class="card coach"',s.index('function home()'))
end=s.index("${section('会员卡推荐'",start)
s=s[:start]+'<div class="stack">${coachCards()}</div>'+s[end:]
start=s.index('const classes=()=>')
end=s.index('\nfunction schedule()',start)
s=s[:start]+'''const coaches=[
 {id:0,name:'林教练',courses:['基础小班课','专注力进阶课'],types:['小班课','精品课']},
 {id:1,name:'陈教练',courses:['一对一基础训练','一对一进阶训练'],types:['私教课']},
 {id:2,name:'周教练',courses:['基础小班课','一对一基础训练'],types:['小班课','私教课']}
];
// Demo of published backend records: the member can only select these slots.
const publishedClasses=[
 {id:0,type:'小班课',title:'基础小班课',time:'10:00',end:'11:00',left:3,cap:6,coachId:0,coach:'林教练',level:'入门',days:[18,19,20,21,22,23]},
 {id:1,type:'私教课',title:'一对一基础训练',time:'14:00',end:'15:00',left:1,cap:1,coachId:1,coach:'陈教练',level:'入门',days:[18,19,21,23]},
 {id:2,type:'精品课',title:'专注力进阶课',time:'16:00',end:'17:30',left:0,cap:4,coachId:0,coach:'林教练',level:'进阶',days:[18,19,20,21,22,23]},
 {id:3,type:'私教课',title:'一对一进阶训练',time:'19:00',end:'20:00',left:1,cap:1,coachId:1,coach:'陈教练',level:'进阶',days:[18,20,22]},
 {id:4,type:'私教课',title:'一对一基础训练',time:'15:30',end:'16:30',left:1,cap:1,coachId:2,coach:'周教练',level:'入门',days:[18,19,20,22,23]},
 {id:5,type:'小班课',title:'基础小班课',time:'11:30',end:'12:30',left:2,cap:6,coachId:2,coach:'周教练',level:'入门',days:[18,19,21,23]}
];
const classes=()=>publishedClasses.filter(c=>c.days.includes(day)).sort((a,b)=>a.time.localeCompare(b.time));
let selectedCoach=0;
function coachCards(){return coaches.map(c=>`<button class="card coach" style="width:100%;text-align:left" data-action="coachslots" data-id="${c.id}"><div class="avatar">${icon('user')}</div><div class="grow"><h3>${c.name}</h3><div style="margin:8px 0">${c.types.map(t=>`<span class="tag">${t}</span>`).join(' ')}</div><p class="small muted">${c.courses.join(' · ')}</p></div>${icon('chevron')}</button>`).join('')}
function coachList(){openSheet(`<h2>教练预约</h2><p class="muted small" style="margin-bottom:16px">${stores[store]} · ${coaches.length}位教练</p><div class="stack">${coachCards()}</div>`)}
function coachSlots(id){selectedCoach=id;const c=coaches[id],slots=classes().filter(x=>x.coachId===id);openSheet(`<button class="small" style="min-height:44px" data-action="coach">‹ 全部教练</button><div class="row"><div class="avatar">${icon('user')}</div><div><h2 style="margin:0">${c.name}</h2><span class="small muted">${stores[store]}</span></div></div><div class="summary"><h3>可授课程</h3><p class="small muted" style="margin-top:8px">${c.courses.join(' · ')}</p></div><h3>选择上课日期</h3><div class="chips">${[18,19,20,21,22,23,24].map(d=>`<button class="chip ${day===d?'active':''}" data-action="coachday" data-id="${d}">9月${d}日</button>`).join('')}</div><div class="row between"><h3>可约课程与时段</h3><span class="small muted">${slots.length}个时段</span></div>${slots.length?slots.map(x=>{const taken=bookings.some(b=>b.id===x.id&&b.day===day&&b.store===store);return `<div class="summary"><div class="row between"><strong>${x.time} — ${x.end}</strong><span class="tag">${x.type}</span></div><h3 style="margin:8px 0">${x.title}</h3><div class="row between"><span class="small muted">${taken?'已预约':x.left?'剩余'+x.left+'个名额':'已约满'} · ${x.type}卡1次</span><button class="btn" style="min-height:44px;padding:8px 12px" data-action="book" data-id="${x.id}" ${taken||!x.left?'disabled':''}>${taken?'已预约':x.left?'预约':'已约满'}</button></div></div>`}).join(''):'<div class="empty">暂无可约时段，请选择其他日期。</div>'}`)}
''' + s[end:]
s=s.replace("classType='全部',day=11","classType='全部',day=18")
s=s.replace('[11,12,13,14,15,16,17]','[18,19,20,21,22,23,24]').replace('day===17','day===24')
s=s.replace('9月11日至17日','9月18日至24日').replace('2026-09-11','2026-09-18').replace('2026-09-17','2026-09-24')
s=s.replace('const c=classes()[id];activeClass',"const c=classes().find(c=>c.id===id);if(!c||!c.left||bookings.some(b=>b.id===id&&b.day===day&&b.store===store)){toast('该时段不可预约，请重新选择');return;}activeClass")
start=s.index("case 'coach':")
end=s.index("case 'rules':",start)
s=s[:start]+"case 'coach':coachList();break;case 'coachslots':coachSlots(i);break;case 'coachday':day=i;render();coachSlots(selectedCoach);break;\n"+s[end:]
s=s.replace("case 'confirmbook':{const w=", "case 'confirmbook':{if(bookings.some(b=>b.id===activeClass.id&&b.day===activeClass.day&&b.store===activeClass.store)){toast('你已预约该时段');break;}const w=")
s=s.replace('${stores[b.store]} · ${b.type}卡占用1次','${stores[b.store]} · ${b.coach} · ${b.type}卡占用1次')
s=s.replace('${activeClass.title} · ${stores[activeClass.store]}','${activeClass.title} · ${activeClass.coach}<br>${stores[activeClass.store]}')
p.write_text(s,encoding='utf-8')
