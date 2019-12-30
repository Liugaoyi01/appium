# 定义一个启动到首页的方法

#from auto_test_client.public.desired_caps import appium_desired,creat_process_list
from auto_test_client.baseView.basepage import Base
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auto_test_client.utils.countRunTime import run_time

privacy_service_loc = (By.ID, "cb_privacy_service")  # 勾选同意隐私
agree_btn_loc = (By.ID, "btn_agree")  # 点击同意按钮
open_btn_loc = (By.ID, "now_open_btn")  # 立即开启按钮
guide_img_loc = (By.ID, "guide_img")  # 引导图
# guide_img_loc = (By.ID, "webView")  # 引导图-5.8版本

quanxian_frame_loc = (By.ID, "dialog_container")  # 权限弹框
# quanxian_allow_loc = (By.ID, "permission_allow_button")  # 权限弹框同意按钮
quanxian_allow_loc = (By.XPATH, "//*[@text='允许']")  # 权限弹框同意按钮
# index_text_loc = (By.XPATH, "//*[contains(@text,'首页')]")

index_text_loc = (By.ID, "mallwebview") # 首页检测元素


@run_time
def start_index(driver):
    privacy_check(driver)  # 同意隐私协议
    always_allow(driver, number=1)  # 权限检测，并同意
    # try:
    #     logging.info("检查是否出现授权弹框")
    #     frame_ele = base.find_element(quanxian_frame_loc)
    #     while frame_ele:
    #         # WebDriverWait(driver, 1000).until(
    #         #     EC.element_to_be_clickable(quanxian_allow_loc)
    #         # )
    #         base.click_button(quanxian_allow_loc)
    #         logging.info("点击允许授权")
    #
    #     # logging.info("没有定位到，需要手动点击")
    #     # time.sleep(5)
    # except:
    #
    #     logging.info("没有出现授权阶段，无需授权")

    # try:
    #     button = self.driver.find_element_by_id('app_startPage_skip')
    # except NoSuchElementException:
    #     logging.info("无跳过button")
    # else:
    #     button.click()
    guide_swift(driver, number=4)  # 引导页滑动
    check_update(driver)  # 检查更新
    index_check(driver)  # 检查是否启动到首页


@run_time
def privacy_check(driver):
    try:
        e = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(privacy_service_loc)
        )
        e.click()
        logging.info("勾选隐私协议")
        agree_ele = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(agree_btn_loc)
        )
        agree_ele.click()
        logging.info("点击同意开启按钮")
    except:
        logging.info("无需同意隐私协议")


@run_time
def always_allow(driver, number=5):
    '''
    function:权限弹窗-允许
    args:1.传driver
    2.number，判断弹窗次数，默认给5次
    其它：
    WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
    '''
    for i in range(number):
        quanxian_allow_loc = (By.XPATH, "//*[@text='允许']")
        # quanxian_allow_loc = (By.ID, "permission_allow_button")
        try:
            e = WebDriverWait(driver, 1).until(EC.presence_of_element_located(quanxian_allow_loc))
            e.click()
        except:
            logging.info("没有出现授权阶段，无需授权,跳出循环")
            break


@run_time
def guide_swift(driver, number=4):
    base = Base(driver)
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(guide_img_loc)
        )
        logging.info("进入引导页面")
        base.swipe_left(t=1500, n=number)
        logging.info("左滑到开启页面")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(open_btn_loc)
        )
    except:
        pass
    else:
        base.click_button(open_btn_loc)
        logging.info('点击立即开启进入首页')


@run_time
def check_update(driver):
    update_later_loc = (By.ID, "dialog_btn1 ")

    try:
        e = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(update_later_loc)
        )
        e.click()
        logging.info("检测更新弹窗，点击以后再说")
    except:
        logging.info("无需更新")


@run_time
def index_check(driver):
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(index_text_loc)
        )
        logging.info('客户端启动成功，已进入首页')
    except:
        logging.error('检测未进入首页')


if __name__ == '__main__':

    # driver = appium_desired('P79LPJUO9DM7PZF6', 4723)

    # start_index(driver)
    desired_process = creat_process_list()
    # appium_desired('P79LPJUO9DM7PZF6', 4723)
