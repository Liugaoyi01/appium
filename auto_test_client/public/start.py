# 定义一个启动到首页的方法

from auto_test_client.public.desired_caps import appium_desired
from auto_test_client.baseView.basepage import Base
import logging
import time

def start_index(driver):
    base = Base(driver)
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    print(X, Y)
    base.tap((141 / 1080) * X, (1487 / 1920) * Y)
    logging.info('勾选隐私协议')
    base.tap((516 / 1080) * X, (1666 / 1920) * Y)
    logging.info('点击同意')
    time.sleep(9)
    base.swipe_left(t=1000, n=3)
    time.sleep(3)
    base.tap((533 / 1080) * X, (1571 / 1920) * Y)  # 真机：(533,1380)；模拟器：(539, 1556)
    logging.info('点击立即开启')
    # try:
    #     button = self.driver.find_element_by_id('app_startPage_skip')
    # except NoSuchElementException:
    #     logging.info("无跳过button")
    # else:
    #     button.click()
    time.sleep(7)
    try:
        driver.find_element_by_xpath("//*[contains(@text,'首页')]")
        logging.info('客户端启动成功，已进入首页')
    except:
        logging.error('检测未进入首页')
    # time.sleep(3)
    # self.get_screenshot('首页')  # 此处用来测试截图功能，后面可以忽略