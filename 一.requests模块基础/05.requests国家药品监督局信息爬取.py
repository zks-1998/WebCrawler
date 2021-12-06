import requests

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
id_list = []
for page in range(1, 5):
    data = {
        'on': 'true',
        'page': page,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': ''
    }
    json_ids = requests.post(url=url, data=data, headers=headers).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])


post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data = {
        'id': id
    }
    detail_json = requests.post(url=post_url, data=data, headers=headers).json()
    print(detail_json)
