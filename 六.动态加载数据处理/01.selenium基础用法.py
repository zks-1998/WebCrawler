import requests
import os
from lxml import etree
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
if not os.path.exists('./tupian'):
    os.mkdir('./tupian')
# 实例化一个浏览器对象（传入浏览器的驱动）
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# 让浏览器发起一个指定的url请求
bro.get('https://stock.tuchong.com/topic?topicId=50043')
# 获取当前页面的源码数据（动态加载的也被爬取捕获）
page_text = bro.page_source

tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@class="justified-layout"][position()=1]/div')


for div in div_list:
    detail_page = 'https://stock.tuchong.com' + div.xpath('.//a/@href')[0]
    bro.get(detail_page)
    detail_page_text = bro.page_source
    tree = etree.HTML(detail_page_text)
    img_src = 'https:'+tree.xpath('//div[@class="image-detail-carousel__item J_LazyLoad tt-img-loaded"]/@data-lazy-url')[0]
    img_content = requests.get(url=img_src, headers=headers).content
    img_name = tree.xpath('//div[@class="image-detail-infos"]/h1/@title')[0]+'.webp'
    img_path = './tupian/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_content)
bro.quit()
