from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url=url, headers=headers)
page_text.encoding = 'utf-8'
# 实例化对象并且将网页源码加载到对象中 第二个参数lxml是固定的
soup = BeautifulSoup(page_text.text, 'lxml')
# select 选择标签 .XX:类选择器
li_list = soup.select('.book-mulu ul li')
for li in li_list:
    title = li.a.string  # li标签下的a标签间的文本数据
    detail_url = 'https://www.shicimingju.com/' + li.a['href']  # 标签属性值提取
    # 获取了详情页面
    detail_page = requests.get(url=detail_url, headers=headers)
    detail_page.encoding = 'utf-8'
    detail_soup = BeautifulSoup(detail_page.text, 'lxml')
    detail_data = detail_soup.find('div', class_='chapter_content').text.replace(u'\xa0', u' ')
    with open('./sanguo.txt', 'a', encoding='utf-8') as fp:
        fp.write(title+':'+detail_data+'\n')
    print(title+' '+"爬取成功!")

