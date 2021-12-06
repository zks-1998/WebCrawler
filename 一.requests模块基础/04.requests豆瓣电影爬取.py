import requests

url = 'https://movie.douban.com/j/chart/top_list'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}

param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',  # 从第几个开始
    'limit': '20'  # 选择几个
}

response = requests.get(url=url, params=param, headers=headers)

dic_obj = response.json()
print(dic_obj)
