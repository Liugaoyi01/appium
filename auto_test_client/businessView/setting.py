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
    wode_loc = eval(data['Settings']['wode_loc'])  # 我的页面
    settings_loc = eval(data['Settings']['settings_loc'])  # 设置按钮
    dlsz_loc = eval(data['Settings']['dlsz_loc'])  # 登录设置
    zddl_loc = eval(data['Settings']['zddl_loc'])  # 自动登录
    xxts_loc = eval(data['Settings']['xxts_loc'])  # 消息推送
    xxtz_loc = eval(data['Settings']['xxtz_loc'])  # 消息通知
    tzl_loc = eval(data['Settings']['tzl_loc'])  # 常驻通知栏
    kaiguan_loc = eval(data['Settings']['kaiguan_loc'])  # 通知栏开关
    wlan_loc = eval(data['Settings']['wlan_loc'])  # wlan设置
    toubu_loc = eval(data['Settings']['toubu_loc'])  # wlan头部展示
    zhbd_loc = eval(data['Settings']['zhbd_loc'])  # 第3方账号绑定
    bdlxr_loc = eval(data['Settings']['bdlxr_loc'])  # 绑定联系人
    baocun_loc = eval(data['Settings']['baocun_loc'])  # 保存按钮
    qchc_loc = eval(data['Settings']['qchc_loc'])  # 清除缓存
    qxiao_loc = eval(data['Settings']['qxiao_loc'])  # 取消按钮
    fwxy_loc = eval(data['Settings']['fwxy_loc'])  # 服务协议
    grxx_loc = eval(data['Settings']['grxx_loc'])  # 个人信息保护政策
    gr_loc = eval(data['Settings']['gr_loc'])  # 个人信息展示
    help_loc = eval(data['Settings']['help_loc'])  # 帮助中心
    he_loc = eval(data['Settings']['he_loc'])  # 帮助中心内部展示
    gywm_loc = eval(data['Settings']['gywm_loc'])  # 关于我们
    gy_loc = eval(data['Settings']['gy_loc'])  # 关于我们内部展示
    denglu_loc = eval(data['Settings']['denglu_loc'])  # 登录按钮
    login_loc = eval(data['Settings']['login_loc'])  # 登录按钮
    queren_loc = eval(data['Settings']['queren_loc'])  # 确认按钮
    l_close_loc = eval(data['Settings']['l_close_loc'])  # 登录页返回
    title_loc = eval(data['Settings']['title_loc'])

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
        self.click_button(self.dlsz_loc)
        logging.info("进入登录设置")

    # 定位消息推送进入消息推送
    def settingb(self):
        self.click_button(self.xxts_loc)
        logging.info("进入消息推送")

    # 定位常驻通知栏进入常驻通知栏
    def settingc(self):
        self.click_button(self.tzl_loc)
        logging.info("进入通知栏")

    # 定位WlAN设置进入WlAN设置
    def settingd(self):
        self.click_button(self.wlan_loc)
        logging.info("进入wlan设置")

    # 定位第3方账号绑定进入第3方账号绑定
    def settinge(self):
        self.click_button(self.zhbd_loc)
        logging.info("进入账号绑定")

    # 定位绑定推荐人进入推荐人
    def settingf(self):
        self.click_button(self.bdlxr_loc)
        logging.info("进入联系人")

    def queren(self):
        self.back()
        self.click_button(self.queren_loc)

    # 定位清除缓存进入缓存
    def settingg(self):
        self.click_button(self.qchc_loc)
        self.click_button(self.queren_loc)
        logging.info("清除缓存")

    # 定位服务协议进入服务协议
    def settingh(self):
        self.click_button(self.fwxy_loc)
        logging.info("服务协议")

    # 定位个人信息进入个人信息
    def settingi(self):
        self.click_button(self.grxx_loc)
        logging.info("个人信息")

    # 定位帮助中心进入帮助中心
    def settingj(self):
        self.click_button(self.help_loc)
        logging.info("帮助中心")

    # 定位关于我们进入关于我们
    def settingk(self):
        self.click_button(self.gywm_loc)
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
