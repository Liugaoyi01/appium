# -*- coding:utf-8 -*-
import sys
import os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import yaml
from PO import loginpage
from PO import basepage
from PO.desired_caps import appium_desired
import time
import logging

driver = appium_desired()
import pytest


def setup_module():
    base = loginpage.Login(driver)
    base.start()


def teardown_module():
    driver.close_app()


class TestLogin():

    def teardown(self):  # 每个用例结束返回
        login = loginpage.Login(driver)
        login.close()

    def test_logonbutton(self):  # 我的页面判断有登录按钮
        denglu = loginpage.Login(driver)
        denglu.wode()
        try:
            assert denglu.try_find(loginpage.Login.denglu_loc) is True
            logging.info("登录按钮")
        except:
            logging.warning("未找到登录按钮")
            denglu.get_screenshot("登录按钮")
            raise

    def test_automaticlogon(self):  # 判断登录页面有自动登录
        login = loginpage.Login(driver)
        login.denglu()
        try:
            assert login.try_find(loginpage.Login.zddl_loc) is True
            logging.info("自动登录")
        except:
            logging.warning("未找到自动登录按钮")
            login.get_screenshot("自动登录按钮")
            raise

    def test_contacts(self):  # 判断登录页面有联系人
        login = loginpage.Login(driver)
        login.denglu()
        try:
            assert login.try_find(loginpage.Login.lxr_loc) is True
            logging.info("联系人")
        except:
            logging.warning("未找到联系人按钮")
            login.get_screenshot("联系人按钮")
            raise

    def test_delete(self):  # 判断输入账号有删除按钮
        login = loginpage.Login(driver)
        login.denglu()
        login.zhanghao('13715307043')
        try:
            assert login.try_find(loginpage.Login.scan_loc) is True
            logging.info("删除按钮")
        except:
            logging.warning("未找到删除按钮")
            login.get_screenshot("删除按钮")
            raise

    def test_verificationcode(self):  # 判断输入账号可以点击验证码
        login = loginpage.Login(driver)
        login.denglu()
        login.zhanghao("13715307043")
        try:
            assert login.try_find(loginpage.Login.yanzheng_loc) is True
            logging.info("不能输入验证码")
        except:
            logging.warning("不能输入验证码")
            login.get_screenshot("不能输入验证码")
            raise

    def test_entercontacts(self):  # 判断进入联系人成功
        login = loginpage.Login(driver)
        login.denglu()
        login.lxr()
        try:
            assert login.try_find(loginpage.Login.search_loc) is True
            login.L_back()
            logging.info("联系人进入")
        except:
            logging.warning("联系人进入")
            login.get_screenshot("联系人进入失败")
            raise

    def test_suslogin(self):  # 判断登录成功
        login = loginpage.Login(driver)
        login.denglu()
        login.login("15012761017")
        try:
            assert login.try_find(loginpage.Login.wode_loc) is True
            logging.info("登录失败")
        except:
            logging.warning("登录失败")
            login.get_screenshot("登录失败")
            raise


if __name__ == "__main__":
    pytest.main(["s", "denglu_test.py"])
