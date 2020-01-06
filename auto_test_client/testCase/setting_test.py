# -*- coding:utf-8 -*-
import sys
import os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import yaml
from auto_test_client.businessView import setting
from auto_test_client.baseView import basepage
from auto_test_client.public.desired_caps import appium_desired
import time
import logging
from auto_test_client.testCase.denglu_test import driver

# driver = appium_desired()
import pytest


def setup_module():
    base = setting.Settings(driver)
    base.start()
    time.sleep(3)
    #base.tap(970,1850)
    base.wode()


def teardown_module():
    driver.close_app()


class TestLogin():
    def setup(self):
        shezhi = setting.Settings(driver)
        shezhi.settings()

    def teardown(self):  # 每个用例结束返回
        shezhi = setting.Settings(driver)
        shezhi.back()
        def test_001(self):  # 我的页面判断有设置按钮
            shezhi = setting.Settings(driver)
            try:
                assert shezhi.try_find(setting.Settings.settings_loc) is True
                logging.info("设置按钮")
            except:
                logging.warning("未找到登录按钮")
                shezhi.get_screenshot("登录按钮")
                raise


    def test_loginsetting(self): # 设置页面登录设置跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settinga()
        try:
            assert shezhi.try_find(setting.Settings.automatic_loc) is True
            logging.info("登录设置")
        except:
            logging.warning("未找到登录设置")
            shezhi.get_screenshot("登录设置")
            raise
        finally:
            shezhi.back()


    def test_messagepush(self):  # 设置页面消息推送跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settingb()
        try:
            assert shezhi.try_find(setting.Settings.pushed_loc) is True
            logging.info("消息推送")
        except:
            logging.warning("未找到消息推送")
            shezhi.get_screenshot("消息推送")
            raise
        finally:
            shezhi.back()

    def test_notice(self):  # 设置页面常驻通知栏跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settingc()
        try:
            assert shezhi.try_find(setting.Settings.switch_loc) is True
            logging.info("常驻通知栏")
        except:
            logging.warning("未找到常驻通知栏")
            shezhi.get_screenshot("常驻通知栏")
            raise
        finally:
            shezhi.back()

    def test_wlan(self):  # 设置页面WLAN跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settingd()
        try:
            assert shezhi.try_find(setting.Settings.head_loc) is True
            logging.info("wlan设置")
        except:
            logging.warning("未找到WLAN设置")
            shezhi.get_screenshot("wlan设置")
            raise
        finally:
            shezhi.back()

    def test_accountbinding(self):  # 设置页面账号绑定跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settinge()
        try:
            assert shezhi.try_text(setting.Settings.title_loc) == "第三方账号绑定"
            logging.info("账号绑定")
        except:
            logging.warning("未找到账号设置")
            shezhi.get_screenshot("账号设置")
            raise
        finally:
            shezhi.back()

    def test_bindingcontacts(self):  # 设置页面绑定联系人跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settingf()
        try:
            assert shezhi.try_find(setting.Settings. save_button_loc) is True
            logging.info("绑定联系人")
        except:
            logging.warning("未找到联系人")
            shezhi.get_screenshot("绑定联系人")
            raise
        finally:
            shezhi.queren()

    def test_cache(self):  # 设置页面清除缓存跳转正常
        shezhi = setting.Settings(driver)
        try:
            assert shezhi.try_find(setting.Settings. remove_loc) is True
            logging.info("清除缓存")
        except:
            logging.warning("未找到清除缓存")
            shezhi.get_screenshot("清除缓存")
            raise
        finally:
            shezhi.back()

    # def test_009(self):  # 设置页面服务协议跳转正常
    #     shezhi = setting.Settings(driver)
    #     shezhi.settingh()
    #     try:
    #         assert shezhi.try_text(setting.Settings.title_loc) =="服务协议"
    #         logging.info("服务协议")
    #     except:
    #         logging.warning("未找到服务协议")
    #         shezhi.get_screenshot("服务协议")
    #         raise
    #     finally:
    #         shezhi.back()

    def test_information(self):  # 设置页面个人信息跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settingi()
        try:
            assert shezhi.try_find(setting.Settings.personal_inf_loc) is True
            logging.info("个人信息")
        except:
            logging.warning("未找到个人信息保护")
            shezhi.get_screenshot("个人信息")
            raise
        finally:
            shezhi.back()

    def test_helpcenter(self):  # 设置页面帮助中心跳转正常
        shezhi = setting.Settings(driver)
        shezhi.settingj()
        try:
            assert shezhi.try_find(setting.Settings.help_internal_loc) is True
            logging.info("帮助中心")
        except:
            logging.warning("未找到帮助中心")
            shezhi.get_screenshot("帮助中心")
            raise
        finally:
            shezhi.back()

    def test_aboutus(self):  # 设置页面关于我们跳转正常
        shezhi = setting.Settings(driver)
        shezhi.swipe_up(t=1000,n=1)
        logging.info("向上滑动")
        shezhi.settingk()
        try:
            assert shezhi.try_find(setting.Settings.about_who_loc) is True
            logging.info("关于我们")
        except:
            logging.warning("未找到关于我们")
            shezhi.get_screenshot("关于我们")
            raise
        finally:
            shezhi.back()

    def test_logonbutton(self):  # 设置页面登录按钮跳转正常
        shezhi = setting.Settings(driver)
        shezhi.swipe_up(t=1000,n=1)
        logging.info("向上滑动")
        shezhi.settingl()


        try:
            assert shezhi.try_find(setting.Settings.login_loc) is True
            logging.info("登录按钮")
        except:
            logging.warning("未找到登录按钮")
            shezhi.get_screenshot("登录按钮")
            raise
        finally:
            shezhi.l_close()


if __name__ == "__main__":
    pytest.main(["s", "setting_test.py"])
