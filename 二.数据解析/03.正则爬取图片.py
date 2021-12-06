import requests
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
# 创建文件夹保存图片
if not os.path.exists('./qiutu'):
    os.mkdir('./qiutu')
# 爬取前3页的数据
url = 'https://www.qiushibaike.com/imgrank/page/%d/'
for i in range(1, 3):
    new_url = format(url % i)
    # 爬取整张页面的前端代码
    page_text = requests.get(url=new_url, headers=headers).text
    # print(page_text)
    # 爬取图片地址的正则表达式
    ex = '<div class="thumb">.*?<img src="(.*?)".*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)
    for src in img_src_list:
        # 拼接src
        src = 'https:' + src
        # 图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 图片名称
        img_name = src.split('/')[-1]
        img_path = './qiutu/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！')
