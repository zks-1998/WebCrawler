import requests
from hashlib import md5
from selenium import webdriver
# 导入动作链对应的类
from selenium.webdriver import ActionChains
# 实现规避检测
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=option)
# 动作链
action = ActionChains(driver)

driver.get('https://kyfw.12306.cn/otn/resources/login.html')
driver.maximize_window()
login = driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
login.click()
verify_img = driver.find_element_by_xpath('//*[@id="J-loginImg"]')


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


chaojiying = Chaojiying_Client('1355776458', 'zks1355776458', '920974')
dic = chaojiying.PostPic(verify_img.screenshot_as_png, 9004)
rs = dic['pic_str']
rs_list = rs.split('|')
print(rs_list)
for rs in rs_list:
    p_temp = rs.split(',')
    x = int(p_temp[0])
    y = int(p_temp[1])
    action.move_to_element_with_offset(verify_img, x, y).click().perform()  # 移动到该节点的左上角并且偏移x和y

driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys('123456789')
driver.find_element_by_xpath('//*[@id="J-password"]').send_keys('123456789')

driver.find_element_by_xpath('//*[@id="J-login"]').click()

# 拖拽滑块
