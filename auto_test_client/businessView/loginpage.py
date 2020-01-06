#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from auto_test_client.public.desired_caps import appium_desired
from auto_test_client.baseView.basepage import Base
import time
import yaml
import logging
from auto_test_client.utils import getLoger, openYaml
import os

path = os.path.dirname(os.getcwd())
login_path = path + "/data/login.yaml"
data = openYaml.get_yaml_data(login_path)


class Login(Base):  # 无法查询到登录界面的UI
    wode_loc =  (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.ImageView") # 我的页面
    denglu_loc = (By.ID,'mine_login_btn') # 登录按钮
    account_number_loc = (By.ID,'user_phoneno_edt')  # 账号输入框
    captcha_loc = (By.ID,'com.greenpoint.android.mc10086.activity:id/login_checksms_btn')  # 验证码按钮
    my_vCode_loc = (By.ID,'user_login_smspassword_edt')  # 输入验证码框
    login_button_loc = (By.ID,'one_key_login_btn')  # 登录按钮
    nextld_loc = (By.ID,'dialog_btn1')  # 下次再说
    set_title_loc = (By.ID,'tv_title')  # 登录页面标题
    shutdown_loc = (By.ID,'login_close')  # 登录页返回关闭
    setlogin_loc = (By.ID,'autologin_btn')  # 自动登录
    delete_button_loc = (By.ID,'com.greenpoint.android.mc10086.activity:id/clear_phone_num_img') # 删除按钮
    contact_loc = (By.ID,'com.greenpoint.android.mc10086.activity:id/get_contacts_img')  # 联系人
    search_loc = (By.XPATH,'//android.widget.TextView[@content-desc="搜索"]')  # 联系人搜索
    L_back_loc = (By.XPATH,'//android.widget.ImageButton[@content-desc="向上导航"]') # 联系人返回

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
        self.send_keys(self.account_number_loc, num)
        logging.info('输入账号')

    # 点击验证码
    def yanzheng(self):
        self.click_button(self.captcha_loc)
        logging.info('点击验证码')

    # 输入验证码
    def shuru(self, yanzhengma):
        self.yanzhengma = yanzhengma
        self.send_keys(self. my_vCode_loc, yanzhengma)
        logging.info('输入验证码')

    # 点击登录按钮
    def chick_login(self):
        self.click_button(self.login_button_loc)
        logging.info('点击登录按钮')

    # 手势登录下次再说
    def next(self):
        try:
            self.click_button(self. nextld_loc)
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
            self.click_button(self. shutdown_loc)
            logging.info('关闭登录页面')
        except:
            pass

    def lxr(self):
        self.click_button(self.contact_loc)
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
    ba.login('15012761017')
