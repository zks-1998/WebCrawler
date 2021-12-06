import requests
from hashlib import md5
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/92.0.4515.131 Safari/537.36 '
}
# 1.创建一个session
s = requests.session()
# 2.获取验证码链接
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = s.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
src = tree.xpath('//*[@id="imgCode"]/@src')[0]
img_src = 'https://so.gushiwen.cn' + src
# 3.将验证码图片保存到本地
img_data = s.get(url=img_src, headers=headers).content
with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)


class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

# 4.使用超级鹰将验证码读取出来
chaojiying = Chaojiying_Client('1355776458', 'zks1355776458', '920974')
im = open('./code.jpg', 'rb').read()
result = chaojiying.PostPic(im, 1004)['pic_str']
print(result)
# 5.模拟登陆 post请求
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
__VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
data = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '17852422531',
    'pwd': 'zks1355776458',
    'code': result,
    'denglu': '登录'
}
login_page = s.post(url=post_url, headers=headers, data=data)
print(login_page.status_code)

# 6.登陆成功爬取详情页并保存到本地
detail_page = 'https://so.gushiwen.cn/user/collect.aspx'
detail_page_text = s.get(url=detail_page, headers=headers).text
with open('./detail.html', 'w', encoding='utf-8') as fp:
    fp.write(detail_page_text)
