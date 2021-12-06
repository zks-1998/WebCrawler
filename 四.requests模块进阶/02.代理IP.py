# 需求：
import requests

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}

page_text = requests.get(url=url, headers=headers, proxies={"https": '222.110.147.50:3128'}).text

with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

# 反爬机制：  封ip
# 反反爬策略：使用代理进行请求发送
