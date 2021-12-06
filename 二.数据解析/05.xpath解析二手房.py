
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
url = 'https://jn.58.com/ershoufang/?from=esf'

page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)

div_list = tree.xpath('//section[@class="list"][position()=1]/div')
fp = open('./58.txt', 'w', encoding='utf-8')
for div in div_list:
    title = div.xpath('.//h3/@title')[0]  # .表示当前div 一定要加.
    fp.write(title+'\n')
