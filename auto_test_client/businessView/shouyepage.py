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
    home_loc = (By.XPATH, "//*[contains(@text,'首页')]")  # 首页入口
    mask_loc = (By.ID, 'guide_know')  # 蒙版ID
    close_loc = (By.ID, 'close_btn')  # 窗帘广告/情感化插件关闭按钮
    more_loc = (By.NAME, "更多")  # 更多icon
    goto_login = (By.NAME, "去登录")  # 去登录提示
    login_frame = (By.ID, 'com.greenpoint.android.mc10086.activity:id/tv_title')
    dishi_loc = (By.ID, 'title_city_arrow_img')  # 地市入口
    search_loc = (By.ID, 'img_search')  # 搜索入口
    yuyin_loc = (By.ID, 'img_voice_search')  # 语音搜索入口
    scan_loc = (By.NAME, '扫一扫')  # 扫一扫入口
    content1_loc = (By.NAME, "充值交费")  # 充值交费入口
    taocan_loc = (By.NAME, "套餐余量")  # 套餐余量入口
    liuliang_loc = (By.NAME, "流量管家")  # 流量管家入口
    bill_loc = (By.NAME, "我的账单")  # 我的账单入口
    points_loc = (By.NAME, "积分商城")  # 积分商城入口
    title_loc = (By.ID, 'title_name_txt')  # 页面标题
    guide_know = (By.ID, 'guide_know')
    c_close_loc = (By.ID, 'close_btn')  # 窗帘广告/情感化插件关闭按钮
    weiyu_loc = (By.ID, "uighur_img")  # 维语版入口
    qinggan_loc = (By.ID, "drag_img")  # 情感化插件
    xinyong_loc = (
    By.XPATH, '//android.webkit.WebView[@content-desc="中国移动手机营业厅首页"]/android.view.View[18]/android.widget.Image')
    jingxi_loc = (By.NAME, "点击有惊喜")  # 信用分点击有惊喜
    liaojie_loc = (By.NAME, "了解信用分")  # 了解信用分
    huanyi_loc = (By.NAME, "换一批")  # 猜你喜欢换一批
    gengduo_loc = (By.NAME, "更多")  # 更多icon
    beijin_loc = (By.ID, 'title_city_name_txt')  # 默认定位
    upper_right_loc = (By.ID, 'title_msg_center_img')  # 右上角更多按钮
    xiaoxi_loc = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.TextView')  # 消息按钮
    dingdanxi_loc = (By.ID, 'img_order_notice')  # 订单消息
    denglu_loc = (By.ID, 'tv_title')  # 拉起登录  # 拉起登录
    fanhui_loc = (By.ID, 'login_close')  # 返回


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

    def jingxi(self):
        self.click_button(self.jingxi_loc)
        logging.info("点击和信用分入口")

    # 建议：最好使用try-except提高及健壮性，参考check_guide_know

    def huan(self):
        self.click_button(self.huanyi_loc)
        logging.info("点击换一批")

    # 消息中心模块
    def upper_right(self):  # 右上角更多
        self.click_button(self.upper_right_loc)
        logging.info('右上角更多按钮')

    def xiaoxi(self):  # 点击消息按钮
        self.click_button(self.xiaoxi_loc)
        logging.info('点击消息按钮')

    def dingdanxi(self):  # 点击订单消息
        self.click_button(self.dingdanxi_loc)
        logging.info('点击订单消息')

    def fanhui(self):  # 返回
        self.click_button(self.fanhui_loc)


# 消息中心模块
class Message_center(Shouye):
    more_right_loc = (By.ID, 'title_msg_center_img')  # 右上角更多按钮
    message_loc = (By.ID, 'pop_menu_msg_center')  # 消息按钮
    order_message_loc = (By.ID, 'img_order_notice')  # 订单消息
    login_button_loc = (By.ID, 'tv_title')  # 拉起登录
    returns_loc = (By.ID, 'login_close')  # 返回

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
    license_loc = (By.NAME, "证照信息")  # 证照信息入口

    # title_back_btn
    def license(self):  # 证照信息
        self.swipe_up(t=1000, n=5)
        time.sleep(2)
        self.click_button(self.license_loc)
        logging.info('点击证照信息')


class Recharge(Shouye):  # 充值交费
    recharge_loc = (By.NAME, "充值交费")
    title_name_txt = (By.ID, 'title_name_txt')  # 充值中心页面，文字判断元素
    # 话费充值模块
    amount_loc = (By.NAME, "10元")  # 选择话费充值金额

    # 流量充值模块
    flow_loc = (By.XPATH, '//*[@text="流量"]')  # 流量
    flowamount_loc = (By.NAME, "2G")  # 流量充值额度2G
    top_up_loc = (By.NAME, "立即充值")  # 立即充值
    # 话费/流量充值模块->元素判断
    payment_loc = (By.XPATH, '//*[@text="支付宝支付"]')
    return_loc = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView')  # 返回

    # 未完成订单弹框
    later_loc = (By.NAME, "稍后再说")  # 稍后再说
    immediately_loc = (By.NAME, "立即查看")  # 立即查看

    # 电子发票
    invoice_loc = (By.NAME, "电子发票")  # 电子发票入口icon
    my_invoice_loc = (By.ID, 'title_name_txt')  # 我的发票页面（文字判断）

    title_back_btn = (By.ID, 'title_back_btn')  # 充值页面返回

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
    rackage_loc = (By.NAME, "套餐余量")  # 套餐余量入口
    title_name_txt = (By.ID, 'title_name_txt')  # 套餐余量标题

    overflow_loc = (By.NAME, "流量直充")  # 流量直充
    top_up_loc = (By.NAME, "立即充值")  # 立即充值
    payment_loc = (By.XPATH, '//*[@text="支付宝支付"]')  # 支付宝支付
    Button1_loc = (By.XPATH, '//android.widget.Button')  #
    payment_login_loc = (By.NAME, "登录支付宝")  # 登录支付宝
    return_loc = (By.ID, 'title_back_btn')  # 返回

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
    bill_loc = (By.NAME, "我的账单")  # 我的账单入口
    account_loc = (By.ID, 'tv_balance')  # 账户余额
    recharge_button_loc = eval(data['Bill']['gobutton_loc'])  # 去充值按钮

    def bill(self):
        self.click_button(self.bill_loc)
        logging.info('进入我的账单')

    def gobutton(self):
        self.click_button(self.recharge_button_loc)
        logging.info('点击去充值按钮')


class Cities(Shouye):  # 省市选择
    c_search_loc = (By.ID, 'citychoose_searchcontent_edt')  # 地市选择搜索框
    c_choose_loc = (By.ID, 'tv_name')  # 搜索结果省市选择
    city_loc = (By.ID, 'title_city_name_txt')  # 页面当前城市,文本

    def dishi(self):  # 点击地市入口
        self.click_button(self.dishi_loc)
        logging.info('点击省市选择')

    def search(self, city):  # 输入搜索省市
        self.send_keys(self.c_search_loc, city)
        logging.info('输入搜索省市')

    def choose(self):  # 选择搜索结果
        self.click_button(self.c_choose_loc)
        logging.info('选择搜索结果')

    def qiehuan(self, sheng, shi):
        # self.dishi()
        # print("进入地市选择")
        self.search(sheng)
        logging.info('搜索省份：%s' % (sheng))
        self.choose()
        logging.info("选择省份")
        self.search(shi)
        logging.info('搜索地市：%s' % (shi))
        self.choose()
        logging.info("选择地市")


class Search(Shouye):  # 搜索
    box_loc = (By.XPATH, '//android.webkit.WebView[@content-desc="搜索"]/android.widget.EditText')  # 搜索框
    t_search_loc = (By.XPATH, '//android.widget.Button[@content-desc="搜索"]')  # 搜索按钮
    s_choose_loc = (By.NAME, "增值业务")  # 选择流量直充
    resou_loc = (By.NAME, "热搜")  # 热搜标题
    tuijian_loc = (By.NAME, "未找到相关结果")  # 搜索无结果推荐
    neirong_loc = (By.NAME, "5G看移动")  # 热搜内容
    lishi_loc = (By.NAME, "历史搜索")  # 搜索历史
    yuyin_s_loc = (By.NAME, "开始语音搜索")  # 开始语音搜索
    yuyin_m_loc = (By.NAME, "普通话")  # 语音搜索默认普通话
    yuyin_c_loc = (By.ID, "btn_voice_close")  # 语音搜索关闭

    def search(self):  # 点击搜索入口
        self.click_button(self.search_loc)
        logging.info("点击搜索入口")

    def yuyin(self):  # 点击语音搜索入口
        self.click_button(self.yuyin_loc)
        logging.info("点击语音搜索入口")

    def yuyin_c(self):  # 点击搜索关闭
        self.click_button(self.yuyin_c_loc)
        logging.info("点击语音搜索关闭")

    def chazhao(self, value):  # 搜索流程
        self.send_keys(self.box_loc, value)
        logging.info("输入搜索内容")
        self.tap(942, 320)
        logging.info("点击搜索按钮")

    def choose(self):  # 搜索结果选择
        self.click_button(self.s_choose_loc)
        logging.info("搜索结果选择")

    def neirong(self):  # 点击热搜内容
        self.click_button(self.neirong_loc)
        logging.info("5G看移动")


class Card(Base):  # 卡片码表
    # 未登录
    look_loc = (By.NAME, "登录查看")  # 登录查看
    tishi_loc = (By.NAME, "Hi，欢迎您，请登录")  # 未登录提示语
    liuliang_loc = (By.NAME, "通用流量剩余")  # 流量剩余
    huafei_loc = (By.NAME, "话费余额")  # 话费余额
    yue_loc = (By.NAME, "您的账户总余额")  # 账户总余额
    keyong_loc = (By.ID, 'txt_use_balance_title')  # 话费可用余额
    yuyin_loc = (By.NAME, "语音剩余")  # 语言剩余
    shengyu_loc = (By.NAME, "您的语音剩余")  # 您的语音剩余
    fenxiang_loc = (By.ID, 'title_share_btn')  # 分享按钮
    gobutton_loc = (By.NAME, '去充值')  # 语音去充值按钮
    gopay_loc = (By.ID, 'txt_gopay')  # 话费去充值按钮
    jine_loc = (By.ID, "--元")  # 未登录话费余额
    taocan_loc = (By.NAME, "套餐余量")  # 套餐余量icon
    banli_loc = (By.NAME, "套餐办理")  # 套餐办理icon
    feixiang_loc = (By.NAME, "4G飞享套餐")  # 4G分享套餐
    zhangdan_loc = (By.NAME, "我的账单")  # 我的账单icon
    zonge_loc = (By.ID, "tv_bill_all")  # 本期账单总额

    # 登录查看
    def look(self):
        self.click_button(self.look_loc)
        logging.info("点击登录查看")

    # 点击通用流量已用
    def liuliang(self):
        self.click_button(self.liuliang_loc)
        logging.info("点击通用流量已用")

    # 点击话费余额
    def huafei(self):
        self.click_button(self.huafei_loc)
        logging.info("点击话费余额")

    # 点击语音剩余
    def yuyin(self):
        self.click_button(self.yuyin_loc)
        logging.info("点击语音剩余")

    # 点击语音查询去充值
    def gobutton(self):
        self.click_button(self.gobutton_loc)
        logging.info("点击语音去充值")

    # 点击语音查询去充值
    def gopay(self):
        self.click_button(self.gopay_loc)
        logging.info("点击话费去充值")

    def taocan(self):
        self.click_button(self.taocan_loc)
        logging.info("点击套餐余量")

    def banli(self):
        self.click_button(self.banli_loc)
        logging.info("点击套餐业务")

    def zhangdan(self):
        self.click_button(self.zhangdan_loc)
        logging.info("点击我的账单")


class Scan(Shouye):  # 扫一扫
    pic_loc = (By.ID, 'title_share_btn')  # 本地图片按钮
    tishi_loc = (By.ID, 'message')  # 扫码结果提示语
    zhidao_loc = (By.ID, 'dialog_btn2')  # 知道了

    def scan(self):
        self.click_button(self.upper_right_loc)
        logging.info("点击右上角菜单选择")
        self.click_button(self.scan_loc)
        logging.info("点击扫一扫入口")

    def pic(self):
        self.click_button(self.pic_loc)
        logging.info("点击本地图片选择")
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        self.tap((230 / 1080) * X, (302 / 1920) * Y)  # (239, 314)
        logging.info("点击第一张图片")

    def zhidao(self):
        self.click_button(self.zhidao_loc)
        logging.info("点击知道了")


class Traffic(Shouye):  # 流量管家
    fenxiang_loc = (By.ID, 'title_share_btn')  # 分享按钮
    kuaizhao_loc = (By.NAME, "微信快照")  # 微信快照
    quxiao_loc = (By.ID, 'btn_cancel')  # 分享取消
    zhankai_loc = (By.NAME, "展开")  # 流量明细展开
    shouqi_loc = (By.NAME, "收起")  # 流量明细收起
    dingdan_loc = (By.NAME, "流量订单")  # 流量订单icon
    chongzhi_loc = (By.NAME, "充值订单")  # 跳转我的订单
    jingwai_loc = (By.NAME, "境外流量")  # 境外流量
    shangpin_loc = (By.NAME, "流量商品")  # 流量商品icon
    xiangdan_loc = (By.NAME, "流量详单")  # 流量详单icon
    shenfen_loc = (By.NAME, "身份认证")  # 身份认证
    bugouyong_loc = (By.NAME, "流量不够用")  # 流量不够用title
    yongbuwan_loc = (By.NAME, "流量用不完")  # 流量用不完title

    def liuliang(self):
        self.click_button(self.liuliang_loc)
        logging.info("点击流量管家")

    def fenxiang(self):
        self.click_button(self.fenxiang_loc)
        logging.info("点击分享按钮")

    def quxiao(self):
        self.click_button(self.quxiao_loc)
        logging.info("点击分享取消")

    def dingdan(self):
        self.click_button(self.dingdan_loc)
        logging.info("点击流量订单")

    def jingwai(self):
        self.click_button(self.jingwai_loc)
        logging.info("点击境外流量")

    def shangpin(self):
        self.click_button(self.shangpin_loc)
        logging.info("点击流量商品")

    def xiangdan(self):
        self.click_button(self.xiangdan_loc)
        logging.info("点击流量详单")


class Jifen(Shouye):  # 积分商城
    duihuan_loc = (By.NAME, "兑换排行")  # 兑换排行入口
    lishi_loc = (By.NAME, "历史排行")  # 历史排行tab
    year_loc = (By.NAME, "年排行")  # 年排行tab
    firs_loc = (By.NAME, "1")  # 第一位商品
    liji_loc = (By.NAME, "立即兑换")  # 立即兑换按钮
    sure_loc = (By.NAME, "确定兑换")  # 确定兑换按钮
    shop_loc = (By.NAME, "购物车")  # 我的账户页购物车入口
    goshop_loc = (By.NAME, "去购物")  # 购物车空时去购物按钮
    shoucang_loc = (By.NAME, "加入收藏")  # 左滑加入收藏
    delete_loc = (By.NAME, "删除")  # 左滑删除
    gift_loc = (By.NAME, "礼品分类")  # 礼品分类入口
    shuzi_loc = (By.NAME, "数字生活")  # 数字生活标题栏
    shiting_loc = (By.NAME, "视听")  # 视听模块入口
    shi_title_loc = (By.ID, 'title_name_txt')  # 视听页标题
    candui_loc = (By.NAME, "我能兑换")  # 我能兑换入口
    account_loc = (By.NAME, "我的账户")  # 我的账户入口
    jifen_loc = (By.NAME, "可用积分：")  # 我的账户页登录后字段

    def points(self):  # 点击积分商城入口
        self.click_button(self.points_loc)
        logging.info('点击积分商城')

    def account(self):  # 点击我的账户入口
        self.click_button(self.account_loc)
        logging.info("点击我的账户")

    def shop(self):  # 点击购物车入口
        self.click_button(self.shop_loc)
        logging.info("点击购物车入口")

    def gift(self):  # 礼品分类兑换
        self.click_button(self.gift_loc)
        logging.info("点击礼品分类入口")
        self.click_button(self.shuzi_loc)
        logging.info("切换数字生活标题栏")
        self.click_button(self.shiting_loc)
        logging.info("点击视听模块入口")

    def duihuan(self):  # 点击兑换排行榜
        self.click_button(self.duihuan_loc)
        logging.info('点击兑换排行榜')

    def firs(self):  # 点击第一个商品
        self.click_button(self.firs_loc)
        logging.info('点击第一个商品')

    def liji(self):  # 点击立即兑换
        self.click_button(self.liji_loc)
        logging.info('点击立即兑换')

    def sure(self):  # 点击确认兑换
        self.click_button(self.sure_loc)
        logging.info('点击确认兑换')

    def jifen(self):  # 积分兑换流程
        time.sleep(3)
        self.duihuan()
        logging.info("进入兑换排行榜")
        time.sleep(3)
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        self.tap((147 / 1080) * X, (446 / 1920) * Y)
        logging.info("点击第一个商品")
        self.liji()
        logging.info("点击立即兑换")
        self.tap((536 / 1080) * X, (1845 / 1920) * Y)
        logging.info("点击确认按钮")


# ----------------------------------
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
    recharge = Recharge(driver)
    recharge.content()
    recharge.goto_login_Btn()
    recharge.call_charge()
