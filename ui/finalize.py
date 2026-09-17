from pathlib import Path
import re
p=Path(__file__).with_name('index.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'<p class="prototype[^\"]*">.*?</p>','',s,flags=re.S)
s=s.replace('function render(reset=false){',"function render(reset=false){if(reset)$('#toast').textContent='';")
s=s.replace('原型采用本人使用、仅购卡门店可用。','仅限本人使用，适用于购卡门店。')
s=s.replace('有效期从购买当天开始计算。门店范围、退卡及延期政策请在购买前确认。此处为原型示例规则。','有效期从购买当天开始。购买前请确认适用门店与退款规则。')
s=s.replace('示例规则：开课前24小时可免费取消并返还次数；到店核销后正式扣次。实际规则以场馆公布为准。','开课前24小时可免费取消并返还次数，到店核销后正式扣次。')
s=s.replace('本卡仅适用于${cardType}，不与其他课型通用。有效期从购买当天开始；演示采用仅本店可用规则。','本卡仅适用于${cardType}，不可跨课型或门店使用，有效期从购买当天开始。')
s=s.replace('总部仓库发货 · 示例运费规则：满 ¥299 包邮，不满收取 ¥12。','总部仓库发货 · 满 ¥299 包邮，不满收取 ¥12。')
p.write_text(s,encoding='utf-8')
