from selenium import webdriver
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
driver.switch_to.frame('iframeResult')  # iframeResult是iframe的id，切换浏览器标签定位的作用域

div = driver.find_element_by_id('draggable')

# 动作链
action = ActionChains(driver)
# 点击长按
action.click_and_hold(div)

for i in range(5):
    # perform()立即执行动作链操作
    # move_by_offset(x,y):x水平方向 y竖直方向
    action.move_by_offset(17, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()

