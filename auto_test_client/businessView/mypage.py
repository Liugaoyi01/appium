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
    wode_loc = eval(data['My']['wode_loc'])
    imglogin_loc = eval(data['My']['imglogin_loc'])  # 个人信息图标
    touxiang_loc = eval(data['My']['touxiang_loc'])  # 头像
    xjbs_loc = eval(data['My']['xjbs_loc'])  # 星级标识
    my_zhangdan_loc = eval(data['My']['my_zhangdan_loc'])  # 我的账单
    qinmifu_loc = eval(data['My']['qinmifu_loc'])  # 亲密付
    yiding_loc = eval(data['My']['yiding_loc'])  # 已订业务
    balance_loc = eval(data['My']['balance_loc'])  # 话费余额
    payhistory_loc = eval(data['My']['payhistory_loc'])
    my_order_loc = eval(data['My']['my_order_loc'])
    dingyue_loc = eval(data['My']['dingyue_loc'])
    guanjia_loc = eval(data['My']['guanjia_loc'])
    my_voucher_loc = eval(data['My']['my_voucher_loc'])
    my_movie_loc = eval(data['My']['my_movie_loc'])
    xiangdan_loc = eval(data['My']['xiangdan_loc'])
    login_loc = eval(data['My']['login_loc'])  # 点击登录
    kefu_loc = eval(data['My']['kefu_loc'])
    fapiao_loc = eval(data['My']['fapiao_loc'])  # 电子发票
    shiming_loc = eval(data['My']['shiming_loc'])  # 实名登记
    heduohao_loc = eval(data['My']['heduohao_loc'])  # 和多号
    zhineng_loc = eval(data['My']['zhineng_loc'])  # 智能家居
    chajian_loc = eval(data['My']['chajian_loc'])  # 插件中心

    def wode(self):
        self.click_button(self.wode_loc)
        logging.info('进入我的页面')

    def imglogin(self):  # 个人信息图标
        self.click_button(self.imglogin_loc)
        logging.info('进入个人信息页面')

    def xjbs(self):  # 进入星级标识
        self.click_button(self.xjbs_loc)
        logging.info('进入星际标识页面')

    def my_zhangdan(self):  # 我的账单
        self.click_button(self.my_zhangdan_loc)
        logging.info('进入我的账单页面')

    def qinmifu(self):  # 亲密付
        self.click_button(self.qinmifu_loc)
        logging.info('进入亲密付页面')

    def yiding(self):  # 已订业务
        self.click_button(self.yiding_loc)
        logging.info('进入已订业务页面')

    def balance(self):  # 话费余额
        self.click_button(self.balance_loc)
        logging.info('进入话费余额页面')

    def payhistory(self):  # 交费历史
        self.click_button(self.payhistory_loc)
        logging.info('进入交费历史页面')

    def my_order(self):  # 我的订单
        self.click_button(self.my_order_loc)
        logging.info('进入我的订单页面')

    def dingyue(self):  # 消息订阅
        self.click_button(self.dingyue_loc)
        logging.info('进入消息订阅页面')

    def guanjia(self):  # 流量管家
        self.click_button(self.guanjia_loc)
        logging.info('进入流量管家页面')

    def my_voucher(self):  # 我的卡券
        self.click_button(self.my_voucher_loc)
        logging.info('进入我的卡劵页面')

    def my_movie(self):  # 我的电影
        self.click_button(self.my_movie_loc)
        logging.info('进入我的电影页面')

    def xiangdan(self):  # 详单查询
        self.click_button(self.xiangdan_loc)
        logging.info('进入详单查询页面')

    def login(self):  # 点击登录
        self.click_button(self.login_loc)
        logging.info('进入登录页面')

    def kefu(self):  # 在线客服
        self.click_button(self.kefu_loc)
        logging.info('进入在线客服页面')

    def my(self):
        self.wode()
        logging.info("进入我的页面")

    def fapiao(self):  # 电子发票
        self.click_button(self.fapiao_loc)
        logging.info('进入电子发票页面')

    def shiming(self):  # 实名登记
        self.click_button(self.shiming_loc)
        logging.info('进入实名登记页面')

    def heduohao(self):  # 和多号
        self.click_button(self.heduohao_loc)
        logging.info('进入和多号页面')

    def zhineng(self):  # 智能家居
        self.click_button(self.zhineng_loc)
        logging.info('进入智能家居页面')

    def chajian(self):  # 插件
        self.click_button(self.chajian_loc)
        logging.info('进入我的插件页面')


# OK
# 张云龙代码

class Liuliang_qianbao(My):
    qianbao_loc = eval(data['Liuliang_qianbao']['qianbao_loc'])  # 流量钱包
    qianbao_yue_loc = eval(data['Liuliang_qianbao']['qianbao_yue_loc'])  # 流量钱包_余额
    bangzhu_loc = eval(data['Liuliang_qianbao']['bangzhu_loc'])  # 帮助中心
    bangzhu_pan_loc = eval(data['Liuliang_qianbao']['bangzhu_pan_loc'])  # 帮助中心
    hongbao_jilu_loc = eval(data['Liuliang_qianbao']['hongbao_jilu_loc'])  # 红包记录
    hongbao_jilu_pan_loc = eval(data['Liuliang_qianbao']['hongbao_jilu_pan_loc'])  # 收到的红包
    liuliang_mingxi_loc = eval(data['Liuliang_qianbao']['liuliang_mingxi_loc'])  # 流量明细
    liuliang_mingxi_pan_loc = eval(data['Liuliang_qianbao']['liuliang_mingxi_pan_loc'])  # 流量明细
    chongzhi_jilu_loc = eval(data['Liuliang_qianbao']['chongzhi_jilu_loc'])  # 充值记录
    chongzhi_jilu_pan_loc = eval(data['Liuliang_qianbao']['chongzhi_jilu_pan_loc'])  # 充值记录
    tiqu_jilu_loc = eval(data['Liuliang_qianbao']['tiqu_jilu_loc'])  # 提取记录
    tiqu_jilu_pan_loc = eval(data['Liuliang_qianbao']['tiqu_jilu_pan_loc'])  # 提取记录

    def qianbao(self):
        self.click_button(self.qianbao_loc)
        logging.info('点击流量钱包')

    def bangzhu(self):
        self.click_button(self.bangzhu_loc)
        logging.info('点击帮助中心')

    def hongbao_jilu(self):
        self.click_button(self.hongbao_jilu_loc)
        logging.info('点击红包记录')

    def liuliang_mingxi(self):
        self.click_button(self.liuliang_mingxi_loc)
        logging.info('点击流量明细')

    def chongzhi_jilu(self):
        self.click_button(self.chongzhi_jilu_loc)
        logging.info('点击充值记录')

    def tiqu_jilu(self):
        self.click_button(self.tiqu_jilu_loc)
        logging.info('点击提取记录')


# OK
class Yiding(My):
    yiding_loc = eval(data['Yiding']['yiding_loc'])  # 已订业务
    taocan_pan_loc = eval(data['Yiding']['taocan_pan_loc'])  # 判定，我的套餐
    zengzhi_pan_loc = eval(data['Yiding']['zengzhi_pan_loc'])  # 判定，增值业务
    jichu_pan_loc = eval(data['Yiding']['jichu_pan_loc'])  # 判定，基础功能
    qita_pan_loc = eval(data['Yiding']['qita_pan_loc'])  # 判定，其他
    gengduo_loc = eval(data['Yiding']['gengduo_loc'])  # 更多业务办理
    taocan_panyiding_loc = eval(data['Yiding']['taocan_panyiding_loc'])  # 更多业务办理
    tuiding_loc = eval(data['Yiding']['tuiding_loc'])  # 判定，基础功能页的退订按钮
    tuiding_quxiao_loc = eval(data['Yiding']['tuiding_quxiao_loc'])  # 取消
    tuiding_queding_loc = eval(data['Yiding']['tuiding_queding_loc'])  # 判定，退订提示语
    fenxiang_loc = eval(data['Yiding']['fenxiang_loc'])  # 分享
    fenxiang_pan_loc = eval(data['Yiding']['fenxiang_pan_loc'])  # 分享的二维码
    fenxiang_quxiao_loc = eval(data['Yiding']['fenxiang_quxiao_loc'])  # 取消分享
    weixin_loc = eval(data['Yiding']['weixin_loc'])  # 微信

    def gengduo(self):
        self.click_button(self.gengduo_loc)
        logging.info('点击更多')

    def jichu_pan(self):
        self.click_button(self.jichu_pan_loc)
        logging.info('点击基础功能')

    def tuiding(self):
        self.click_button(self.tuiding_loc)
        logging.info('点击退订')

    def tuiding_quxiao(self):
        self.click_button(self.tuiding_quxiao_loc)
        logging.info('点击取消')

    def fenxiang(self):
        self.click_button(self.fenxiang_loc)
        logging.info('点击分享')

    def fenxiang_quxiao(self):
        self.click_button(self.fenxiang_quxiao_loc)
        logging.info('点击分享的取消按钮')

    def weixin(self):
        self.click_button(self.weixin_loc)
        logging.info('点击微信')

    def yiding_lc(self):
        self.yiding()
        logging.info("进入已订业务")
        self.gengduo()
        logging.info("点击更多")
        self.back()
        logging.info("点击返回")
        self.jichu_pan()
        logging.info("点击基础业务")
        self.tuiding()
        logging.info("点击退订按钮")
        self.tuiding_quxiao()
        logging.info("点击取消退订")


# OK
class Balance(My):
    chongzhi_loc = eval(data['Balance']['chongzhi_loc'])  # 充值交费
    pan_chongzhi_loc = eval(data['Balance']['pan_chongzhi_loc'])  # 判定，充值交费
    yuliang_loc = eval(data['Balance']['yuliang_loc'])  # 套餐余量
    pan_yuliang_loc = eval(data['Balance']['pan_yuliang_loc'])  # 判定，套餐余量
    yuliang_back_loc = eval(data['Balance']['yuliang_back_loc'])  # 套餐余量的返回按钮
    taocan_loc = eval(data['Balance']['taocan_loc'])  # 套餐办理
    pan_taocan_loc = eval(data['Balance']['pan_taocan_loc'])  # 判定，套餐办理
    zhangdan_loc = eval(data['Balance']['zhangdan_loc'])  # 我的账单
    pan_zhangdan_loc = eval(data['Balance']['pan_zhangdan_loc'])  # 判定，我的账单
    balance_back_loc = eval(data['Balance']['balance_back_loc'])  # 话费余额的返回按钮
    quchongzhi_loc = eval(data['Balance']['quchongzhi_loc'])  # 去充值
    chongzhi_pan_loc = eval(data['Balance']['chongzhi_pan_loc'])  # 判定，充值页面
    xiaofei_loc = eval(data['Balance']['xiaofei_loc'])  # 当月消费
    keyong_loc = eval(data['Balance']['keyong_loc'])  # 可用余额

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


# OK
class Myorder(My):
    fenxiang_loc = eval(data['Myorder']['fenxiang_loc'])  # 分享订单页面
    fenxiangdao_loc = eval(data['Myorder']['fenxiangdao_loc'])  # 分享到
    fenxiang_pan_loc = eval(data['Myorder']['fenxiang_pan_loc'])  # 分享到
    ll_order_loc = eval(data['Myorder']['ll_order_loc'])  # 判定
    bh_order_loc = eval(data['Myorder']['bh_order_loc'])  # 判定流量订单
    cz_order_loc = eval(data['Myorder']['cz_order_loc'])
    czxq_order_loc = eval(data['Myorder']['czxq_order_loc'])  # 判定
    sp_order_loc = eval(data['Myorder']['sp_order_loc'])  # 判定
    spkf_order_loc = eval(data['Myorder']['spkf_order_loc'])
    kefu_1_loc = eval(data['Myorder']['kefu_1_loc'])

    def fenxiang(self):
        self.click_button(self.fenxiang_loc)
        logging.info('点击分享订单')

    def fenxiangdao(self):
        self.click_button(self.fenxiangdao_loc)
        logging.info('点击分享到')

    def sporder(self):
        self.click_button(self.sp_order_loc)
        logging.info('点击商品订单')

    def spkf_order(self):
        self.click_button(self.spkf_order_loc)
        logging.info('点击商品订单的第一个订单，进入到订单详情')

    def kefu_1(self):
        self.click_button(self.kefu_1_loc)
        logging.info('点击点击商品订单的第一个订单的客服')

    def cz_order(self):
        self.click_button(self.cz_order_loc)
        logging.info('点击充值订单')

    def ll_order(self):
        self.click_button(self.ll_order_loc)
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


# OK
class Xxdingyue(My):
    no_dingyue_loc = eval(data['Xxdingyue']['no_dingyue_loc'])  # 没有订阅消息

    def Xxdingyue_lc(self):
        self.swipe_up()
        logging.info("向下滑动")
        self.dingyue()
        logging.info("进入消息订阅")


# OK---------
class Guanjia(My):
    dingdan_loc = eval(data['Guanjia']['dingdan_loc'])
    dingdan_pan_loc = eval(data['Guanjia']['dingdan_pan_loc'])
    zhichong_loc = eval(data['Guanjia']['zhichong_loc'])
    zhichong_pan_loc = eval(data['Guanjia']['zhichong_pan_loc'])
    shangpin_loc = eval(data['Guanjia']['shangpin_loc'])
    shangpin_pan_loc = eval(data['Guanjia']['shangpin_pan_loc'])
    xiangdan_loc = eval(data['Guanjia']['xiangdan_loc'])
    xiangdan_pan_loc = eval(data['Guanjia']['xiangdan_pan_loc'])
    xiangdanback_pan_loc = eval(data['Guanjia']['xiangdanback_pan_loc'])
    bannian_loc = eval(data['Guanjia']['bannian_loc'])
    liuliang_pan_loc = eval(data['Guanjia']['liuliang_pan_loc'])
    jibao_loc = eval(data['Guanjia']['jibao_loc'])
    ri_taocan_loc = eval(data['Guanjia']['ri_taocan_loc'])
    shiping_loc = eval(data['Guanjia']['shiping_loc'])
    yuedu_loc = eval(data['Guanjia']['yuedu_loc'])
    yinyue_loc = eval(data['Guanjia']['yinyue_loc'])

    def dingdan(self):
        self.click_button(self.dingdan_loc)

    def zhichong(self):
        self.click_button(self.zhichong_loc)

    def shangpin(self):
        self.click_button(self.shangpin_loc)

    def xiangdan(self):
        self.click_button(self.xiangdan_loc)

    def bannian(self):
        self.click_button(self.bannian_loc)  # 流量半年包

    def jibao(self):
        self.click_button(self.jibao_loc)  # 流量季包

    def ri_taocan(self):
        self.click_button(self.ri_taocan_loc)  # 流量日套餐

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


# OK
class My_voucher(My):
    no_shiyongxuan_loc = eval(data['My_voucher']['no_shiyongxuan_loc'])  # 判定
    kajuan_lishi_loc = eval(data['My_voucher']['kajuan_lishi_loc'])  # 判定
    yiguoqi_loc = eval(data['My_voucher']['yiguoqi_loc'])  # 判定
    yishiyong_loc = eval(data['My_voucher']['yishiyong_loc'])  # 判定
    no_kajuan_loc = eval(data['My_voucher']['no_kajuan_loc'])  # 判定
    migu_loc = eval(data['My_voucher']['migu_loc'])

    def kajuan_lishi(self):
        self.click_button(self.kajuan_lishi_loc)

    def yiguoqi(self):
        self.click_button(self.yiguoqi_loc)

    def yishiyong(self):
        self.click_button(self.yishiyong_loc)

    def migu(self):
        self.click_button(self.migu_loc)

    def ka_juan(self):
        self.my_voucher()
        logging.info("进入我的卡劵")
        self.yiguoqi()
        logging.info("点击已过期")
        self.yishiyong()
        logging.info("点击已使用")
        self.migu()
        logging.info("点击咪咕电影劵")
        self.back()
        logging.info("点击返回")


# OK
class My_movie(My):
    gou_piao_loc = eval(data['My_movie']['gou_piao_loc'])  # 判定
    gou_piaoclose_loc = eval(data['My_movie']['gou_piaoclose_loc'])  # 判定

    def gou_piao(self):
        self.click_button(self.gou_piao_loc)

    def gou_piaoclose(self):
        self.click_button(self.gou_piaoclose_loc)

    def dian_ying(self):
        self.my_movie()
        logging.info("进入我的电影")


class Xiangdan(My):
    renzheng_loc = eval(data['Xiangdan']['renzheng_loc'])  # 详单的身份认证
    jiansuo_loc = eval(data['Xiangdan']['jiansuo_loc'])
    anniu_loc = eval(data['Xiangdan']['anniu_loc'])  # 按号码的下拉按钮
    haoma_loc = eval(data['Xiangdan']['haoma_loc'])  # 按号码
    riqi_loc = eval(data['Xiangdan']['riqi_loc'])  # 按日期
    mingcheng_loc = eval(data['Xiangdan']['mingcheng_loc'])  # 按名称
    shuru_loc = eval(data['Xiangdan']['shuru_loc'])  # 检索的输入框
    sousuo_loc = eval(data['Xiangdan']['sousuo_loc'])  # 搜索按钮
    tonghua_loc = eval(data['Xiangdan']['tonghua_loc'])
    fenxi_loc = eval(data['Xiangdan']['fenxi_loc'])  # 详单分析
    pan_gaisu_loc = eval(data['Xiangdan']['pan_gaisu_loc'])  # 判定
    pan_meiri_loc = eval(data['Xiangdan']['pan_meiri_loc'])  # 判定
    pan_time_loc = eval(data['Xiangdan']['pan_time_loc'])  # 判定

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


# OK
class Taocan_xq(My):
    qianbao_loc = eval(data['Taocan_xq']['qianbao_loc'])  # 余额
    qianbao_pan_loc = eval(data['Taocan_xq']['qianbao_pan_loc'])  # 余额  #流量钱包判定
    kajuan_loc = eval(data['Taocan_xq']['kajuan_loc'])  # 卡劵
    kajuan_pan_loc = eval(data['Taocan_xq']['kajuan_pan_loc'])  # 卡劵判定
    jifen_loc = eval(data['Taocan_xq']['jifen_loc'])  # 积分
    jifen_pan_loc = eval(data['Taocan_xq']['jifen_pan_loc'])  # 积分判定
    quanyi_loc = eval(data['Taocan_xq']['quanyi_loc'])  # 我的权益
    quanyi_pan_loc = eval(data['Taocan_xq']['quanyi_pan_loc'])  # 我的权益判定

    def qianbao(self):
        self.click_button(self.qianbao_loc)

    def kajuan(self):
        self.click_button(self.kajuan_loc)

    def jifen(self):
        self.click_button(self.jifen_loc)

    def quanyi(self):
        self.click_button(self.quanyi_loc)


# OK
class Ke_fu(My):
    send_loc = eval(data['Ke_fu']['send_loc'])  # 点击登录

    def send(self):
        self.click_button(self.send_loc)

    def Kefu_lc(self):
        self.swipe_up()
        logging.info("向下滑动")
        self.kefu()
        logging.info("进入在线客服")


# OK
class Geren(My):  # 个人信息
    # 权限元素
    bianji_loc = eval(data['Geren']['bianji_loc'])
    imgexit_loc = eval(data['Geren']['imgexit_loc'])
    touxiang_loc = eval(data['Geren']['touxiang_loc'])

    def bianji(self):  # 编辑头像
        self.click_button(self.bianji_loc)

    def imgexit(self):  # 取消头像
        self.click_button(self.imgexit_loc)

    def touxiang(self):  # 取消头像
        self.click_button(self.touxiang_loc)

    def geren_lc(self):
        self.imglogin()
        logging.info("进入个人信息")
        self.bianji()
        logging.info("点击编辑")
        self.imgexit()
        logging.info("点击取消")
        self.back()
        logging.info("点击返回")


# OK
class Zhangdan(My):  # 我的账单
    # 权限元素
    zhangdan_zonge_loc = eval(data['Zhangdan']['zhangdan_zonge_loc'])  # 判定，账单总额
    qu_chongzhi_loc = eval(data['Zhangdan']['qu_chongzhi_loc'])  # 去充值
    chongzhi_zhongxin_loc = eval(data['Zhangdan']['chongzhi_zhongxin_loc'])  # 判定，充值中心
    chongzhi_back_loc = eval(data['Zhangdan']['chongzhi_back_loc'])  # 充值中心的返回按钮
    xiangdan_loc = eval(data['Zhangdan']['xiangdan_loc'])  # 详单查询
    xiangdan_panding_loc = eval(data['Zhangdan']['xiangdan_panding_loc'])  # 判定，详单查询
    xiangdanback_loc = eval(data['Zhangdan']['xiangdanback_loc'])  # 详单查询的返回按钮
    zhangdan_fenxiang_loc = eval(data['Zhangdan']['zhangdan_fenxiang_loc'])  # 我的账单分享
    fenxiang_panding_loc = eval(data['Zhangdan']['fenxiang_panding_loc'])  # 判定，分享
    quxiao_fenxiang_loc = eval(data['Zhangdan']['quxiao_fenxiang_loc'])  # 取消分享
    zhangdanback_loc = eval(data['Zhangdan']['zhangdanback_loc'])  # 账单的返回（我的）按钮

    def qu_chongzhi(self):  # 去充值
        self.click_button(self.qu_chongzhi_loc)

    def chongzhiback(self):  # 充值中心的返回按钮
        self.click_button(self.chongzhi_back_loc)

    def xiangdan(self):  # 详单查询
        self.click_button(self.xiangdan_loc)

    def xiangdanback(self):  # 详单查询的返回按钮
        self.click_button(self.xiangdanback_loc)

    def zhanndan_fenxiang(self):  # 我的账单分享
        self.click_button(self.zhangdan_fenxiang_loc)

    def quxiao(self):  # 取消分享
        self.click_button(self.quxiao_fenxiang_loc)

    def zhangdanback(self):  # 账单的返回（我的）按钮
        self.click_button(self.zhangdanback_loc)

    def zhangdan_lc(self):
        self.my_zhangdan()
        logging.info("进入我的账单")
        self.qu_chongzhi()
        logging.info("点击去充值")
        self.chongzhiback()
        logging.info("返回")
        #    self.yuliang()
        logging.info("点击套餐余量")
        #  self.yuliang_back()
        logging.info("点击套餐余量的返回按钮")
        self.xiangdan()
        logging.info("点击详单查询")
        self.xiangdanback()
        logging.info("点击详单查询的返回按钮")


# 一半
class Payhistory(My):
    jiaofei_pan_loc = eval(data['Payhistory']['jiaofei_pan_loc'])
    chongzhi_pan_loc = eval(data['Payhistory']['chongzhi_pan_loc'])  # 充值中心
    shaixuan_loc = eval(data['Payhistory']['shaixuan_loc'])
    shouqi_loc = eval(data['Payhistory']['shouqi_loc'])
    fenxiang_loc = eval(data['Payhistory']['fenxiang_loc'])
    pengyouquan_loc = eval(data['Payhistory']['pengyouquan_loc'])
    quxiao_loc = eval(data['Payhistory']['fenxiang_loc'])
    siyue_loc = eval(data['Payhistory']['siyue_loc'])
    erweima_loc = eval(data['Payhistory']['erweima_loc'])

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


# 李纯代码
# 李纯代码
class Qinmifu(My):  # 亲密付
    # 权限元素
    qmf_dingdan_pan_loc = eval(data['Qinmifu']['qmf_dingdan_pan_loc'])  # 判定，亲密付订单
    qmf_jilu_pan_loc = eval(data['Qinmifu']['qmf_jilu_pan_loc'])  # 判定，添加记录
    qmf_tianjia_pan_loc = eval(data['Qinmifu']['qmf_tianjia_pan_loc'])  # 判定，添加号码
    liuliang_pan_loc = eval(data['Qinmifu']['liuliang_pan_loc'])  # 判定，亲密付流量订单
    chongzhi_pan_loc = eval(data['Qinmifu']['chongzhi_pan_loc'])  # 判定，亲密付充值订单
    chongzhi_loc = eval(data['Qinmifu']['chongzhi_loc'])  # 充值订单
    liuliang_loc = eval(data['Qinmifu']['liuliang_loc'])  # 流量订单
    chongliuliang_loc = eval(data['Qinmifu']['chongliuliang_loc'])  # 冲流量
    chonghuafei_loc = eval(data['Qinmifu']['chonghuafei_loc'])  # 充话费
    lijichong_loc = eval(data['Qinmifu']['lijichong_loc'])  # 立即充值
    queren_loc = eval(data['Qinmifu']['queren_loc'])  # 确认支付
    close_anniu_loc = eval(data['Qinmifu']['close_anniu_loc'])  # 关闭支付页面
    querenpay_loc = eval(data['Qinmifu']['querenpay_loc'])  # 确认支付完成
    close_zhifu_loc = eval(data['Qinmifu']['close_zhifu_loc'])  # 关闭支付页面
    tianjiajilu_loc = eval(data['Qinmifu']['tianjiajilu_loc'])  # 添加记录
    beitianjiajilu_loc = eval(data['Qinmifu']['beitianjiajilu_loc'])  # 被添加记录
    pan_tianjiajilu_loc = eval(data['Qinmifu']['pan_tianjiajilu_loc'])  # 判定，添加记录
    pan_beitianjiajilu_loc = eval(data['Qinmifu']['pan_beitianjiajilu_loc'])  # 判定，被添加记录
    pan_chaoshijilu_loc = eval(data['Qinmifu']['pan_chaoshijilu_loc'])  # 判定，超时未回复
    pan_qinmifu_loc = eval(data['Qinmifu']['pan_qinmifu_loc'])  # 判定亲密付
    pan_liuliang_loc = eval(data['Qinmifu']['pan_liuliang_loc'])  # 判定充流量页面
    pan_huafei_loc = eval(data['Qinmifu']['pan_huafei_loc'])  # 判定充话费页面
    back_loc = eval(data['Qinmifu']['back_loc'])  # 返回_
    chongzhijilu_loc = eval(data['Qinmifu']['chongzhijilu_loc'])  # 充值记录
    tianjiahaoma_loc = eval(data['Qinmifu']['tianjiahaoma_loc'])  # 添加号码
    haomashurulan_loc = eval(data['Qinmifu']['haomashurulan_loc'])  # 号码输入栏
    shurunicheng_loc = eval(data['Qinmifu']['shurunicheng_loc'])  # 输入昵称栏
    quxiao_loc = eval(data['Qinmifu']['quxiao_loc'])  # 取消
    pan_quxiao_loc = eval(data['Qinmifu']['pan_quxiao_loc'])  # 判定取消
    lijitianjia_loc = eval(data['Qinmifu']['lijitianjia_loc'])  # 立即添加
    pan_lijitianjia_loc = eval(data['Qinmifu']['pan_lijitianjia_loc'])  # 判定 立即添加
    guanli_loc = eval(data['Qinmifu']['guanli_loc'])  # 管理成员
    pan_guanli_loc = eval(data['Qinmifu']['pan_guanli_loc'])  # 判定 管理成员

    def tianjiahaoma(self):  # 添加号码
        self.click_button(self.tianjiahaoma_loc)
        logging.info("添加号码")

    def haomashurulan(self, value1):  # 号码输入栏
        self.send_keys(self.haomashurulan_loc, value1)
        logging.info("号码输入栏")

    def shurunicheng(self, value2):  # 昵称输入栏
        self.send_keys(self.shurunicheng_loc, value2)
        logging.info("昵称输入")

    def quxiao(self):  # 取消
        self.click_button(self.quxiao_loc)
        logging.info("取消")

    def lijitianjia(self):  # 立即添加
        self.click_button(self.lijitianjia_loc)
        logging.info("立即添加")

    def guanli(self):  # 管理成员
        self.tap(635.7, 237.1)
        self.click_button(self.guanli_loc)
        logging.info("管理成员")

    def chongzhi(self):  # 亲密付充值订单
        self.click_button(self.chongzhi_loc)
        logging.info("点击亲密付充值订单")

    def liuliang(self):  # 亲密付流量订单
        self.click_button(self.liuliang_loc)
        logging.info("点击亲密付流量订单")

    def chongliuliang(self):  # 冲流量
        self.click_button(self.chongliuliang_loc)
        logging.info("点击充流量")

    def chonghuafei(self):  # 充话费
        self.click_button(self.chonghuafei_loc)
        logging.info("点击充话费")

    def lijichong(self):  # 立即充值
        self.click_button(self.lijichong_loc)
        logging.info("点击立即充值")

    def queren(self):  # 确认支付
        self.click_button(self.queren_loc)
        logging.info("点击确认支付")

    def close_zhifu(self):  # 关闭支付页面
        self.click_button(self.close_zhifu_loc)
        logging.info("点击关闭支付")

    def tianjiajilu(self):  # 添加记录
        self.tap(635.7, 237.1)
        self.click_button(self.tianjiajilu_loc)
        logging.info("点击添加记录")

    def beitianjiajilu(self):  # 被添加记录
        self.click_button(self.beitianjiajilu_loc)
        logging.info("点击被添加记录")

    def chongzhijilu(self):
        self.tap(635.7, 237.1)
        self.click_button(self.chongzhijilu_loc)
        logging.info("点击充值记录")

    def back(self):  # 返回
        self.click_button(self.back_loc)
        logging.info("点击返回")

    def tianhaoquxiao(self):  # 添加号码时取消
        self.tianjiahaoma()
        logging.info("点击添加号码")
        self.haomashurulan("18723240750")
        logging.info("点击号码输入栏")
        self.shurunicheng("cheshi")
        logging.info("点击昵称输入栏")
        self.quxiao()
        logging.info("点击取消")

    def tianhao(self):  # 添加号码
        self.tianjiahaoma()
        logging.info("点击添加号码")
        self.haomashurulan("18723240750")
        logging.info("点击号码输入栏")
        self.shurunicheng("cheshi")
        logging.info("点击昵称输入栏")
        self.lijitianjia()
        logging.info("点击立即添加")


class FaPiao(My):
    # 话费充值发票入口
    huafei_loc = eval(data['FaPiao']['huafei_loc'])
    # 流量直充发票入口
    liuliang_loc = eval(data['FaPiao']['liuliang_loc'])
    # 宽带发票入口
    kuandai_loc = eval(data['FaPiao']['kuandai_loc'])
    # 月结发票入口
    yuejie_loc = eval(data['FaPiao']['yuejie_loc'])
    # 发票抬头入口
    taitou_loc = eval(data['FaPiao']['taitou_loc'])
    # 点击新增发票
    xinzeng_loc = eval(data['FaPiao']['xinzeng_loc'])
    # 点击发票抬头输入栏
    riseinput_loc = eval(data['FaPiao']['riseinput_loc'])
    # 点击纳税人识别号输入栏
    shibiehao_loc = eval(data['FaPiao']['shibiehao_loc'])
    # 设为默认按钮
    moren_loc = eval(data['FaPiao']['moren_loc'])
    # 点击保存按钮
    baocun_loc = eval(data['FaPiao']['baocun_loc'])
    # 邮件推送入口
    youtui_loc = eval(data['FaPiao']['youtui_loc'])
    # 点击常用邮箱输入栏
    mail_loc = eval(data['FaPiao']['mail_loc'])
    # 点击保存按钮
    save_loc = eval(data['FaPiao']['save_loc'])
    # 知道了按钮
    zhidaole_loc = eval(data['FaPiao']['zhidaole_loc'])
    # 返回按钮
    back_loc = eval(data['FaPiao']['back_loc'])
    # 关闭按钮
    close_loc = eval(data['FaPiao']['close_loc'])
    # 点击开具按钮
    kaiju_loc = eval(data['FaPiao']['kaiju_loc'])
    # 停止开具按钮
    tingkai_loc = eval(data['FaPiao']['tingkai_loc'])
    # 确认开具按钮
    quekai_loc = eval(data['FaPiao']['quekai_loc'])
    # 判定话费充值发票页面
    pan_huafei_loc = eval(data['FaPiao']['pan_huafei_loc'])
    # 判定流量直充发票页面
    pan_liuliang_loc = eval(data['FaPiao']['pan_liuliang_loc'])
    # 判定宽带发票页面
    pan_kuandai_loc = eval(data['FaPiao']['pan_kuandai_loc'])
    # 判定月结发票页面
    pan_yuejie_loc = eval(data['FaPiao']['pan_yuejie_loc'])
    # 判定发票抬头页面
    pan_taitou_loc = eval(data['FaPiao']['pan_taitou_loc'])
    # 判定新增发票页面
    pan_xinzeng_loc = eval(data['FaPiao']['pan_xinzeng_loc'])
    # 判定已成功新增发票
    danwei_loc = eval(data['FaPiao']['danwei_loc'])
    # 判定推送邮箱
    pan_tuisong_loc = eval(data['FaPiao']['pan_tuisong_loc'])
    # 判定邮箱保存
    pan_youxiang_loc = eval(data['FaPiao']['pan_youxiang_loc'])

    # 判定停止开具

    # 点击话费充值发票
    def huafei(self):
        self.click_button(self.huafei_loc)
        logging.info("点击话费充值发票")
        # 点击流量直充发票

    def liuliang(self):
        self.click_button(self.liuliang_loc)
        logging.info("点击流量直充发票")
        # 点击宽带发票

    def kuandai(self):
        self.click_button(self.kuandai_loc)
        logging.info("点击宽带发票")
        # 点击月结发票

    def yuejie(self):
        self.click_button(self.yuejie_loc)
        logging.info("点击月结发票")
        # 点击发票抬头

    def taitou(self):
        self.click_button(self.taitou_loc)
        logging.info("点击发票抬头")
        # 点击新增发票

    def xinzeng(self):
        self.click_button(self.xinzeng_loc)
        logging.info("点击新增发票")
        # 点击抬头输入栏

    def riseinput(self, value1):
        self.send_keys(self.riseinput_loc, value1)
        logging.info("点击发票抬头输入栏")
        # 点击识别号输入栏

    def shibiehao(self, value2):
        self.send_keys(self.shibiehao_loc, value2)
        logging.info("点击纳税人识别号输入栏")
        # 点击默认

    def moren(self):
        self.click_button(self.moren_loc)
        logging.info("点击默认")
        # 点击保存

    def baocun(self):
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

    def kaiju(self):
        self.click_button(self.kaiju_loc)
        logging.info("点击开具")

        #  点击停止开具

    def tingkai(self):
        self.click_button(self.tingkai_loc)
        logging.info("点击停止开具")
        # 点击确认开具

    def quekai(self):
        self.click_button(self.quekai_loc)
        logging.info("点击确认开具")
        # 点击邮箱推送

    def youtui(self):
        self.click_button(self.youtui_loc)
        logging.info("点击邮箱推送")
        # 输入邮箱号

    def mail(self, value3):
        self.send_keys(self.mail_loc, value3)
        # self.send_keys(self.mail_loc, value1)
        logging.info("点击邮箱号")
        # self.find_element(self.mail_loc).clear()

        # 点击保存

    def save(self):
        self.click_button(self.save_loc)
        logging.info("点击保存")

    def xinfapiao(self, value1, value2):  # 新增一个发票
        self.fapiao()
        logging.info("进入电子发票")
        self.taitou()
        logging.info("进入发票抬头")
        self.xinzeng()
        logging.info("新增发票")
        self.riseinput(value1)
        logging.info("抬头栏输入")
        # 点击纳税人识别号输入栏输入内容
        self.shibiehao(value2)
        logging.info("识别栏输入")
        # 点击默认，点击保存
        self.moren()
        self.baocun()
        self.back()


class ShiMing(My):
    pan_shiming_loc = eval(data['ShiMing']['pan_shiming_loc'])  # 判实名登记
    back_loc = eval(data['ShiMing']['back_loc'])  # 返回

    # 返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")


class HeDuoHao(My):
    pan_heduohao_loc = eval(data['HeDuoHao']['pan_heduohao_loc'])  # 判和多号
    back_loc = eval(data['ShiMing']['back_loc'])  # 返回

    # 点击返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")


class ZhiNeng(My):
    wangguan_loc = eval(data['ZhiNeng']['wangguan_loc'])  # 网关管理
    shebei_loc = eval(data['ZhiNeng']['shebei_loc'])  # 设备管理
    baokuan_loc = eval(data['ZhiNeng']['baokuan_loc'])  # 爆款商品
    pan_zhineng_loc = eval(data['ZhiNeng']['pan_zhineng_loc'])  # 判定智能家居
    pan_wangguan_loc = eval(data['ZhiNeng']['pan_wangguan_loc'])  # 判定网关管理
    pan_shebei_loc = eval(data['ZhiNeng']['pan_shebei_loc'])  # 判定设备管理
    pan_baokuan_loc = eval(data['ZhiNeng']['pan_baokuan_loc'])  # 判定爆款商品
    back_loc = eval(data['ZhiNeng']['back_loc'])  # 返回
    wangguan_back_loc = eval(data['ZhiNeng']['wangguan_back_loc'])  # 网关管理页面返回
    shebei_back_loc = eval(data['ZhiNeng']['shebei_back_loc'])  # 设备管理页面返
    close_loc = eval(data['ZhiNeng']['close_loc'])  # 关闭

    # 点击网关管理
    def wangguan(self):
        self.click_button(self.wangguan_loc)
        logging.info("点击网关管理")

    # 点击设备管理
    def shebei(self):
        self.click_button(self.shebei_loc)
        logging.info("点击设备管理")

    # 点击爆款商品
    def baokuan(self):
        self.click_button(self.baokuan_loc)
        logging.info("点击爆款商品")

    # 点击返回
    def back(self):
        self.click_button(self.back_loc)
        logging.info("点击返回")

    # 点击网关管理返回
    def wangguan_back(self):
        self.click_button(self.wangguan_back_loc)
        logging.info("点击网关管理返回")

    # 点击设备管理返回
    def shebei_back(self):
        self.click_button(self.shebei_back_loc)
        logging.info("点击设备管理返回")

    # 点击关闭
    def close(self):
        self.click_button(self.close_loc)
        logging.info("点击关闭")


class ChaJian(My):
    pan_chajian_loc = eval(data['ChaJian']['pan_chajian_loc'])  # 判定插件中心
    fenxiang_loc = eval(data['ChaJian']['fenxiang_loc'])  # 分享按钮
    pan_fenxiang_loc = eval(data['ChaJian']['pan_fenxiang_loc'])  # 判定分享
    quxiao_loc = eval(data['ChaJian']['quxiao_loc'])  # 取消按钮
    back_loc = eval(data['ChaJian']['back_loc'])  # 返回

    # 点击分享
    def fenxiang(self):
        self.click_button(self.fenxiang_loc)
        logging.info("点击进入分享")

    # 点击取消
    def quxiao(self):
        self.click_button(self.quxiao_loc)
        logging.info("点击取消")

    # 点击返回
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
