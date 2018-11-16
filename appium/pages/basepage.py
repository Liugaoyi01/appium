# coding = utf-8
''' 封装公共的方法及驱动 '''
from appium import webdriver
import time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Base:

    def __init__(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'platformVersion': '5.1.1',
            'appPackage': 'com.greenpoint.android.mc10086.activity',  # apk包名
            'appActivity': 'com.leadeon.cmcc.base.StartPageActivity',  # apk的launcherActivity
            'unicodeKeyboard': True,  # 使用Unicode编码方式发送字符串
            'resetKeyboard': True  # 将键盘隐藏起来
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver

    # 封装单个元素定位方法

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u'页面中通过%s未能找到%s元素' % (loc))

    # 封装一组元素定位方法

    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            print(u'页面中通过%s未能找到%s元素' % (loc))

    # 重新封装点击方法
    def click_button(self, loc):
        try:
            self.find_element(*loc).click()
        except:
            print(u'页面中通过%s未能找到%s按钮' % (loc))

    # 滑动封装-向左滑动
    '''
        参数1：t是持续时间单位：毫秒
        参数2：滑动次数
    '''

    def swipe_left(self, t=500, n=1):

        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75  # 起点横坐标
        y = l['height'] * 0.5  # 纵坐标
        x2 = l['width'] * 0.25  # 终点横坐标

        for i in range(n):
            self.driver.swipe(x1, y, x2, y, t)

    # 滑动封装-向右滑动

    def swipe_right(self, t=500, n=1):

        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25  # 起点横坐标
        y = l['height'] * 0.5  # 纵坐标
        x2 = l['width'] * 0.75  # 终点横坐标

        for i in range(n):
            self.driver.swipe(x1, y, x2, y, t)

    # 滑动封装-向上滑动

    def swipe_up(self, t=500, n=1):

        l = self.driver.get_window_size()
        x = l['width'] * 0.5  # 横坐标
        y1 = l['height'] * 0.75  # 起点纵坐标
        y2 = l['height'] * 0.25  # 终点纵坐标

        for i in range(n):
            self.driver.swipe(x, y1, x, y2, t)

    # 滑动封装-向下滑动

    def swipe_down(self, t=500, n=1):

        l = self.driver.get_window_size()
        x = l['width'] * 0.5  # 横坐标
        y1 = l['height'] * 0.25  # 起点纵坐标
        y2 = l['height'] * 0.75  # 终点纵坐标

        for i in range(n):
            self.driver.swipe(x, y1, x, y2, t)

    # 重新封装输入方法

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()

            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print(u'页面中通过%s未能找到%s元素' % (loc))
    def back(self):
        try:
             

    # 封装坐标点击方法

    def tap(self, x, y):
        try:
            self.driver.tap([(x, y)])
        except:
            pass

    # 获取时间

    def get_time(self):
        return time.strftime('%Y-%m-%d-%H-%M-%S', (time.localtime(time.time())))

    # 以当前时间+自定义名称命名保存截图
    def get_screenshot(self):
        tm = self.get_time()
        file_name = '..\\result\\image\\%s.png' % tm
        self.driver.get_screenshot_as_file(file_name)


# 定义一个启动到首页的方法
def start():
    base = Base()
    #ac = base.get_driver().current_activity
    time.sleep(6)
    base.swipe_left(t=1000, n=5)
    time.sleep(3)
    base.tap(278, 750)
    time.sleep(5)
    try:
        base.get_driver().wait_activity('com.leadeon.cmcc.view.tabs.AppTabFragment',5)
        print('客户端启动成功，已进入首页')
    except TimeoutError:
        print('检测未进入首页')
    base.get_screenshot()

if __name__ == '__main__':
    start()