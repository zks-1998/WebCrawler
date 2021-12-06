import requests

#1.指定url
url = 'https://www.sogou.com/'
#2.发起请求 get方法返回响应对象
response = requests.get(url=url)
#3.获取响应数据
page_text = response.text
#4.持久化数据
print(page_text)
