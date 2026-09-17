from pathlib import Path
p=Path(__file__).with_name('index.html')
s=p.read_text(encoding='utf-8')
s=s.replace('${coachCards()}</div>${section(\'会员卡推荐\'', '${coachCards(coaches.slice(0,2))}</div>${section(\'会员卡推荐\'')
s=s.replace('let selectedCoach=0;', "let selectedCoach=null,bookingMode='course',coachQuery='',coachType='全部',coachLimit=6;")
s=s.replace('function coachCards(){return coaches.map', 'function coachCards(list=coaches){return list.map')
s=s.replace("${icon('chevron')}</button>`).join('')}\nfunction coachList", "<span class=\"small\">查看时段 ›</span></button>`).join('')}\nfunction coachList")
start=s.index('function coachList()')
end=s.index('function coachSlots(id)',start)
s=s[:start]+'''function coachList(){closeSheet();page=2;bookingMode='coach';selectedCoach=null;render(true)}
function coachSlots(id){closeSheet();page=2;bookingMode='coach';selectedCoach=id;render(true)}
function coachDirectory(){const list=coaches.filter(c=>c.name.includes(coachQuery.trim())&&(coachType==='全部'||c.types.includes(coachType)));return `<div class="search">${icon('search')}<input id="coachSearch" aria-label="搜索教练姓名" placeholder="搜索教练姓名" value="${escapeHTML(coachQuery)}"><button class="iconbtn" data-action="clearcoach" aria-label="清空教练搜索">×</button></div><div class="chips">${['全部','小班课','私教课','精品课'].map(t=>`<button class="chip ${coachType===t?'active':''}" data-action="coachtype" data-value="${t}">${t}</button>`).join('')}</div><p class="small muted" style="margin-bottom:16px">共 ${list.length} 位教练</p><div class="stack">${coachCards(list.slice(0,coachLimit))}</div>${list.length>coachLimit?'<button class="btn light full" style="margin-top:16px" data-action="morecoaches">加载更多教练</button>':list.length?'':'<div class="empty">没有找到符合条件的教练<button class="btn light full" style="margin-top:16px" data-action="resetcoaches">重置筛选</button></div>'}`}
''' + s[end:]
s=s.replace('function coachSlots(id){selectedCoach=id;const c=coaches[id],slots=classes().filter(x=>x.coachId===id);openSheet(`', 'function coachSchedule(){const id=selectedCoach,c=coaches[id],slots=classes().filter(x=>x.coachId===id);return `')
marker="'<div class=\"empty\">暂无可约时段，请选择其他日期。</div>'}`)}"
assert marker in s
s=s.replace(marker,"'<div class=\"empty\">暂无可约时段，请选择其他日期。</div>'}`}" )
s=s.replace('function schedule(){return `<div class="pageintro"><h1>预约课程</h1></div>${storeButton()}', 'function courseSchedule(){return `')
pos=s.index('function courseSchedule()')
s=s[:pos]+'''function schedule(){return `<div class="pageintro row between"><h1>预约</h1><button class="small" style="min-height:44px" data-action="bookings">我的预约 ›</button></div>${storeButton()}<div class="booking-tabs" role="tablist" aria-label="预约方式"><button role="tab" aria-selected="${bookingMode==='course'}" class="${bookingMode==='course'?'active':''}" data-action="bookingmode" data-value="course">按课程预约</button><button role="tab" aria-selected="${bookingMode==='coach'}" class="${bookingMode==='coach'?'active':''}" data-action="bookingmode" data-value="coach">按教练预约</button></div>${bookingMode==='course'?courseSchedule():selectedCoach===null?coachDirectory():coachSchedule()}`}
''' + s[pos:]
s=s.replace("case 'coachday':day=i;render();coachSlots(selectedCoach);break;", "case 'coachday':day=i;render();break;case 'bookingmode':bookingMode=v;selectedCoach=null;render(true);break;case 'coachtype':coachType=v;coachLimit=6;render();break;case 'morecoaches':coachLimit+=6;render();break;case 'clearcoach':coachQuery='';coachLimit=6;render();$('#coachSearch').focus();break;case 'resetcoaches':coachQuery='';coachType='全部';coachLimit=6;render();break;")
s=s.replace("case 'gobook':closeSheet();page=2;render(true);", "case 'gobook':closeSheet();page=2;bookingMode='course';selectedCoach=null;render(true);")
s=s.replace("document.addEventListener('input',e=>{if(e.target.id==='searchInput')", "document.addEventListener('input',e=>{if(e.target.id==='coachSearch'){coachQuery=e.target.value;coachLimit=6;const pos=e.target.selectionStart;render();$('#coachSearch').focus();$('#coachSearch').setSelectionRange(pos,pos);}if(e.target.id==='searchInput')")
s=s.replace('</style>','''
.booking-tabs{display:flex;background:#e6eadf;padding:4px;border-radius:16px;margin:8px 0 20px;gap:4px}.booking-tabs button{flex:1;min-height:44px;border-radius:12px;color:var(--muted)}.booking-tabs button.active{background:var(--ink);color:white;font-weight:600}.scroll>.summary{background:white;border-radius:16px;padding:16px;margin:16px 0}.scroll>.summary .row{margin:8px 0}.scroll>.summary+.summary{margin-top:12px}
</style>''')
p.write_text(s,encoding='utf-8')
