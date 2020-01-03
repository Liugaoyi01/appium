#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
import time, os
from selenium.common.exceptions import NoSuchElementException  # 捕捉NoSuchElementException异常
from selenium.webdriver.common.by import By
from auto_test_client.public.desired_caps import appium_desired
import yaml
import logging
from auto_test_client.baseView.basepage import Base
from auto_test_client.utils import getLoger, openYaml
from auto_test_client.businessView.loginpage import Login

my_path = "../../data/login.yaml"
data = openYaml.get_yaml_data(my_path)
class My(Base):
    mine_loc = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.ImageView")
    my_bill_loc = (By.XPATH, "//*[contains(@text,'账单查询')]")
    qinmifu_loc = (By.XPATH, "//*[contains(@text,'亲密付')]")
    yiDing_loc = (By.XPATH, "//*[contains(@text,'已订业务')]")
    balance_loc = (By.XPATH, "//*[contains(@text,'话费余额')]")
    payhistory_loc = (By.XPATH, "//android.view.View[@content-desc='交费历史']")
    my_order_loc = (By.XPATH, "//*[contains(@text,'我的订单')]")
    dingyue_loc = (By.XPATH, "//*[contains(@text,'消息订阅')]")
    guanjia_loc = (By.XPATH, "(//android.view.View[@content-desc='流量管家'])[1]")
    my_voucher_loc = (By.XPATH, "//*[contains(@text,'卡券')]")
    my_movie_loc = (By.XPATH, "//*[contains(@text,'电影购票')]")
    xiangdan_loc = (By.XPATH, "//*[contains(@text,'详单查询')]")
    login_loc = (By.XPATH, "//*[@resource-id='mine_login_btn']")
    kefu_loc = (By.XPATH, "//*[contains(@text,'在线客服')]")
    fapiao_loc = (By.XPATH, "//*[contains(@text,'电子发票')]")  # 电子发票
    shiming_loc = (By.XPATH, "//*[contains(@text,'实名登记')]")  # 实名登记
    heduohao_loc = (By.XPATH, "//*[contains(@text,'和多号')]")  # 和多号
    zhineng_loc = (By.XPATH, "//*[contains(@text,'智能家居')]")  # 智能家居
    chajian_loc = (By.XPATH, "//*[contains(@text,'插件中心')]")  # 插件中心
    myInfo_loc = (By.ID, 'img_login')   # 个人信息
    xjbs_loc = (By.ID, 'star_user')  # 星级标识


    def wode(self):
        self.click_button(self.mine_loc)
        logging.info('进入我的页面')
    def xjbs(self):       #进入星级标识
        self.click_button(self.xjbs_loc)
        logging.info('进入星际标识页面')
    def my_bill(self):  #我的账单
        self.click_button(self.my_bill_loc)
        logging.info('进入我的账单页面')
    def qinmifu(self):  #亲密付
        self.click_button(self.qinmifu_loc)
        logging.info('进入亲密付页面')
    def yiDing(self):   #已订业务
        self.click_button(self.yiDing_loc)
        logging.info('进入已订业务页面')
    def balance(self):  #话费余额
        self.click_button(self.balance_loc)
        logging.info('进入话费余额页面')
    def payhistory(self):   #交费历史
        self.click_button(self.payhistory_loc)
        logging.info('进入交费历史页面')
    def my_order(self): #我的订单
        self.click_button(self.my_order_loc)
        logging.info('进入我的订单页面')
    def dingyue(self):  #消息订阅
        self.click_button(self.dingyue_loc)
        logging.info('进入消息订阅页面')
    def guanjia(self):  #流量管家
        self.click_button(self.guanjia_loc)
        logging.info('进入流量管家页面')
    def my_voucher(self):   #我的卡券
        self.click_button(self.my_voucher_loc)
        logging.info('进入我的卡劵页面')
    def my_movie(self):   #我的电影
        self.click_button(self.my_movie_loc)
        logging.info('进入我的电影页面')
    def xiangdan(self): #详单查询
        self.click_button(self.xiangdan_loc)
        logging.info('进入详单查询页面')
    def login(self):  #点击登录
        self.click_button(self.login_loc)
        logging.info('进入登录页面')
    def kefu(self):   #在线客服
        self.click_button(self.kefu_loc)
        logging.info('进入在线客服页面')
    def my(self):
        self.wode()
        logging.info("进入我的页面")
    def fapiao(self):   #电子发票
        self.click_button(self.fapiao_loc)
        logging.info('进入电子发票页面')
    def shiming(self):   #实名登记
        self.click_button(self.shiming_loc)
        logging.info('进入实名登记页面')
    def heduohao(self):   #和多号
        self.click_button(self.heduohao_loc)
        logging.info('进入和多号页面')
    def zhineng(self):   #智能家居
        self.click_button(self.zhineng_loc)
        logging.info('进入智能家居页面')
    def chajian(self):   #插件
        self.click_button(self.chajian_loc)
        logging.info('进入我的插件页面')
    def myInfo(self):   #个人信息
        self.click_button(self.chajian_loc)
        logging.info('进入个人信息')
#OK
#张云龙代码
#ok
class Flow_wallet(My):
  #  wallet_loc = (By.XPATH, "//*[contains(@text,'流量钱包')]")  # 流量钱包
    wallet_loc = (By.ID, 'flow_wallet_name_txt')  # 流量钱包
    accountBalance_loc = (By.ID, '账户余额')  # 流量钱包_余额
    activityRules_loc = (By.ID, '活动规则')  # 活动规则
    activityRules_pan_loc = (By.ID, '什么是流量钱包？')  # 活动规则
    redPacketRecords_loc = (By.ID, '红包记录')  # 红包记录
    redPacketRecords_pan_loc = (By.ID, '收到的红包')  # 收到的红包
    flowDetails_loc = (By.ID, '流量明细')  # 流量明细
    flowDetails_pan_loc = (By.ID, '收入')  # 流量明细
    rechargeRecord_loc = (By.ID, '充值记录')  # 充值记录
    rechargeRecord_pan_loc = (By.ID, '收入')  # 充值记录
    tiQu_jiLu_loc = (By.ID, '提取记录')  # 提取记录
    tiQu_jiLu_pan_loc = (By.ID, '支出')  # 提取记录
    def wallet(self):
        self.click_button(self.wallet_loc)
        logging.info('点击流量钱包')
    def activityRules(self):
        self.click_button(self.activityRules_loc)
        logging.info('点击活动规则')
    def redPacketRecords(self):
        self.click_button(self.redPacketRecords_loc)
        logging.info('点击红包记录')
    def flowDetails(self):
        self.click_button(self.flowDetails_loc)
        logging.info('点击流量明细')
    def rechargeRecord(self):
        self.click_button(self.rechargeRecord_loc)
        logging.info('点击充值记录')
    def tiQu_jiLu(self):
        self.click_button(self.tiQu_jiLu_loc)
        logging.info('点击提取记录')
#ok
class YiDing(My):
    setMeal_pan_loc = (By.XPATH, "//*[contains(@text,'我的套餐')]")   #判定，我的套餐
#    setMeal_pan_loc = (By.NAME,'我的套餐')   #判定，我的套餐
    increment_pan_loc = (By.XPATH, "//*[contains(@text,'增值业务')]")
#    increment_pan_loc = (By.NAME,'增值业务')   #判定，增值业务
    basics_pan_loc = (By.XPATH, "//*[contains(@text,'基础功能')]")   #判定，基础功能
#    basics_pan_loc = (By.NAME,'基础功能')   #判定，基础功能
    other_pan_loc = (By.XPATH, "//*[contains(@text,'其他')]")   #判定，其他
#    other_pan_loc = (By.NAME,'其他')   #判定，其他
    moreBusiness_loc = (By.ID,'moreBusiness')   #更多业务办理
    order_pan_loc = (By.XPATH, "//*[contains(@text,'套餐订购')]")
 #   order_pan_loc = (By.NAME,'套餐订购')
    tuiDing_loc = (By.ID,'do_btn')    #判定，基础功能页的退订按钮
    cancel_loc = (By.ID,'dialog_btn1')   #取消
    tuiding_confirm_loc = (By.ID,'dialog_btn2')   #判定，确定按钮
    share_loc = (By.ID,'title_share_btn')   #分享
    share_pan_loc = (By.XPATH, "//*[contains(@text,'二维码')]")   #分享的二维码
#    share_pan_loc = (By.NAME,'二维码')   #分享的二维码
    share_cancel_loc = (By.ID,'btn_cancel')   #取消分享
    weiXin_loc = (By.XPATH, "//*[contains(@text,'微信好友')]")
#    weiXin_loc = (By.NAME,'微信好友')
    def moreBusiness(self):
        self.click_button(self.moreBusiness_loc)
        logging.info('点击更多')
    def basics_pan(self):
        self.click_button(self.basics_pan_loc)
        logging.info('点击基础功能')
    def tuiDing(self):
        self.click_button(self.tuiDing_loc)
        logging.info('点击退订')
    def cancel(self):
        self.click_button(self.cancel_loc)
        logging.info('点击取消')
    def share(self):
        self.click_button(self.share_loc)
        logging.info('点击分享')
    def share_cancel(self):
        self.click_button(self.share_cancel_loc)
        logging.info('点击分享的取消按钮')
    def weiXin(self):
        self.click_button(self.weiXin_loc)
        logging.info('点击微信')

    def yiDing_lc(self):
        self.yiDing()
        logging.info("进入已订业务")
        self.moreBusiness()
        logging.info("点击更多")
        self.back()
        logging.info("点击返回")
        self.basics_pan()
        logging.info("点击基础业务")
        self.tuiDing()
        logging.info("点击退订按钮")
        self.cancel()
        logging.info("点击取消退订")
#
class Balance(My):
    chongzhi_loc = (By.XPATH,"//*[contains(@text,'充值交费')]")   #充值交费
    pan_chongzhi_loc = (By.ID,'立即充值')   #判定，充值交费
    yuliang_loc = (By.XPATH,"//*[contains(@text,'套餐余量')]")   #套餐余量
    pan_yuliang_loc = (By.XPATH,"//*[contains(@text,'已用:')]")   #判定，套餐余量
    yuliang_back_loc = (By.ID,'title_back_btn')  #套餐余量的返回按钮
    taocan_loc = (By.XPATH,"//*[contains(@text,'套餐办理')]")   #套餐办理
    pan_taocan_loc = (By.XPATH,"//android.view.View[@content-desc='4G飞享套餐¥58-588.']")   #判定，套餐办理
    zhangdan_loc = (By.XPATH,"//*[contains(@text,'我的账单')]")   #我的账单
    pan_zhangdan_loc = (By.XPATH,"//*[contains(@text,'账单总额')]")   #判定，我的账单
    balance_back_loc = (By.ID,'title_back_btn')
    quchongzhi_loc = (By.ID,'txt_gopay')    #去充值
    chongzhi_pan_loc = (By.ID,'立即充值')    #判定，充值页面
    xiaofei_loc = (By.ID,'txt_mouth_consume_title')    #当月消费
    keyong_loc = (By.ID,'title_back_btn')    #可用余额

    def chongzhi(self):
        self.click_button(self.chongzhi_loc)
        logging.info('点击充值交费')
    def yuliang(self):
        self.click_button(self.yuliang_loc)
        logging.info('点击套餐余量')
    def taocan(self):
        self.click_button(self.taocan_loc)
        logging.info('点击他女安办理')
    def zhangdan(self):
        self.click_button(self.zhangdan_loc)
        logging.info('点击我的账单')
    def balance_back(self):
        self.click_button(self.balance_back_loc)
        logging.info('点击话费余额的返回按钮')
    def yuliang_back(self):
        self.click_button(self.yuliang_back_loc)
        logging.info('点击套餐余量的返回按钮')
    def quchongzhi(self):
        self.click_button(self.quchongzhi_loc)
        logging.info('点击去充值')

    def Balance_lc(self):
        self.balance()
        logging.info("进入话费余额")
        self.chongzhi()
        logging.info("点击充值交费")
        self.back()
        self.yuliang()
        logging.info("点击套餐余量")
        self.back()
        self.taocan()
        logging.info("点击套餐办理")
        self.back()
        self.zhangdan()
        logging.info("点击套餐办理")
#ok
class MyOrder(My):
    share_loc = (By.ID,'title_share_btn')  #分享订单页面
    share_to_loc = (By.XPATH,"//*[contains(@text,'二维码')]")    #二维码分享
    share_pan_loc = (By.XPATH,"//*[contains(@text,'邀请好友扫一扫分享给TA')]")    #二维码分享判定
    flowOrder_loc = (By.XPATH,"//*[contains(@text,'流量订单')]")  #判定
    orderNumber_loc = (By.XPATH,"//*[@resource-id='订单编号：']")  #判定流量订单
    cz_order_loc = (By.XPATH,"//*[contains(@text,'充值订单')]")
    cz_order_pan_loc = (By.XPATH,"//android.webkit.WebView[@content-desc='充值订单']/android.widget.ListView[1]/android.view.View")  #判定
    sp_order_loc = (By.XPATH,"//*[contains(@text,'商品订单')]")  #判定
    sp_order_pan_loc = (By.XPATH,"//android.webkit.WebView[@content-desc=‘商品订单’]/android.widget.ListView/android.view.View[1]")
    keFu_1_loc = (By.XPATH,"(//android.view.View[@content-desc='客服'])[1]")
    def share(self):
        self.click_button(self.share_loc)
        logging.info('点击分享订单')
    def share_to(self):
        self.click_button(self.share_to_loc)
        logging.info('点击分享到')
    def sp_order(self):
        self.click_button(self.sp_order_loc)
        logging.info('点击商品订单')
    def sp_order_pan(self):
        self.click_button(self.sp_order_pan_loc)
        logging.info('点击商品订单的第一个订单，进入到订单详情')
    def keFu_1(self):
        self.click_button(self.keFu_1_loc)
        logging.info('点击点击商品订单的第一个订单的客服')
    def cz_order(self):
        self.click_button(self.cz_order_loc)
        logging.info('点击充值订单')
    def flowOrder(self):
        self.click_button(self.flowOrder_loc)
        logging.info('点击流量订单')









    def Myorder_lc(self):
        self.my_order()
        logging.info("进入我的订单")
        self.cz_order()
        logging.info("点击充值订单")
        self.ll_order()
        logging.info("点击流量订单")
        self.sporder()
        logging.info("点击商品订单")
#
class Xxdingyue(My):
    no_dingyue_loc = (By.XPATH,"//*[@resource-id='暂无订阅信息']")  #没有订阅消息
    def Xxdingyue_lc(self):
        self.swipe_up()
        logging.info("向下滑动")
        self.dingyue()
        logging.info("进入消息订阅")
#
class Guanjia(My):
    dingdan_loc = (By.ID,'流量订单')
    dingdan_pan_loc = (By.ID,'充值订单')
    zhichong_loc = (By.ID,'流量商品')
    zhichong_pan_loc = (By.ID,'通讯录')
    shangpin_loc = (By.ID,'流量商品')
    shangpin_pan_loc = (By.ID,'搜索')
    xiangdan_loc = (By.ID,'流量详单')
    xiangdan_pan_loc = (By.ID,'tv_title')  #拉起详单登录判定
    xiangdanback_pan_loc = (By.ID,'login_close')  #详单返回按钮
    bannian_loc = (By.XPATH,"(//android.view.View[@content-desc='流量半年包'])[1]")
    liuliang_pan_loc = (By.ID,'立即办理')
    jibao_loc = (By.XPATH,"//android.view.View[@content-desc='流量季包']")
    ri_taocan_loc = (By.XPATH,"//android.view.View[@content-desc='流量日套餐']")
    shiping_loc = (By.ID,'视频')
    yuedu_loc = (By.ID,'阅读')
    yinyue_loc = (By.ID,'音乐')
    def dingdan(self):
        self.click_button(self.dingdan_loc)
    def zhichong(self):
        self.click_button(self.zhichong_loc)
    def shangpin(self):
        self.click_button(self.shangpin_loc)
    def xiangdan(self):
        self.click_button(self.xiangdan_loc)
    def bannian(self):
        self.click_button(self.bannian_loc)   #流量半年包
    def jibao(self):
        self.click_button(self.jibao_loc) #流量季包
    def ri_taocan(self):
        self.click_button(self.ri_taocan_loc)  #流量日套餐
    def shiping(self):
        self.click_button(self.shiping_loc)
    def yuedu(self):
        self.click_button(self.yuedu_loc)
    def yinyue(self):
        self.click_button(self.yinyue_loc)
    def xiangdanback_pan(self):
        self.click_button(self.xiangdanback_pan_loc)
    def Guanjia_lc(self):
        self.guanjia()
        logging.info("进入流量管家")
        self.dingdan()
        logging.info("进入流量订单")
        self.back()
        logging.info("返回")
        self.zhichong()
        logging.info("进入充值订单")
        self.back()
        logging.info("返回")
        self.shangpin()
        logging.info("进入商品订单")
        self.back()
        logging.info("返回")
        self.back()
        logging.info("返回")
        self.bannian()
        logging.info("点击流量半年包")
        self.back()
        logging.info("返回")
        self.jibao()
        logging.info("点击流量季包")
        self.back()
        logging.info("返回")
        self.ri_taocan()
        logging.info("点击流量日包")
        self.back()
        logging.info("返回")
        self.swipe_up()
        logging.info("向上滑动")
        self.yuedu()
        logging.info("点击阅读")
        self.yinyue()
        logging.info("点击音乐")
#
class My_voucher(My):
    notUsed_loc = (By.XPATH,"(//android.widget.Button[@content-desc='查看'])[1]")  #判定“未使用”标签
    cardHistory_loc = (By.ID,'卡券历史')
    guoQi_loc = (By.ID,'已过期')  #判定
    alreadyUsed_loc = (By.ID,'已使用')  #判定
    no_voucher_loc = (By.XPATH,"//*[@resource-id='暂无卡券，更多好券敬请期待']")  #判定
    miGu_loc = (By.ID,'咪咕电影券')
    def cardHistory(self):
        self.click_button(self.cardHistory_loc)
    def guoQi(self):
        self.click_button(self.guoQi_loc)
    def alreadyUsed(self):
        self.click_button(self.alreadyUsed_loc)
    def miGu(self):
        self.click_button(self.miGu_loc)
    def ka_juan(self):
        self.my_voucher()
        logging.info("进入我的卡劵")
        self.guoQi()
        logging.info("点击已过期")
        self.alreadyUsed()
        logging.info("点击已使用")
        self.miGu()
        logging.info("点击咪咕电影劵")
        self.back()
        logging.info("点击返回")
#
class My_movie(My):
    gou_piao_loc = (By.ID,'title_name_txt')  #购票判定
    gou_piaoclose_loc = (By.ID,'title_close_btn')  #购票判定
    def gou_piao(self):
        self.click_button(self.gou_piao_loc)
    def gou_piaoclose(self):
        self.click_button(self.gou_piaoclose_loc)

    def dian_ying(self):
        self.my_movie()
        logging.info("进入我的电影")

class Xiangdan(My):
    renzheng_loc = (By.XPATH,"//*[@resource-id='tv_title']")  #详单的身份认证
    jiansuo_loc = (By.XPATH,"//*[contains(@text,'检索')]")
    anniu_loc = (By.XPATH,"//*[@resource-id='select_timeornumber']")  #按号码的下拉按钮
    haoma_loc = (By.XPATH,"//*[@resource-id='text_num']")  #按号码
    riqi_loc = (By.XPATH,"//*[@resource-id='text_date']")  #按日期
    mingcheng_loc = (By.XPATH,"//*[@resource-id='text_name']")  #按名称
    shuru_loc = (By.XPATH,"//*[@resource-id='searedt']")  #检索的输入框
    sousuo_loc = (By.XPATH,"//*[@resource-id='searedt']")  #搜索按钮
    tonghua_loc = (By.XPATH,"//*[contains(@text,'通话详单')]")
    fenxi_loc = (By.XPATH,"//*[@resource-id='toanalysis']")  #详单分析
    pan_gaisu_loc = (By.XPATH,"//android.view.View[@content-desc='11月通话概述']")  #判定
    pan_meiri_loc = (By.XPATH,"//android.view.View[@content-desc='每日通话']")  #判定
    pan_time_loc = (By.XPATH,"//android.view.View[@content-desc='通话时间分布']")  #判定
    def jiansuo(self):
        self.click_button(self.jiansuo_loc)
    def anniu(self):
        self.click_button(self.anniu_loc)
    def haoma(self):
        self.click_button(self.haoma_loc)
    def riqi(self):
        self.click_button(self.riqi_loc)
    def mingcheng(self):
        self.click_button(self.mingcheng_loc)
    def shuru(self):
        self.click_button(self.shuru_loc)
    def sousuo(self):
        self.click_button(self.sousuo_loc)
    def tonghua(self):
        self.click_button(self.tonghua_loc)
    def fenxi(self):
        self.click_button(self.fenxi_loc)
#
class Taocan_xq(My):
    qianbao_loc = (By.XPATH,"//*[contains(@text,'流量钱包')]")  #流量钱包
    qianbao_pan_loc = (By.ID,'流量钱包账户余额')  #流量钱包判定
    kajuan_loc = (By.XPATH,"//*[contains(@text,'卡券')]")  #卡劵
    kajuan_pan_loc = (By.ID,'话费券')  #卡劵判定
    jifen_loc = (By.XPATH,"//*[contains(@text,'积分')]")  #积分
    jifen_pan_loc = (By.ID,'中国移动积分商城')  #积分判定
    quanyi_loc = (By.XPATH,"//*[contains(@text,'权益')]")  #我的权益
    quanyi_pan_loc = (By.ID,'积分')  #我的权益判定

    def qianbao(self):
        self.click_button(self.qianbao_loc)
    def kajuan(self):
        self.click_button(self.kajuan_loc)
    def jifen(self):
        self.click_button(self.jifen_loc)
    def quanyi(self):
        self.click_button(self.quanyi_loc)
#
class Ke_fu(My):
    send_loc = (By.XPATH,"//android.widget.Button[@content-desc='发送']")  #点击登录
    def send(self):
        self.click_button(self.send_loc)
    def Kefu_lc(self):
        self.swipe_up()
        logging.info("向下滑动")
        self.kefu()
        logging.info("进入在线客服")
#
class MyInfo(My):    #个人信息
    #权限元素
    edit_loc = (By.XPATH,"//*[contains(@text,'编辑头像')]")  #编辑头像
    headImg_loc = (By.ID,'selectid')  #头像id
    imgExit_loc = (By.ID,'but_exit')  #取消头像

    def edit(self):  #编辑头像
        self.click_button(self.edit_loc)
    def imgExit(self):  #取消头像
        self.click_button(self.imgExit_loc)
    def headImg(self):  #点击头像
        self.click_button(self.headImg_loc)


#ok
class MyBill(My):    #我的账单
    #权限元素
    totalBill_loc = (By.ID,'tv_bill_all')  #判定，账单总额
    toRecharge_loc = (By.ID,'img_go_recharge')  #去充值
    voucherCenter_loc = (By.ID,'立即充值')  #判定，充值中心
    voucherCenter_back_loc = (By.ID,'title_back_btn')      #充值中心的返回按钮
    xiangDan_loc = (By.ID,'xiangdan_btn')  #详单查询
    xiangDan_pan_loc = (By.ID,'one_key_login_tv')  #判定，详单查询
    xiangDan_Back_loc = (By.ID,'login_close')  #详单查询的返回按钮
    shareBill_loc = (By.ID,'title_share_btn')  #我的账单分享
    share_pan_loc = (By.ID,'tv_share_name')  #判定，分享
    cancelShare_loc = (By.ID,'btn_cancel')  #取消分享
    billBack_loc = (By.ID,'title_back_btn')  #账单的返回（我的）按钮
    def toRecharge(self):      #去充值
        self.click_button(self.toRecharge_loc)
    def voucherCenter_back(self):      #充值中心的返回按钮
        self.click_button(self.voucherCenter_back_loc)
    def xiangDan(self):  #详单查询
        self.click_button(self.xiangDan_loc)
    def xiangDan_Back(self):  #详单查询的返回按钮
        self.click_button(self.xiangDan_Back_loc)
    def shareBill(self):  #我的账单分享
        self.click_button(self.shareBill_loc)
    def cancelShare(self):  #取消分享
        self.click_button(self.cancelShare_loc)
    def billBack(self):  #账单的返回（我的）按钮
        self.click_button(self.billBack_loc)
    def zhangdan_lc(self):
        self.my_zhangdan()
        logging.info("进入我的账单")
        self.toRecharge()
        logging.info("点击去充值")
        self.voucherCenter_back()
        logging.info("返回")
    #    self.yuliang()
        logging.info("点击套餐余量")
      #  self.yuliang_back()
        logging.info("点击套餐余量的返回按钮")
        self.xiangDan()
        logging.info("点击详单查询")
        self.xiangDan_Back()
        logging.info("点击详单查询的返回按钮")
#
class Payhistory(My):
    jiaofei_pan_loc = (By.ID,'pay_history_btn')
    chongzhi_pan_loc = (By.ID,'title_name_txt')   #充值中心
    shaixuan_loc = (By.ID,'title_select_btn')
    shouqi_loc = (By.XPATH,"//*[contains(@text,'收起')]")
    fenxiang_loc = (By.ID,'title_share_btn')
    pengyouquan_loc = (By.XPATH,"//*[contains(@text,'朋友圈')]")
    quxiao_loc = (By.XPATH,"//*[contains(@text,'取消')]")
    siyue_loc = (By.XPATH,"//*[contains(@text,'2019年4月')]")
    erweima_loc = (By.XPATH,"//*[contains(@text,'二维码')]")
    def shaixuan(self):
        self.click_button(self.shaixuan_loc)
    def jiaofei(self):
        self.click_button(self.jiaofei_pan_loc)
    def shouqi(self):
        self.click_button(self.shouqi_loc)
    def fenxiang(self):
        self.click_button(self.fenxiang_loc)
    def quxiao(self):
        self.click_button(self.quxiao_loc)
    def siyue(self):
        self.click_button(self.siyue_loc)
    def erweima(self):
        self.click_button(self.erweima_loc)
    def payhistory_lc(self):
        self.payhistory()
        logging.info("进入交费历史")
        self.jiaofei()
        logging.info("进入充值缴费")
        self.back()
        logging.info("返回")
        self.shaixuan()
        logging.info("点击筛选")

#李纯代码
class Qinmifu(My):    #亲密付
    #权限元素
    qmf_dingdan_pan_loc = (By.ID, '亲密付订单')  #判定，亲密付订单
    qmf_jilu_pan_loc = (By.ID, '添加记录')  #判定，添加记录
    qmf_tianjia_pan_loc = (By.ID, '添加号码')  #判定，添加号码
    liuliang_pan_loc = (By.ID, '您当前没有亲密付流量订单')  #判定，亲密付流量订单
    chongzhi_pan_loc = (By.ID, '¥9.98删除订单再充一笔')  #判定，亲密付充值订单
    chongzhi_loc = (By.ID, '亲密付充值订单')  #充值订单
    liuliang_loc = (By.ID, '亲密付流量订单')   #流量订单
    chongliuliang_loc = (By.ID, '充流量')  #冲流量
    chonghuafei_loc = (By.ID, '充话费')  #充话费
    lijichongzhi_loc = (By.ID, '立即充值')  #立即充值
    queren_loc = (By.XPATH, "//*[contains(@text,'确认支付 ¥5.00')]")  #确认支付
    close_anniu_loc = (By.XPATH, "//*[contains(@text,'关闭')]")  #关闭支付页面
    querenpay_loc = (By.XPATH, "//*[contains(@text,'确认支付 ¥5.00')]")  #确认支付完成
    close_zhifu_loc = (By.XPATH, "//*[@resource-id='title_close_btn']")  #关闭支付页面
    tianjiajilu_loc = (By.XPATH, "//*[contains(@text,'添加记录')]")  #添加记录
    beitianjiajilu_loc = (By.ID, '被绑定记录')  #被添加记录
    pan_tianjiajilu_loc = (By.ID, '绑定记录')  #判定，添加记录
    pan_beitianjiajilu_loc = (By.ID, '超时未回复你追一')   #判定，被添加记录
    pan_chaoshijilu_loc = (By.XPATH, "//*[contains(@text,'超时未回复')]")  #判定，超时未回复
    pan_qinmifu_loc = (By.XPATH, "//*[contains(@text,'家庭成员管理')]")  #判定亲密付
    pan_liuliang_loc =  (By.XPATH, "//*[contains(@text,'流量直充')]")  #判定充流量页面
    pan_huafei_loc =  (By.XPATH, "//*[contains(@text,'充值交费')]")  #判定充话费页面
    back_loc = (By.ID, 'title_back_btn')  #返回_
    chongzhijilu_loc = (By.XPATH, "//*[contains(@text,'充值记录')]")  #充值记录
    tianjiahaoma_loc = (By.ID, '添加号码') # 添加号码
    haomashurulan_loc = (By.XPATH, '//android.webkit.WebView[@content-desc="家庭成员管理"]'
                                   '/android.widget.EditText[1]')  # 号码输入栏
    shurunicheng_loc = (By.XPATH, '//android.webkit.WebView[@content-desc="家庭成员管理"]'
                                  '/android.widget.EditText[2]')  # 输入昵称栏
    quxiao_loc = (By.ID, '取消') # 取消
    pan_quxiao_loc = (By.ID, '添加号码') # 判定取消
    lijitianjia_loc = (By.ID, '立即添加') # 立即添加
    pan_lijitianjia_loc = (By.ID, 'cheshi') # 判定 立即添加
    guanli_loc = (By.XPATH, "//*[contains(@text,'管理成员')]")  # 管理成员
    pan_guanli_loc = (By.ID, '成员管理')  # 判定 管理成员


    def TianJiaHaoMa(self):  #添加号码
        self.click_button(self.tianjiahaoma_loc)
        logging.info("添加号码")
    def HaoMaShuRuLan(self,value1):   #号码输入栏
        self.send_keys(self.haomashurulan_loc,value1)
        logging.info("号码输入栏")
    def ShuRuNiCheng(self,value2):  #昵称输入栏
        self.send_keys(self.shurunicheng_loc, value2)
        logging.info("昵称输入")
    def QuXiao(self):  #取消
        self.click_button(self.quxiao_loc)
        logging.info("取消")
    def LiJiTianJia(self):   #立即添加
        self.click_button(self.lijitianjia_loc)
        logging.info("立即添加")
    def GuanLi(self):   #管理成员
        self.tap(635.7, 237.1)
        self.click_button(self.guanli_loc)
        logging.info("管理成员")
    def ChongZhi(self):  #亲密付充值订单
        self.click_button(self.chongzhi_loc)
        logging.info("点击亲密付充值订单")
    def LiuLiang(self):  #亲密付流量订单
        self.click_button(self.liuliang_loc)
        logging.info("点击亲密付流量订单")
    def ChongLiuLiang(self):  #冲流量
        self.click_button(self.chongliuliang_loc)
        logging.info("点击充流量")
    def ChongHuaFei(self):  #充话费
        self.click_button(self.chonghuafei_loc)
        logging.info("点击充话费")
    def LiJiChongZhi(self):  #立即充值
        self.click_button(self.lijichongzhi_loc)
        logging.info("点击立即充值")
    def QueRen(self):  #确认支付
        self.click_button(self.queren_loc)
        logging.info("点击确认支付")
    def close_zhifu(self):  #关闭支付页面
        self.click_button(self.close_zhifu_loc)
        logging.info("点击关闭支付")
    def TianJiaJiLu(self):  #添加记录
        self.tap(635.7, 237.1)
        self.click_button(self.tianjiajilu_loc)
        logging.info("点击添加记录")
    def BeiTianJiaJiLu(self):  #被添加记录
        self.click_button(self.beitianjiajilu_loc)
        logging.info("点击被添加记录")
    def ChongZhiJiLu(self):
        self.tap(635.7, 237.1)
        self.click_button(self.chongzhijilu_loc)
        logging.info("点击充值记录")
    def back(self):  #返回
        self.click_button(self.back_loc)
        logging.info("点击返回")

    def TianHaoQuXiao(self): #添加号码时取消
        self.TianJiaHaoMa()
        logging.info("点击添加号码")
        self.HaoMaShuRuLan("18723240750")
        logging.info("点击号码输入栏")
        self.ShuRuNiCheng("cheshi")
        logging.info("点击昵称输入栏")
        self.QuXiao()
        logging.info("点击取消")
    def TianHao(self):  #添加号码
        self.TianJiaHaoMa()
        logging.info("点击添加号码")
        self.HaoMaShuRuLan("18723240750")
        logging.info("点击号码输入栏")
        self.ShuRuNiCheng("cheshi")
        logging.info("点击昵称输入栏")
        self.LiJiTianJia()
        logging.info("点击立即添加")




class FaPiao(My):
    # 话费充值发票入口
    huafei_loc =(By.ID,'话费充值发票')
    # 流量直充发票入口
    liuliang_loc = (By.ID,'流量直充发票')
    # 宽带发票入口
    kuandai_loc = (By.ID,'宽带发票')
    # 月结发票入口
    yuejie_loc = (By.ID,'月结发票')
    # 发票抬头入口
    taitou_loc = (By.ID,'发票抬头')
    # 点击新增发票
    xinzeng_loc = (By.ID,'新增发票')
    # 点击发票抬头输入栏
    riseinput_loc = (By.XPATH,'//android.webkit.WebView[@content-desc="新增发票"]/android.widget.EditText[1]')
    # 点击纳税人识别号输入栏
    shibiehao_loc = (By.XPATH,'//android.webkit.WebView[@content-desc="新增发票"]/android.widget.EditText[2]')
    #设为默认按钮
    moren_loc = (By.XPATH,'//android.webkit.WebView[@content-desc="新增发票"]/android.view.View[4]/android.widget.CheckBox')
    #点击保存按钮
    baocun_loc = (By.ID,'保存')
    #邮件推送入口
    youtui_loc = (By.ID,'邮件推送')
    #点击常用邮箱输入栏
    mail_loc = (By.XPATH,'//android.webkit.WebView[@content-desc="推送设置"]/android.widget.EditText')
    #点击保存按钮
    save_loc = (By.ID,'保存')
    #知道了按钮
    zhidaole_loc = (By.ID,'知道了')
    # 返回按钮
    back_loc = (By.ID,'title_back_btn')
    # 关闭按钮
    close_loc = (By.ID,'title_close_btn')
    # 点击开具按钮
    kaiju_loc = (By.ID,'开具')
    # 停止开具按钮
    tingkai_loc = (By.ID,'停止开具')
    # 确认开具按钮
    quekai_loc = (By.ID,'确认开具')
    # 判定话费充值发票页面
    pan_huafei_loc = (By.XPATH,'//*[contains(@text,"话费充值发票")]')
    # 判定流量直充发票页面
    pan_liuliang_loc = (By.XPATH,'//*[contains(@text,"流量直充发票")]')
    # 判定宽带发票页面
    pan_kuandai_loc = (By.XPATH,'//*[contains(@text,"宽带发票")]')
    # 判定月结发票页面
    pan_yuejie_loc = (By.XPATH,'//*[contains(@text,"月结发票")]')
    # 判定发票抬头页面
    pan_taitou_loc = (By.XPATH,'//*[contains(@text,"发票管理")]')
    # 判定新增发票页面
    pan_xinzeng_loc = (By.XPATH,'//*[contains(@text,"新增发票")]')
    # 判定已成功新增发票
    danwei_loc = (By.ID,'单位')
    # 判定推送邮箱
    pan_tuisong_loc = (By.XPATH,'//*[contains(@text,"推送设置")]')
    # 判定邮箱保存
    pan_youxiang_loc = (By.XPATH,'//android.widget.EditText[@content-desc="2418261328@qq.com"]')




        #点击话费充值发票
    def HuaFei(self):
        self.click_button(self.huafei_loc)
        logging.info("点击话费充值发票")
        #点击流量直充发票
    def LiuLiang(self):
        self.click_button(self.liuliang_loc)
        logging.info("点击流量直充发票")
        #点击宽带发票
    def KuanDai(self):
        self.click_button(self.kuandai_loc)
        logging.info("点击宽带发票")
        #点击月结发票
    def YueJie(self):
        self.click_button(self.yuejie_loc)
        logging.info("点击月结发票")
        #点击发票抬头
    def TaiTou(self):
        self.click_button(self.taitou_loc)
        logging.info("点击发票抬头")
        # 点击新增发票
    def XinZeng(self):
        self.click_button(self.xinzeng_loc)
        logging.info("点击新增发票")
        # 点击抬头输入栏
    def RiseInput(self,value1):
        self.send_keys(self.riseinput_loc, value1)
        logging.info("点击发票抬头输入栏")
        #点击识别号输入栏
    def ShiBieHao(self,value2):
        self.send_keys(self.shibiehao_loc, value2)
        logging.info("点击纳税人识别号输入栏")
        # 点击默认
    def MoRen(self):
        self.click_button(self.moren_loc)
        logging.info("点击默认")
        # 点击保存
    def BaoCun(self):
        self.click_button(self.baocun_loc)
        logging.info("点击保存")
        # 点击返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")
        # 点击关闭
    def close(self):
        self.click_button(self.close_loc)
        logging.info("点击关闭")
        # 点击开具
    def KaiJu(self):
        self.click_button(self.kaiju_loc)
        logging.info("点击开具")

        #  点击停止开具
    def TingKai(self):
        self.click_button(self.tingkai_loc)
        logging.info("点击停止开具")
        # 点击确认开具
    def QueKai(self):
        self.click_button(self.quekai_loc)
        logging.info("点击确认开具")
        # 点击邮箱推送
    def YouTui(self):
        self.click_button(self.youtui_loc)
        logging.info("点击邮箱推送")
        #输入邮箱号
    def mail(self,value3):
        self.send_keys(self.mail_loc,value3)
        #self.send_keys(self.mail_loc, value1)
        logging.info("点击邮箱号")
        #self.find_element(self.mail_loc).clear()

        #点击保存
    def save(self):
        self.click_button(self.save_loc)
        logging.info("点击保存")

    def XinFaPiao(self,value1,value2):   #新增一个发票
        self.fapiao()
        logging.info("进入电子发票")
        self.TaiTou()
        logging.info("进入发票抬头")
        self.XinZeng()
        logging.info("新增发票")
        self.RiseInput(value1)
        logging.info("抬头栏输入")
        #点击纳税人识别号输入栏输入内容
        self.ShiBieHao(value2)
        logging.info("识别栏输入")
        #点击默认，点击保存
        self.MoRen()
        self.BaoCun()
        self.back()

class ShiMing(My):
    pan_shiming_loc = (By.XPATH,'//*[contains(@text,"实名补登记")]')   #判定进入实名登记页面
    back_loc = (By.ID,'title_back_btn')  #返回按钮

    #返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")

class HeDuoHao(My):
    pan_heduohao_loc = (By.XPATH,'//*[contains(@text,"副号")]') #判定进入和多号页面
    back_loc = (By.ID,'title_back_btn')  #返回按钮
    #点击返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")

class ZhiNeng(My):
    wangguan_loc = (By.XPATH, '//android.webkit.WebView[@content-desc="智能家居"]'
                              '/android.widget.ListView[2]/android.view.View[1]')  # 网关管理
    shebei_loc = (By.XPATH, '//android.webkit.WebView[@content-desc="智能家居"]/'
                            'android.widget.ListView[2]/android.view.View[2]')  # 设备管理
    baokuan_loc = (By.XPATH, '//android.webkit.WebView[@content-desc="智能家居"]/'
                             'android.widget.ListView[4]/android.view.View[1]')  # 爆款商品
    pan_zhineng_loc = (By.XPATH, '//*[contains(@text,"智能家居")]')  # 判定进入智能家居
    pan_wangguan_loc = (By.XPATH, '//*[contains(@text,"网络管理")]')  # 判定进入网关管理
    pan_shebei_loc = (By.XPATH, '//*[contains(@text,"添加智能设备")]')  # 判定进入设备管理
    pan_baokuan_loc = (By.XPATH, '//*[contains(@text,"商品详情")]')  # 判定进入爆款商品详情页
    back_loc = (By.ID, 'title_back_btn')  # 返回按钮
    wangguan_back_loc = (By.ID, 'ivBack')  # 网关管理页面的返回按钮
    shebei_back_loc = (By.ID, 'sm_main_back_white_iv')  # 设备管理页面的返回按钮
    close_loc = (By.ID, 'title_close_btn')  # 关闭
    #点击网关管理
    def WangGuan(self):
        self.click_button(self.wangguan_loc)
        logging.info("点击网关管理")
    #点击设备管理
    def SheBei(self):
        self.click_button(self.shebei_loc)
        logging.info("点击设备管理")
    #点击爆款商品
    def BaoKuan(self):
        self.click_button(self.baokuan_loc)
        logging.info("点击爆款商品")
    #点击返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")
    #点击网关管理返回
    def WangGuan_back(self):
        self.click_button(self.wangguan_back_loc)
        logging.info("点击网关管理返回")
    #点击设备管理返回
    def SheBei_back(self):
        self.click_button(self.shebei_back_loc)
        logging.info("点击设备管理返回")
    #点击关闭
    def close(self):
        self.click_button(self.close_loc)
        logging.info("点击关闭")

class ChaJian(My):
    pan_chajian_loc = (By.XPATH, '//*[contains(@text,"插件中心")]')  # 判定插件中心
    fenxiang_loc =  (By.ID, 'title_share_btn')  # 分享按钮
    pan_fenxiang_loc =  (By.XPATH, '//*[contains(@text,"微信朋友圈")]')  # 判定分享
    quxiao_loc = (By.XPATH, '//*[contains(@text,"取消")]')  # 取消按钮
    back_loc = (By.ID, 'title_back_btn')  # 返回按钮
    #点击分享
    def FenXiang(self):
        self.click_button(self.fenxiang_loc)
        logging.info("点击进入分享")
    #点击取消
    def QuXiao(self):
        self.click_button(self.quxiao_loc)
        logging.info("点击取消")
    #点击返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")




if __name__ == '__main__':
    driver = appium_desired()

    ba = Login(driver)

    ba.start()
    ba.login('13501585305')
    zhang = Geren(driver)
    zhang.geren_lc()



    '''
   driver = appium_desired()
   zhang = My_movie(driver)
   zhang.start()
   time.sleep(3)
   zhang.my()
   zhang.dianying()
   deng = PO.loginpage.Login(driver)
   deng.zhanghao(13501585305)
   deng.yanzheng()
   deng.chick_login()
   denglu = PO.loginpage.Login(driver)
   denglu.start()
   denglu.login('13501585305')
   driver.find_element_by_id('com.greenpoint.android.mc10086.activity:id/dialog_btn1').click()
   zhang = Zhangdan(driver)
   zhang.my_zhangdan()
#   base.start()
  # base.my()
'''










