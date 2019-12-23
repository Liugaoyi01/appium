#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from PO.desired_caps import appium_desired
from PO.basepage import Base
from PO.loginpage import Login
from selenium.common.exceptions import NoSuchElementException  # 捕捉NoSuchElementException异常
import time
import yaml
import logging

with open('..\Yaml\shouye.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file)


class Shouye(Base):  # 首页元素
    shouye_loc = eval(data['Shouye']['shouye_loc'])  # 首页入口
    dishi_loc = eval(data['Shouye']['dishi_loc'])  # 地市入口
    search_loc = eval(data['Shouye']['search_loc'])  # 搜索入口
    yuyin_loc = eval(data['Shouye']['yuyin_loc'])  #语音搜索入口
    scan_loc = eval(data['Shouye']['scan_loc'])  # 扫一扫入口
    content1_loc = eval(data['Shouye']['content1_loc'])  # 充值交费入口
    taocan_loc = eval(data['Shouye']['taocan_loc'])  # 套餐余量入口
    liuliang_loc = eval(data['Shouye']['liuliang_loc'])  # 流量管家入口
    bill_loc = eval(data['Shouye']['bill_loc'])  # 我的账单入口
    points_loc = eval(data['Shouye']['points_loc'])  # 积分商城入口
    title_loc = eval(data['Shouye']['title_loc'])  # 页面标题
    guide_know = eval(data['Shouye']['guide_know'])
    c_close_loc = eval(data['Shouye']['c_close_loc'])  # 窗帘广告/情感化插件关闭按钮
    weiyu_loc = eval(data['Shouye']['weiyu_loc'])  # 维语版入口
    qinggan_loc = eval(data['Shouye']['qinggan_loc'])  # 情感化插件
    xinyong_loc = eval(data['Shouye']['xinyong_loc'])  # 和信用分图标入口
    jingxi_loc = eval(data['Shouye']['jingxi_loc'])  # 信用分点击有惊喜
    liaojie_loc = eval(data['Shouye']['liaojie_loc'])  #了解信用分
    huanyi_loc = eval(data['Shouye']['huanyi_loc'])  # 猜你喜欢换一批
    gengduo_loc = eval(data['Shouye']['gengduo_loc'])  # 更多icon
    beijin_loc = eval(data['Shouye']['beijin_loc'])  #默认定位
    upper_right_loc = eval(data['Shouye']['upper_right_loc'])  #右上角更多按钮
    xiaoxi_loc = eval(data['Shouye']['xiaoxi_loc']) #消息按钮
    dingdanxi_loc = eval(data['Shouye']['dingdanxi_loc'])  #订单消息
    denglu_loc = eval(data['Shouye']['denglu_loc'])  #拉起登录
    fanhui_loc = eval(data['Shouye']['fanhui_loc'])  #返回

    # shangping1_loc = eval(data['Shouye']['shangping1_loc'])  #买手机-》第一个商品icon
    # shangping2_loc = eval(data['Shouye']['shangping2_loc'])
    # kuandai_loc = eval(data['Shouye']['kuandai_loc'])  #宽带专区入口
    # zhineng_jiaju_loc = eval(data['Shouye']['zhineng_jiaju_loc'])  #智能家居入口
    # zhengzhao_loc = eval(data['Shouye']['zhengzhao_loc'])  #证照信息入口
    goto_login=eval(data['Shouye']['goto_login'])#去登录提示
    login_frame=eval(data['Shouye']['login_frame'])

    # 点击首页入口
    def shouye(self):
        self.click_button(self.shouye_loc)
        logging.info("切换到首页")

    def close_c(self):  # 窗帘广告、情感化插件
        try:
            self.click_button(self.c_close_loc)
            logging.info("关闭窗帘广告/情感化插件")
        except:
            pass

    def jingxi(self):
        self.click_button(self.jingxi_loc)
        logging.info("点击和信用分入口")

    def huan(self):
        self.click_button(self.huanyi_loc)
        logging.info("点击换一批")

    #蒙版窗口
    def check_guide_know(self):
        logging.info('========check_guide_know========')
        try:
            element = self.driver.find_element(*self.guide_know)
        except NoSuchElementException:
            logging.info('adBtn element is not found!')
        else:
            element.click()
            logging.info('click adBtn')

    # 浮窗广告点击关闭
    def check_adBtn(self):
        logging.info('========check_adBtn========')
        try:
            element = self.driver.find_element(*self.c_close_loc)
        except NoSuchElementException:
            logging.info('adBtn element is not found!')
        else:
            element.click()
            logging.info('click adBtn')

    def hom_ad(self):  # 首页-》关闭弹窗广告
        self.click_button(self.shouye_loc)
        time.sleep(10)
        self.check_adBtn()

    def gengduo(self):  # 更多
        self.click_button(self.gengduo_loc)

    def goto_login_Btn(self):  #验证用户有没有登录(登录弹框)  新增
        try:
            element = self.driver.find_element(*self.goto_login)
        except NoSuchElementException:
            logging.error('用户已登录')
        else:
            logging.info('用户未登录，现在去登录')
            element.click()
            time.sleep(4)
            login=Login(self.driver)
            login.login('15838110562')

    def login_frameBtn(self):  #验证用户有没有登录(登录弹框)  新增
        try:
            element = self.driver.find_element(*self.login_frame)
        except NoSuchElementException:
            logging.error('用户已登录')
        else:
            logging.info('用户未登录，现在去登录')
            element.click()
            time.sleep(4)
            login=Login(self.driver)
            login.login('15838110562')


    def login_s(self):  #新增
        login=Login(self.driver)
        login.next()
        # shouye=Shouye(self.driver)
        self.check_adBtn()

#消息中心模块
    def upper_right(self): #右上角更多
        self.click_button(self.upper_right_loc)
        logging.info('右上角更多按钮')

    def xiaoxi(self):  #点击消息按钮
        self.click_button(self.xiaoxi_loc)
        logging.info('点击消息按钮')

    def dingdanxi(self): #点击订单消息
        self.click_button(self.dingdanxi_loc)
        logging.info('点击订单消息')

    def fanhui(self): #返回
        self.click_button(self.fanhui_loc)

class Personalized(Shouye):  #个性化专区
    shangping1_loc = eval(data['Personalized']['shangping1_loc'])  #买手机-》第一个商品icon
    shangping2_loc = eval(data['Personalized']['shangping2_loc'])
    kuandai_loc = eval(data['Personalized']['kuandai_loc'])  #宽带专区入口
    zhineng_jiaju_loc = eval(data['Personalized']['zhineng_jiaju_loc'])  #智能家居入口
    zhengzhao_loc = eval(data['Personalized']['zhengzhao_loc'])  #证照信息入口


    def maishouji(self): #买手机专区
        self.swipe_up(t=1000,n=5)
        self.click_button(self.shangping1_loc)
        logging.info('买手机专区中,点击第一个商品')

    def zhineng_yingjian(self): #智能硬件
        self.swipe_up(t=1000,n=1)
        time.sleep(3)
        self.click_button(self.shangping2_loc)
        logging.info('智能硬件专区中,点击第一个商品')

    def kuandai(self): #宽带专区入口
        self.swipe_up(t=1000,n=1)
        self.click_button(self.kuandai_loc)
        logging.info('宽带家庭中,点击宽带专区')

    def zhineng_jiaju(self): #智能家居入口
        self.click_button(self.zhineng_jiaju_loc)
        logging.info('宽带家庭中,点击智能家居')

    def zhengzhao(self): #证照信息
        self.swipe_up(t=1000,n=2)
        time.sleep(2)
        self.click_button(self.zhengzhao_loc)
        logging.info('点击证照信息')


class Cities(Shouye):  # 省市选择
    c_search_loc = eval(data['Cities']['c_search_loc'])  # 地市选择搜索框
    c_choose_loc = eval(data['Cities']['c_choose_loc'])  # 搜索结果省市选择
    city_loc = eval(data['Cities']['city_loc'])  # 页面当前城市,文本

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


class Recharge(Shouye):   #充值交费
    title_name_txt=eval(data['Recharge']['title_name_txt']) #充值中心页面，文字判断元素
    #话费充值模块
    amount_loc=eval(data['Recharge']['amount_loc'])   #选择话费充值金额

    #流量充值模块
    flow_loc=eval(data['Recharge']['flow_loc'])  #流量
    flowamount_loc=eval(data['Recharge']['flowamount_loc'])   #流量充值额度2G
    content2_loc=eval(data['Recharge']['content2_loc'])  #立即充值
    #话费/流量充值模块->元素判断
    text1_loc=eval(data['Recharge']['text1_loc'])   #选择支付宝支付
    return_loc=eval(data['Recharge']['return_loc'])   #返回


    #未完成订单弹框
    later_loc=eval(data['Recharge']['later_loc'])   #稍后再说
    immediately_loc=eval(data['Recharge']['immediately_loc'])   #立即查看

    #电子发票
    invoice_loc=eval(data['Recharge']['invoice_loc'])  #电子发票入口icon
    my_invoice_loc=eval(data['Recharge']['my_invoice_loc'])  #我的发票页面（文字判断）

    title_back_btn=eval(data['Recharge']['title_back_btn'])   #充值页面返回


    #未完成订单弹框
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

    def content(self): #充值交费入口icon
        time.sleep(3)
        self.click_button(self.content1_loc)
        time.sleep(4)
        logging.info('进入充值交费')

    def check_content(self): #判断充值交费跳转是否正确
        logging.info('========check_content========')
        try:
            test1 =self.driver.find_element(*self.title_name_txt).text
            logging.info(test1)
        except NoSuchElementException:
            logging.error('充值交费跳转错误')
            self.get_screenshot('充值交费跳转错误')
        else:
            logging.info('充值交费跳转正确!')
            return test1

    def invoice(self):  #电子发票入口
        self.later_immediatelyBtn()
        time.sleep(5)
        self.click_button(self.invoice_loc)
        time.sleep(6)
        logging.info('进入电子发票页面')

    def check_invoice(self): #电子发票页面判断
        logging.info('========check_invoice========')
        try:
            test1=self.driver.find_element(*self.my_invoice_loc).text
            logging.info(test1)
        except NoSuchElementException:
            logging.error('电子发票跳转错误')
            self.get_screenshot('电子发票跳转错误')
            self.back()
        else:
            logging.info('电子发票跳转正确!')
            self.back()
            return test1

    def call_charge(self):      #话费充值流程
        self.later_immediatelyBtn()
        self.click_button(self.amount_loc)
        time.sleep(4)
        self.click_button(self.content2_loc)
        logging.info('充值中心->话费充值')

    def flow(self):     #流量充值流程
        self.later_immediatelyBtn()
        self.click_button(self.flow_loc)
        time.sleep(6)
        self.click_button(self.content2_loc)
        logging.info('充值中心->流量充值')

    def return_s(self):  #话费、流量流程返回
        time.sleep(2)
        self.click_button(self.return_loc)


    def back_btn(self):   #返回到充值交费或首页
        self.click_button(self.title_back_btn)



class Package(Shouye):  # 套餐余量
    title_name_txt = eval(data['Package']['title_name_txt'])  # 套餐余量标题

    liulzhicong_loc = eval(data['Package']['liulzhicong_loc'])   #流量直充
    content2_loc = eval(data['Package']['content2_loc'])   #立即充值
    text1_loc = eval(data['Package']['text1_loc'])  #支付宝支付
    Button1_loc = eval(data['Package']['Button1_loc']) #
    zhifub_loc = eval(data['Package']['zhifub_loc'])  #登录支付宝
    return_loc=eval(data['Recharge']['return_loc'])   #返回
    def taocan(self):
        self.click_button(self.taocan_loc)
        logging.info("进入套餐余量页面")

        #流量直充模块
    def liuliang(self):
        # self.swipe_up(t=1000,n=1)
        self.click_button(self.liulzhicong_loc)
        logging.info("点击流量直充，进入充值中心页面")
        liuliang=Recharge(self.driver)
        liuliang.later_immediatelyBtn()
        self.click_button(self.content2_loc)

    def return_s(self):  #话费、流量流程返回
        time.sleep(2)
        self.click_button(self.return_loc)


class Bill(Shouye):  # 我的账单
    yue_loc = eval(data['Bill']['yue_loc'])  # 账户余额
    gobutton_loc = eval(data['Bill']['gobutton_loc'])  # 去充值按钮

    def bill(self):
        self.click_button(self.bill_loc)
        logging.info('进入我的账单')

    def gobutton(self):
        self.click_button(self.gobutton_loc)
        logging.info('点击去充值按钮')


class Search(Shouye):  # 搜索
    box_loc = eval(data['Search']['box_loc'])  # 搜索框
    t_search_loc = eval(data['Search']['t_search_loc'])  # 搜索按钮
    s_choose_loc = eval(data['Search']['s_choose_loc'])  # 选择流量直充
    resou_loc = eval(data['Search']['resou_loc'])  # 热搜标题
    tuijian_loc = eval(data['Search']['tuijian_loc'])  # 搜索无结果推荐
    neirong_loc = eval(data['Search']['neirong_loc'])  # 热搜内容
    lishi_loc = eval(data['Search']['lishi_loc'])  # 搜索历史
    yuyin_s_loc = eval(data['Search']['yuyin_s_loc'])  #开始语音搜索
    yuyin_m_loc = eval(data['Search']['yuyin_m_loc'])  #语音搜索默认普通话
    yuyin_c_loc = eval(data['Search']['yuyin_c_loc'])  #语音搜索关闭

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
        self.tap(942,320)
        logging.info("点击搜索按钮")

    def choose(self):  # 搜索结果选择
        self.click_button(self.s_choose_loc)
        logging.info("搜索结果选择")

    def neirong(self):  # 点击热搜内容
        self.click_button(self.neirong_loc)
        logging.info("5G看移动")


class Card(Base):  # 卡片码表
    # 未登录
    look_loc = eval(data['Card']['look_loc'])  # 登录查看
    tishi_loc = eval(data['Card']['tishi_loc'])  # 未登录提示语
    liuliang_loc = eval(data['Card']['liuliang_loc'])  # 流量剩余
    huafei_loc = eval(data['Card']['huafei_loc'])  # 话费余额
    yue_loc = eval(data['Card']['yue_loc'])  #账户总余额
    keyong_loc = eval(data['Card']['keyong_loc'])  # 话费可用余额
    yuyin_loc = eval(data['Card']['yuyin_loc'])  # 语言剩余
    shengyu_loc = eval(data['Card']['shengyu_loc'])  #您的语音剩余
    fenxiang_loc = eval(data['Card']['fenxiang_loc'])  #分享按钮
    gobutton_loc = eval(data['Card']['gobutton_loc'])  #语音去充值按钮
    gopay_loc = eval(data['Card']['gopay_loc'])  #话费去充值按钮
    jine_loc = eval(data['Card']['jine_loc'])  # 未登录话费余额
    taocan_loc = eval(data['Card']['taocan_loc']) #套餐余量icon
    banli_loc = eval(data['Card']['banli_loc'])  #套餐办理icon
    feixiang_loc= eval(data['Card']['feixiang_loc'])  #4G分享套餐
    zhangdan_loc = eval(data['Card']['zhangdan_loc'])  #我的账单icon
    zonge_loc= eval(data['Card']['zonge_loc'])  #本期账单总额

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
    pic_loc = eval(data['Scan']['pic_loc'])  # 本地图片按钮
    tishi_loc = eval(data['Scan']['tishi_loc'])  #扫码结果提示语
    zhidao_loc = eval(data['Scan']['zhidao_loc']) #知道了

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
        self.tap((230/1080)*X,(302/1920)*Y)  #(239, 314)
        logging.info("点击第一张图片")

    def zhidao(self):
        self.click_button(self.zhidao_loc)
        logging.info("点击知道了")


class Traffic(Shouye):  # 流量管家
    fenxiang_loc = eval(data['Traffic']['fenxiang_loc'])  #分享按钮
    kuaizhao_loc = eval(data['Traffic']['kuaizhao_loc'])  #微信快照
    quxiao_loc = eval(data['Traffic']['quxiao_loc'])  #分享取消
    zhankai_loc = eval(data['Traffic']['zhankai_loc'])  # 流量明细展开
    shouqi_loc = eval(data['Traffic']['shouqi_loc'])  # 流量明细收起
    dingdan_loc = eval(data['Traffic']['dingdan_loc'])  # 流量订单icon
    chongzhi_loc= eval(data['Traffic']['chongzhi_loc'])  #跳转我的订单
    jingwai_loc = eval(data['Traffic']['jingwai_loc'])  # 境外流量
    shangpin_loc = eval(data['Traffic']['shangpin_loc'])  # 流量商品icon
    xiangdan_loc = eval(data['Traffic']['xiangdan_loc'])  # 流量详单icon
    shenfen_loc = eval(data['Traffic']['shenfen_loc'])  #身份认证
    bugouyong_loc = eval(data['Traffic']['bugouyong_loc'])  # 流量不够用title
    yongbuwan_loc = eval(data['Traffic']['yongbuwan_loc'])  # 流量用不完title

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
    duihuan_loc = eval(data['Jifen']['duihuan_loc'])  # 兑换排行入口
    lishi_loc = eval(data['Jifen']['lishi_loc'])  # 历史排行tab
    year_loc = eval(data['Jifen']['year_loc'])  # 年排行tab
    firs_loc = eval(data['Jifen']['firs_loc'])  # 第一位商品
    liji_loc = eval(data['Jifen']['liji_loc'])  # 立即兑换按钮
    sure_loc = eval(data['Jifen']['sure_loc'])  # 确定兑换按钮
    shop_loc = eval(data['Jifen']['shop_loc'])  # 我的账户页购物车入口
    goshop_loc = eval(data['Jifen']['goshop_loc'])  # 购物车空时去购物按钮
    shoucang_loc = eval(data['Jifen']['shoucang_loc'])  # 左滑加入收藏
    delete_loc = eval(data['Jifen']['delete_loc'])  # 左滑删除
    gift_loc = eval(data['Jifen']['gift_loc'])  # 礼品分类入口
    shuzi_loc = eval(data['Jifen']['shuzi_loc'])  # 数字生活标题栏
    shiting_loc = eval(data['Jifen']['shiting_loc'])  # 视听模块入口
    shi_title_loc = eval(data['Jifen']['shi_title_loc'])  # 视听页标题
    candui_loc = eval(data['Jifen']['candui_loc'])  # 我能兑换入口
    account_loc = eval(data['Jifen']['account_loc'])  # 我的账户入口
    jifen_loc = eval(data['Jifen']['jifen_loc'])  # 我的账户页登录后字段

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
        self.tap((147/1080)*X,(446/1920)*Y)
        logging.info("点击第一个商品")
        self.liji()
        logging.info("点击立即兑换")
        self.tap((536/1080)*X,(1845/1920)*Y)
        logging.info("点击确认按钮")


'''
每个页面
返回：ID:title_back_btn
关闭：ID:title_close_btn
页面名称：ID：title_name_txt
'''

if __name__ == '__main__':
    driver = appium_desired()
    huafei = Shouye(driver)
    huafei.start()
    huafei.check_guide_know()
    huafei.huan()
