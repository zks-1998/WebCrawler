import requests
import json

# 01.指定url 发送post请求
post_url = 'https://fanyi.baidu.com/sug'
# 02.UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
# 03.post请求的参数
word = input('enter a word:')
data = {
    'kw': word
}
# 04.发送POST请求获取响应对象
response = requests.post(url=post_url, data=data, headers=headers)
# 05.返回的是JOSN数据
dic_obj = response.json()
print(dic_obj)
