#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PO.desired_caps import appium_desired
from PO.basepage import Base
import time
import yaml
from PO.basepage import Base
import logging


# with open('C:\\ClientTest\Yaml\login.yaml', 'r', encoding='utf-8') as file:
#     data = yaml.load(file)
with open('..\Yaml\login.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file,Loader=yaml.FullLoader)


class Login(Base):  # 无法查询到登录界面的UI
    wode_loc = eval(data['Login']['wode_loc'])  # 我的页面
    denglu_loc = eval(data['Login']['denglu_loc'])  # 登录按钮
    zhanghao_loc = eval(data['Login']['zhanghao_loc'])  # 账号输入框
    yanzheng_loc = eval(data['Login']['yanzheng_loc'])  # 验证码按钮
    shuru_loc = eval(data['Login']['shuru_loc'])  # 输入验证码框
    denglu2_loc = eval(data['Login']['denglu2_loc'])  # 登录按钮
    next_loc = eval(data['Login']['next_loc'])  # 下次再说
    title_loc = eval(data['Login']['title_loc'])  # 登录页面标题
    l_close_loc = eval(data['Login']['l_close_loc'])  # 登录页返回关闭
    zddl_loc = eval(data['Login']['zddl_loc'])  # 自动登录
    scan_loc = eval(data['Login']['scan_loc'])  # 删除按钮
    lxr_loc = eval(data['Login']['scan_loc'])  # 联系人
    search_loc = eval(data['Login']['search_loc'])  # 联系人搜索
    L_back_loc = eval(data['Login']['L_back_loc'])  # 联系人返回

    # 定位我的页面进入我的页面
    def wode(self):
        self.click_button(self.wode_loc)
        logging.info("进入我的页面")

    # 定位登录按钮进入登录页面
    def denglu(self):
        self.click_button(self.denglu_loc)
        logging.info("进入登录页面")

    # 定位输入框，输入账号
    def zhanghao(self, num):
        self.send_keys(self.zhanghao_loc, num)
        logging.info('输入账号')

    # 点击验证码
    def yanzheng(self):
        self.click_button(self.yanzheng_loc)
        logging.info('点击验证码')

    # 输入验证码
    def shuru(self, yanzhengma):
        self.yanzhengma = yanzhengma
        self.send_keys(self.shuru_loc, yanzhengma)
        logging.info('输入验证码')

    # 点击登录按钮
    def chick_login(self):
        self.click_button(self.denglu2_loc)
        logging.info('点击登录按钮')

    # 手势登录下次再说
    def next(self):
        try:
            self.click_button(self.next_loc)
            logging.info("点击下次再说")
        except:
            pass

    def login(self, num):  # 登录页登录
        self.zhanghao(num)
        logging.info("登录账号:%s" % (num))
        self.yanzheng()
        logging.info("获取验证码")
        time.sleep(20)
        # yanzhengma = input("请输入验证码：")
        # self.shuru(yanzhengma)
        # print("输入验证码：%s"%(yanzhengma))
        self.chick_login()
        logging.info("点击登录")
        self.next()
        logging.info('点击下次再说')

    def close(self):  # 登录页返回关闭
        try:
            self.click_button(self.l_close_loc)
            logging.info('关闭登录页面')
        except:
            pass

    def lxr(self):
        self.click_button(self.lxr_loc)
        logging.info('点击联系人')

    def L_back(self):
        self.click_button(self.L_back_loc)
        logging.info('点击联系人返回')


if __name__ == '__main__':
    driver = appium_desired()
    ba = Login(driver)
    ba.start()
    ba.wode()
    ba.denglu()
    ba.login('13715307043')
