# coding = utf-8
# -*- coding:utf-8 -*-

# 封装公共的方法及驱动

from appium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from auto_test_client.public.desired_caps import appium_desired
import logging


class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    # 封装单个元素定位方法

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            logging.warning(u'页面中通过%s未能找到%s元素' % (loc))

    # 封装一组元素定位方法

    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            logging.warning(u'页面中通过%s未能找到%s元素' % (loc))

    # 重新封装点击方法
    def click_button(self, *loc):
        try:
            self.find_element(*loc).click()
        except NoSuchElementException:
            logging.warning(u'页面中通过%s未能找到%s按钮' % (loc))

    # 重新封装判断元素存在方法
    def try_find(self, loc):

        try:
            self.find_element(loc).is_displayed()
            logging.info(u'元素%s-%s存在,返回True' % (loc))
            return True
        except:
            logging.info(u'元素%s-%s不存在,返回False' % (loc))
            return False

    # 获取元素文本text
    def try_text(self, loc):
        try:
            text = self.find_element(loc).text
            logging.info(u'元素%s文本为：%s ' % (loc, text))
            return text
        except:
            pass

    # 获取元素文本content-desc
    def try_desc(self, loc):
        try:
            text = self.find_element(loc).get_attribute('name')
            logging.info(u'元素%s文本为：%s ' % (loc, text))
            return text
        except:
            pass

    chongzhi_loc = (By.XPATH, '//*[@content-desc="充值交费"]')
    title_loc = (By.ID, 'title_name_txt')
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
        except NoSuchElementException:
            logging.warning(u'页面中通过%s未能找到%s元素' % (loc))

    def back(self):
        back_loc = (By.ID, 'title_back_btn')
        try:
            self.click_button(back_loc)
            logging.info('页面返回')
        except:
            pass

    def close(self):
        close_loc = (By.ID, 'title_close_btn')
        try:
            self.click_button(close_loc)
            logging.info('页面关闭')
        except:
            pass

    # 封装坐标点击方法

    def tap(self, x, y):
        try:
            self.driver.tap([(x, y)])
            logging.info('点击坐标')
        except:
            pass

    # 封装忽略点击

    def hulie(self):
        hulie_loc = (By.ID, 'dialog_btn1')
        try:
            self.click_button(hulie_loc)
            logging.info('点击忽略升级')
        except:
            pass

    # 获取时间

    def get_time(self):
        return time.strftime('%Y-%m-%d-%H-%M-%S', (time.localtime(time.time())))

    # 以当前时间+自定义名称命名保存截图
    def get_screenshot(self, name):
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = '..\Result\image' + day
        tm = time.strftime('%Y-%m-%d-%H-%M-%S', (time.localtime(time.time())))
        type = '.png'

        if os.path.exists(fp):
            filename = fp + '\\' + tm + '_' + name + type
        else:
            os.makedirs(fp)
            filename = fp + '\\' + tm + '_' + name + type

        self.driver.get_screenshot_as_file(filename)


if __name__ == '__main__':
    driver= appium_desired()
    base = Base(driver)
    base.start()

