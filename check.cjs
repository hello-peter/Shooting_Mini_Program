const {chromium}=require('C:/Users/TANG/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({headless:true,channel:'chrome'});
 const page=await browser.newPage({viewport:{width:1440,height:1040},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('file:///C:/Users/TANG/Desktop/MiniPro/ui/index.html');
 fs.mkdirSync('ui/preview',{recursive:true});
 for(let n=0;n<5;n++){await page.locator('#tabbar button').nth(n).click();await page.screenshot({path:`ui/preview/page-${n}.png`});}
 await page.locator('#tabbar button').nth(1).click();
 await page.locator('[data-action="buy"]').first().click();
 await page.locator('#agreement').check();await page.locator('[data-action="paycard"]').click();
 await page.getByRole('heading',{name:'购卡成功'}).waitFor();
 await page.locator('[data-action="gobook"]').click();await page.locator('[data-action="book"]').first().click();
 await page.locator('[data-action="confirmbook"]').click();await page.getByRole('heading',{name:'预约成功'}).waitFor();
 await page.screenshot({path:'ui/preview/booking-success.png'});
 await page.locator('#sheetContent [data-action="bookings"]').click();await page.locator('[data-action="cancelbook"]').click();
 await page.locator('[data-action="close"]').click();
 await page.locator('#tabbar button').nth(3).click();await page.locator('#searchInput').fill('不存在');
 await page.getByRole('heading',{name:'暂时没有找到'}).waitFor();
 await page.locator('[data-action="searchclear"]').click();await page.locator('[data-action="add"]').first().click();
 await page.locator('[data-action="cart"]').first().click();await page.locator('[data-action="checkout"]').click();
 await page.screenshot({path:'ui/preview/checkout.png'});
 await page.locator('[data-action="paygoods"]').click();await page.getByRole('heading',{name:'支付成功'}).waitFor();
 await page.locator('[data-action="close"]').click();
 await page.setViewportSize({width:375,height:812});
 for(let n=0;n<5;n++){
  await page.locator('#tabbar button').nth(n).click();
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);if(overflow)throw new Error('overflow page '+n);
  await page.screenshot({path:`ui/preview/mobile-${n}.png`});
 }
 if(errors.length)throw new Error(errors.join('\n'));
 console.log('PASS: 5 screens, 375px layout, purchase, booking, cancellation, search, cart, checkout; no JS errors.');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
