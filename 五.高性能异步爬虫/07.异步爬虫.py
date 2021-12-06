import aiohttp
import asyncio
from lxml import etree
from selenium import webdriver

url = 'https://www.dushu.com/guoxue/103786/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get(url=url)
page_text = bro.page_source
tree = etree.HTML(page_text)
tr_list = tree.xpath('//*[@id="ctl00_c1_volumes_ctl00_chapters"]/tbody/tr')

dic_list = []
for tr in tr_list:
    td_list = tr.xpath('./td')
    for td in td_list:
        dic = {
            'title': td.xpath('./a/text()')[0],
            'src': 'https://www.dushu.com/' + td.xpath('./a/@href')[0]
        }
        dic_list.append(dic)
bro.quit()


async def download(dic):
    content_path = './xiyouji/' + dic['title']+'.txt'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=dic['src'], headers=headers) as response:
            detail_page_text = await response.text()
            tree_s = etree.HTML(detail_page_text)
            content_list = tree_s.xpath('//div[@class="content_txt"]/text()')
            content_text = "\n".join(content_list)
            with open(content_path, 'w') as fp:
                fp.write(content_text)
            print(dic['title'], '下载成功！')


async def main():
        task_list = []
        for dic in dic_list:
            task_list.append(asyncio.create_task(download(dic)))
        await asyncio.wait(task_list, timeout=None)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


