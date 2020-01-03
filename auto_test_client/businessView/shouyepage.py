#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.common.exceptions import NoSuchElementException  # 捕捉NoSuchElementException异常
import time
import yaml
import logging
import os
from selenium.webdriver.common.by import By

from auto_test_client.public.desired_caps import appium_desired
from auto_test_client.baseView.basepage import Base
from auto_test_client.businessView.loginpage import Login
from auto_test_client.utils import openYaml
from auto_test_client.public.startFunction import start_index

path = os.path.dirname(os.getcwd())
index_path = path + "/data/shouye.yaml"
data = openYaml.get_yaml_data(index_path)


class Shouye(Base):  # 首页元素
    home_loc = (By.XPATH,"//*[contains(@text,'首页')]")  # 首页入口
    mask_loc = (By.ID,'guide_know')   #蒙版ID
    close_loc = (By.ID,'close_btn')  # 窗帘广告/情感化插件关闭按钮
    more_loc = (By.NAME,"更多")  # 更多icon
    goto_login = (By.NAME,"去登录")  # 去登录提示
    login_frame = (By.ID,'com.greenpoint.android.mc10086.activity:id/tv_title')

    # 点击首页入口
    def shouye(self):
        self.click_button(self.home_loc)
        logging.info("切换到首页")

    def close_c(self):  # 窗帘广告、情感化插件
        try:
            self.click_button(self.close_loc)
            logging.info("关闭窗帘广告/情感化插件")
        except:
            pass


    # 蒙版窗口
    def check_guide_know(self):
        logging.info('========check_guide_know========')
        try:
            element = self.driver.find_element(*self.mask_loc)
        except NoSuchElementException:
            logging.info('guide_know element is not found!')
        else:
            element.click()
            logging.info('click guide_know')

    # 浮窗广告点击关闭
    def check_adBtn(self):
        logging.info('========check_adBtn========')
        try:
            element = self.driver.find_element(*self.more_loc)
        except NoSuchElementException:
            logging.info('adBtn element is not found!')
        else:
            element.click()
            logging.info('click adBtn')

    def hom_ad(self):  # 首页-》关闭弹窗广告
        self.click_button(self.close_loc)
        time.sleep(10)
        self.check_adBtn()

    def gengduo(self):  # 更多
        self.click_button(self.more_loc)

    def goto_login_Btn(self):  # 验证用户有没有登录(登录弹框)  新增，
        try:
            element = self.driver.find_element(*self.goto_login)
        except NoSuchElementException:
            logging.error('用户已登录')
        else:
            logging.info('用户未登录，现在去登录')
            element.click()
            time.sleep(4)
            login = Login(self.driver)
            login.login('18334764004')

    def login_frameBtn(self):  # 验证用户有没有登录(登录弹框)  新增
        try:
            element = self.driver.find_element(*self.login_frame)
        except NoSuchElementException:
            logging.error('用户已登录')
        else:
            logging.info('用户未登录，现在去登录')
            element.click()
            time.sleep(4)
            login = Login(self.driver)
            login.login('18334764004')

    def login_s(self):  # 新增
        login = Login(self.driver)
        login.next()
        # shouye=Shouye(self.driver)
        self.check_adBtn()


# 消息中心模块
class Message_center(Shouye):
        more_right_loc = (By.ID,'title_msg_center_img')  # 右上角更多按钮
        message_loc = (By.ID,'pop_menu_msg_center')  # 消息按钮
        order_message_loc = (By.ID,'img_order_notice')  # 订单消息
        login_button_loc = (By.ID,'tv_title')  # 拉起登录
        returns_loc = (By.ID,'login_close')  # 返回

        def more_right(self):  # 右上角更多
            self.click_button(self.more_right_loc)
            logging.info('右上角更多按钮')

        def message(self):  # 点击消息按钮
            self.click_button(self.message_loc)
            logging.info('点击消息按钮')

        def order_message(self):  # 点击订单消息
            self.click_button(self.order_message_loc)
            logging.info('点击订单消息')

        def returns(self):  # 返回
            self.click_button(self.returns_loc)
            self.back()


class License(Shouye):  # 个性化专区
    license_loc = (By.NAME,"证照信息")  # 证照信息入口
    #title_back_btn
    def license(self):  # 证照信息
        self.swipe_up(t=1000, n=5)
        time.sleep(2)
        self.click_button(self.license_loc)
        logging.info('点击证照信息')


class Recharge(Shouye):  # 充值交费
    recharge_loc= (By.NAME,"充值交费")
    title_name_txt = (By.ID,'title_name_txt')  # 充值中心页面，文字判断元素
    # 话费充值模块
    amount_loc = (By.NAME,"10元")  # 选择话费充值金额

    # 流量充值模块
    flow_loc = (By.XPATH,'//*[@text="流量"]')  # 流量
    flowamount_loc = (By.NAME,"2G")  # 流量充值额度2G
    top_up_loc = (By.NAME,"立即充值")  # 立即充值
    # 话费/流量充值模块->元素判断
    payment_loc = (By.XPATH,'//*[@text="支付宝支付"]')
    return_loc = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView')  # 返回

    # 未完成订单弹框
    later_loc = (By.NAME,"稍后再说")  # 稍后再说
    immediately_loc = (By.NAME,"立即查看")  # 立即查看

    # 电子发票
    invoice_loc = (By.NAME,"电子发票")  # 电子发票入口icon
    my_invoice_loc = (By.ID,'title_name_txt')  # 我的发票页面（文字判断）

    title_back_btn = (By.ID,'title_back_btn')  # 充值页面返回

    # 未完成订单弹框
    def later_immediatelyBtn(self):
        # logging.info('您有正在处理中的话费订单......')
        try:
            element = self.driver.find_element(*self.later_loc)
            # self.click_button(self.later_loc)
        except NoSuchElementException:
            logging.error('无未完成订单的弹框信息')
        else:
            element.click()
            logging.info('您有正在处理中的话费订单,点击稍后再说')

    def content(self):  # 充值交费入口icon
        time.sleep(3)
        self.click_button(self.content1_loc)
        time.sleep(4)
        logging.info('进入充值交费')

    def check_content(self):  # 判断充值交费跳转是否正确
        logging.info('========check_content========')
        try:
            test1 = self.driver.find_element(*self.title_name_txt).text
            logging.info(test1)
        except NoSuchElementException:
            logging.error('充值交费跳转错误')
            self.get_screenshot('充值交费跳转错误')
        else:
            logging.info('充值交费跳转正确!')
            return test1

    def invoice(self):  # 电子发票入口
        self.later_immediatelyBtn()
        time.sleep(5)
        self.click_button(self.invoice_loc)
        time.sleep(6)
        logging.info('进入电子发票页面')

    def check_invoice(self):  # 电子发票页面判断
        logging.info('========check_invoice========')
        try:
            test1 = self.driver.find_element(*self.my_invoice_loc).text
            logging.info(test1)
        except NoSuchElementException:
            logging.error('电子发票跳转错误')
            self.get_screenshot('电子发票跳转错误')
            self.back()
        else:
            logging.info('电子发票跳转正确!')
            self.back()
            return test1

    def call_charge(self):  # 话费充值流程
        self.later_immediatelyBtn()
        self.click_button(self.amount_loc)
        time.sleep(4)
        self.click_button(self.top_up_loc)
        logging.info('充值中心->话费充值')

    def flow(self):  # 流量充值流程
        self.later_immediatelyBtn()
        self.click_button(self.flow_loc)
        time.sleep(6)
        self.click_button(self.top_up_loc)
        logging.info('充值中心->流量充值')

    def return_s(self):  # 话费、流量流程返回
        time.sleep(2)
        self.click_button(self.return_loc)

    def back_btn(self):  # 返回到充值交费或首页
        self.click_button(self.title_back_btn)

class Package(Shouye):  # 套餐余量
    rackage_loc = (By.NAME,"套餐余量")  # 套餐余量入口
    title_name_txt = (By.ID,'title_name_txt')  # 套餐余量标题

    overflow_loc = (By.NAME,"流量直充")  # 流量直充
    top_up_loc = (By.NAME,"立即充值")  # 立即充值
    payment_loc = (By.XPATH,'//*[@text="支付宝支付"]')  # 支付宝支付
    Button1_loc = (By.XPATH,'//android.widget.Button')  #
    payment_login_loc = (By.NAME,"登录支付宝")  # 登录支付宝
    return_loc = (By.ID,'title_back_btn')  # 返回

    def taocan(self):
        self.click_button(self.rackage_loc)
        logging.info("进入套餐余量页面")

        # 流量直充模块

    def liuliang(self):
        # self.swipe_up(t=1000,n=1)
        self.click_button(self.overflow_loc)
        logging.info("点击流量直充，进入充值中心页面")
        liuliang = Recharge(self.driver)
        liuliang.later_immediatelyBtn()
        self.click_button(self.top_up_loc)

    def return_s(self):  # 话费、流量流程返回
        time.sleep(2)
        self.click_button(self.return_loc)

class Bill(Shouye):  # 我的账单
    bill_loc = (By.NAME,"我的账单")  # 我的账单入口
    account_loc = (By.ID,'tv_balance')  # 账户余额
    recharge_button_loc = eval(data['Bill']['gobutton_loc'])  # 去充值按钮

    def bill(self):
        self.click_button(self.bill_loc)
        logging.info('进入我的账单')

    def gobutton(self):
        self.click_button(self.recharge_button_loc)
        logging.info('点击去充值按钮')

#----------------------------------
'''
每个页面
返回：ID:title_back_btn
关闭：ID:title_close_btn
页面名称：ID：title_name_txt
'''

if __name__ == '__main__':
    driver = appium_desired('emulator-5554', 4723)
    logging.info('=====首页启动===')
    start_index(driver)
    logging.info('====index到首页===')
    # message=Message_center(driver)
    # message.more_right()
    # message.message()
    # message.order_message()
    # message.returns()
    # license=License(driver)
    # license.license()
    recharge=Recharge(driver)
    recharge.content()
    recharge.goto_login_Btn()
    recharge.call_charge()

