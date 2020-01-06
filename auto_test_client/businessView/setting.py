#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from auto_test_client.public.desired_caps import appium_desired
from auto_test_client.baseView.basepage import Base
import time
import yaml
from auto_test_client.utils import openYaml
import logging

settings_path = "../../data/settings.yaml"
data = openYaml.get_yaml_data(settings_path)


class Settings(Base):
    wode_loc = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout/android.widget.RelativeLayout[5]")  # 我的页面
    settings_loc = (By.ID,'setting_btn')            # 设置按钮
    login_settings_loc = (By.ID,'loginSet')                   # 登录设置
    automatic_loc = (By.ID,'safety_auto')                # 自动登录
    pushed_loc = (By.ID,'pushMsgSet')                   # 消息推送
    mes_not_loc = (By.ID,'pushthemessageset_inform')   # 消息通知
    notification_loc = (By.ID,'notificationSet')             # 常驻通知栏
    switch_loc = (By.ID,'notificationValueSet')   # 通知栏开关
    wlan_loc =  (By.ID,'wlan_set')                  # wlan设置
    head_loc = (By.ID,'title_name_txt')            # wlan头部展示
    account_loc = (By.ID,'settings_bings_txt')        # 第3方账号绑定
    binding_loc = ( By.ID,'settings_bindingreferences_text')  # 绑定联系人
    save_button_loc = (By.ID,'save_btn')                      # 保存按钮
    remove_loc = (By.ID,'wipeCache')                       # 清除缓存
    cancel_loc = (By.ID,'cmessage')                       # 取消按钮
    service_loc = (By.NAME,'服务协议')                      # 服务协议
    information_loc = (By.ID,'user_protection_layout')         # 个人信息保护政策
    personal_inf_loc = (By.ID,'com.greenpoint.android.mc10086.activity:id/title_name_txt')  # 个人信息展示
    help_loc = (By.ID,'helpCenter')           # 帮助中心
    help_internal_loc = (By.XPATH,"//*[contains(@text,'帮助中心')]") # 帮助中心内部展示
    about_intro_loc = (By.ID,'aboutUs') # 关于我们
    about_who_loc = (By.XPATH,"//*[contains(@text,'关于我们')]")  # 关于我们内部展示
    denglu_loc = (By.ID,'settings_exit_btn') # 登录按钮
    login_loc = (By.ID,'autologin_btn') # 登录按钮
    queren_loc = (By.ID,'dialog_btn2')  # 确认按钮
    l_close_loc = (By.ID,'login_close')  # 登录页返回
    title_loc = (By.ID,'title_name_txt')

    # 定位我的页面进入我的页面
    def wode(self):
        self.click_button(self.wode_loc)
        logging.info("进入我的页面")

    # 定位设置按钮进入设置页面
    def settings(self):
        self.click_button(self.settings_loc)
        logging.info("进入设置页面")

    # 定位登录设置进入登录设置
    def settinga(self):
        self.click_button(self.login_settings_loc)
        logging.info("进入登录设置")

    # 定位消息推送进入消息推送
    def settingb(self):
        self.click_button(self. pushed_loc)
        logging.info("进入消息推送")

    # 定位常驻通知栏进入常驻通知栏
    def settingc(self):
        self.click_button(self.notification_loc)
        logging.info("进入通知栏")

    # 定位WlAN设置进入WlAN设置
    def settingd(self):
        self.click_button(self.wlan_loc)
        logging.info("进入wlan设置")

    # 定位第3方账号绑定进入第3方账号绑定
    def settinge(self):
        self.click_button(self.account_loc)
        logging.info("进入账号绑定")

    # 定位绑定推荐人进入推荐人
    def settingf(self):
        self.click_button(self.binding_loc)
        logging.info("进入联系人")

    def queren(self):
        self.back()
        self.click_button(self.queren_loc)

    # 定位清除缓存进入缓存
    def settingg(self):
        self.click_button(self.remove_loc)
        self.click_button(self.queren_loc)
        logging.info("清除缓存")

    # 定位服务协议进入服务协议
    def settingh(self):
        self.click_button(self.service_loc)
        logging.info("服务协议")

    # 定位个人信息进入个人信息
    def settingi(self):
        self.click_button(self.information_loc)
        logging.info("个人信息")

    # 定位帮助中心进入帮助中心
    def settingj(self):
        self.click_button(self.help_loc)
        logging.info("帮助中心")

    # 定位关于我们进入关于我们
    def settingk(self):
        self.click_button(self.about_intro_loc)
        logging.info("关于我们")

    # 定位登录进入登录页面
    def settingl(self):
        self.click_button(self.denglu_loc)
        logging.info("进入登录页面")

    def l_close(self):
        self.click_button(self.l_close_loc)
        logging.info("登录页返回")


if __name__ == '__main__':
    driver = appium_desired()
