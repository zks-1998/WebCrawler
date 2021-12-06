import requests
import os
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9%E7%AE%80%E5%8E%86'

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@class="imgload"]/div')

if not os.path.exists('./jianli'):
    os.mkdir('./jianli')

for div in div_list:
    src = div.xpath('.//p/strong/a/@href')[0]
    img_src = 'https:' + src
    detail_text = requests.get(url=img_src, headers=headers).text
    tree = etree.HTML(detail_text)
    down_list = tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a')
    down_name = tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
    last_name = down_name.encode('iso-8859-1').decode('utf-8')
    for down in down_list:
        down_src = down.xpath('./@href')[0]
        detail = requests.get(url=down_src, headers=headers).content
        down_path = './jianli/' + last_name+'.rar'
        with open(down_path, 'wb+') as fp:
            fp.write(detail)
            print(last_name, '下载成功！')
