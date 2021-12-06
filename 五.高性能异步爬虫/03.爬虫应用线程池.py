import requests
import os
from lxml import etree
from selenium import webdriver
from multiprocessing.dummy import Pool

if not os.path.exists('./lishipin'):
    os.mkdir('./lishipin')
# 实例化一个浏览器对象（传入浏览器的驱动）
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}

driver.get('https://www.pearvideo.com/popular')
i = 100
for i in range(2, 500):  # 设置一个较大的数，一下到底
    js = "var q=document.documentElement.scrollTop={}".format(i * 100)  # javascript语句
    driver.execute_script(js)
page_text = driver.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="popular-list"]/li')
urls = []  # 列表储存视频链接和名字
for li in li_list:
    video_detail_src = 'https://www.pearvideo.com/' + li.xpath('.//a/@href')[0]
    video_name = li.xpath('.//a[@class="popularembd actplay"]/h2/text()')[0] + '.mp4'
    driver.get(video_detail_src)
    video_detail_text = driver.page_source
    tree = etree.HTML(video_detail_text)
    mp4_url = tree.xpath('//*[@id="JprismPlayer"]/video/@src')[0]
    dic = {
        'name': video_name,
        'url': mp4_url
    }
    urls.append(dic)


def get_video(dic):
    url = dic['url']
    print(dic['name'], '正在下载...')
    mp4_content = requests.get(url=url, headers=headers).content
    video_path = './lishipin/' + dic['name']
    with open(video_path, 'wb') as fp:
        fp.write(mp4_content)
        print(dic['name'], '下载成功！')


pool = Pool(80)
pool.map(get_video, urls)
pool.close()
