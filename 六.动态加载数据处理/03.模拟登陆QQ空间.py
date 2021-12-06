from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://qzone.qq.com/')
# 先定位到iframe
driver.switch_to.frame('login_frame')

div = driver.find_element_by_id('switcher_plogin')

div.click()

user = driver.find_element_by_id('u')
password = driver.find_element_by_id('p')
user.send_keys('1355776458')
password.send_keys('lxydsb666')

login = driver.find_element_by_id('login_button')
login.click()





