import requests

# UA User-Agent(请求载体身份标识)
# 门户网址的服务器会检测对应请求载体身份标识。
# 如果检测到请求的载体身份标识为某一款浏览器，意味着当前的用户请求是一个通过浏览器发起的正常的请求。说明是一个正常的请求（用户通过浏览器发出的请求）。
# 但是，如果检测到的请求的载体身份标识不是基于某一款浏览器的，则表示该请求为一个不正常的请求（是一个爬虫请求），则服务器端很有可能拒绝该次请求。
# 为了让我们的请求每次都成功，我们要进行UA伪装。

# 01.指定url
url = 'https://www.sogou.com/web'
# 02.UA伪装：将对应的UA伪装到字典中 反反爬策略
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
# 03.搜索的拼接关键字 封装到字典
kw = input('enter a word:')
param = {
    'query': kw  # query=kw
}
# 04.得到响应对象
response = requests.get(url=url, params=param, headers=headers)  # 这里自动拼接了一个url url?query=kw
# 05.持久化数据
page_text = response.text
fileName = kw + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('保存成功！')
