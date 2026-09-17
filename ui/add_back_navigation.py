from pathlib import Path
p=Path(__file__).with_name('index.html')
s=p.read_text(encoding='utf-8')
s=s.replace('<div class="appbrand" id="appbrand"></div>', '<div class="row" style="gap:4px"><button id="pageBack" class="iconbtn" data-action="pageback" aria-label="返回上一页" hidden><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m15 5-7 7 7 7"/></svg></button><div class="appbrand" id="appbrand"></div></div>')
s=s.replace('</style>','#pageBack[hidden]{display:none}.appbar{min-height:56px}#pageBack{margin-left:-12px}\n</style>')
s=s.replace('function coachList(){closeSheet();', 'function coachList(){navigationStack.length=0;closeSheet();')
s=s.replace('function coachSlots(id){closeSheet();', '''const navigationStack=[];
function saveNavigation(){return {page,bookingMode,selectedCoach,coachQuery,coachType,coachLimit,day,store,scroll:$('#screen').scrollTop}}
function goBack(){const previous=navigationStack.pop();if(!previous)return;({page,bookingMode,selectedCoach,coachQuery,coachType,coachLimit,day,store}=previous);closeSheet();render();$('#screen').scrollTop=previous.scroll;}
function coachSlots(id){navigationStack.push(saveNavigation());closeSheet();''')
s=s.replace('<button class="small" style="min-height:44px" data-action="coach">‹ 全部教练</button>', '')
s=s.replace('function render(reset=false){', '''function render(reset=false){const detail=page===2&&selectedCoach!==null&&bookingMode==='coach';$('#pageBack').hidden=!detail||!navigationStack.length;$('#appbrand').innerHTML=detail?'教练预约':icon('target')+'XX射击俱乐部';''')
s=s.replace("case 'nav':page=i;", "case 'pageback':goBack();break;case 'nav':navigationStack.length=0;selectedCoach=null;page=i;")
s=s.replace("case 'bookingmode':bookingMode=v;", "case 'bookingmode':navigationStack.length=0;bookingMode=v;")
p.write_text(s,encoding='utf-8')
