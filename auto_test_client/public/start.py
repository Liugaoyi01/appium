# 定义一个启动到首页的方法

from auto_test_client.public.desired_caps import appium_desired
from auto_test_client.baseView.basepage import Base
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start_index(driver):
    base = Base(driver)
    '''
        勾选元素
            class  android.widget.CheckBox
            id   com.greenpoint.android.mc10086.activity:id/cb_privacy_service
        点击同意
            id  com.greenpoint.android.mc10086.activity:id/btn_agree
            class   android.widget.Button
        权限弹框同意按钮
            id  com.android.packageinstaller:id/permission_allow_button
            class   android.widget.Button
            拒绝
             id   permission_deny_button
        权限元素
            id/dialog_container
        引导图
            id guide_img
        滑动完之后的立即开启按钮
            id  com.greenpoint.android.mc10086.activity:id/now_open_btn
        

    '''
    privacy_service_loc = (By.ID, "cb_privacy_service")  # 勾选同意隐私
    agree_btn_loc = (By.ID, "btn_agree")  # 点击同意按钮
    open_btn_loc = (By.ID, "now_open_btn")  # 立即开启按钮
    guide_img_loc = (By.ID, "guide_img")  # 引导图
    quanxian_frame_loc = (By.ID, "dialog_container")  # 权限弹框
    # quanxian_allow_loc = (By.ID, "permission_allow_button")  # 权限弹框同意按钮
    quanxian_allow_loc = (By.XPATH, "//*[@text='允许']")  # 权限弹框同意按钮
    index_text_loc = (By.XPATH, "//*[contains(@text,'首页')]")

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(privacy_service_loc)
    )
    base.click_button(privacy_service_loc)
    logging.info("勾选隐私协议")
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(agree_btn_loc)
    )
    base.click_button(agree_btn_loc)
    logging.info("点击同意开启按钮")
    try:
        always_allow(driver, number=3)
    except:
        logging.info("没有出现授权阶段，无需授权")
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
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(guide_img_loc)
    )
    logging.info("进入引导页面")
    base.swipe_left(t=1500, n=4)
    logging.info("左滑到开启页面")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(open_btn_loc)
    )
    base.click_button(open_btn_loc)
    logging.info('点击立即开启进入首页')
    # try:
    #     button = self.driver.find_element_by_id('app_startPage_skip')
    # except NoSuchElementException:
    #     logging.info("无跳过button")
    # else:
    #     button.click()
    '''
        此处还需新增是否更新检测 
    '''
    check_update()
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(index_text_loc)
        )
        logging.info('客户端启动成功，已进入首页')
    except:
        logging.error('检测未进入首页')


def always_allow(driver, number=5):
    '''
    function:权限弹窗-允许
    args:1.传driver
    2.number，判断弹窗次数，默认给5次
    其它：
    WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
    '''
    for i in range(number):
        # quanxian_allow_loc = (By.XPATH, "//*[@text='允许']")
        quanxian_allow_loc = (By.ID, "permission_allow_button")
        try:
            e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(quanxian_allow_loc))
            e.click()
        except:
            pass
def check_update():
    pass

if __name__ == '__main__':
    driver = appium_desired('HB6CE1RPL002YU', 4723)

    start_index(driver)
