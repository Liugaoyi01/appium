#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import sys, os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
import io
import time
from auto_test_client.businessView import shouyepage,mypage,loginpage
from auto_test_client.businessView.mypage import My
import yaml
from auto_test_client.businessView.loginpage import Login
from auto_test_client.public.desired_caps import appium_desired
import logging

driver = appium_desired()

def setup_module():  # 整个.py模块启动一次客户端,进入我的页面
    base = Login(driver)
    base.start()
    time.sleep(3)
    base.wode()
#    base.tap(970,1850)
    base.denglu()
    base.login('13501585305')
    wodea = My(driver)

def teardown_module():  # 整个.py模块退出客户端
    driver.close_app()


#曾威代码
class TestMY():
    def test_xingji(self):  # 是否有星级标识
        biaoshi = mypage.My(driver)
        biaoshi.xjbs()
        try:
            assert biaoshi.try_find(mypage.My.touxiang_loc) is True
            logging.info("星级标识")
        except:
            logging.warning("找不到标识")
            biaoshi.get_screenshot("星级标识")
            raise
        finally:
            biaoshi.back()

#张云龙代码

class TestLl_qianbao():
    def setup(self):  # ，每次进入流量钱包
        qianbao = mypage.Liuliang_qianbao(driver)
        qianbao.qianbao()
        logging.info("进入流量钱包")

    def teardown(self):  # 每次返回
        qianbao = mypage.Liuliang_qianbao(driver)
        qianbao.back()
        logging.info("返回")

    def test_balance(self):  # 能否显示流量钱包的余额
        qianbao = mypage.Liuliang_qianbao(driver)
        try:
            assert qianbao.try_find(mypage.Liuliang_qianbao.qianbao_yue_loc) is True
            logging.info('显示流量钱包的余额')
        except:
            logging.warning("找不到流量钱包的余额")
            qianbao.get_screenshot("找不到流量钱包的余额")
            raise
    def test_mingxi(self):     #能否进入到流量明细页面
        qianbao = mypage.Liuliang_qianbao(driver)
        qianbao.liuliang_mingxi()
        try:
            assert qianbao.try_find(mypage.Liuliang_qianbao.liuliang_mingxi_pan_loc) is True
            logging.info('进入到流量明细页面')
        except:
            logging.warning("找不到流量明细页面")
            qianbao.get_screenshot("找不到流量明细页面")
            raise
        finally:
            qianbao.back()
    def test_chongzhi_jilu(self):     #能否进入到充值记录页面
        qianbao = mypage.Liuliang_qianbao(driver)
        qianbao.chongzhi_jilu()
        try:
            assert qianbao.try_find(mypage.Liuliang_qianbao.chongzhi_jilu_pan_loc) is True
            logging.info('进入到充值记录页面')
        except:
            logging.warning("找不到充值记录页面")
            qianbao.get_screenshot("找不到充值记录页面")
            raise
        finally:
            qianbao.back()
    def test_tiqu_jilu(self):     #能否进入到提取记录页面
        qianbao = mypage.Liuliang_qianbao(driver)
        qianbao.tiqu_jilu()
        try:
            assert qianbao.try_find(mypage.Liuliang_qianbao.tiqu_jilu_pan_loc) is True
            logging.info('进入到提取记录页面')
        except:
            logging.warning("找不到提取记录页面")
            qianbao.get_screenshot("找不到提取记录页面")
            raise
        finally:
            qianbao.back()
    def test_hongbao_jilu(self):     #能否进入到红包记录页面
        qianbao = mypage.Liuliang_qianbao(driver)
        qianbao.hongbao_jilu()
        try:
            assert qianbao.try_find(mypage.Liuliang_qianbao.hongbao_jilu_pan_loc) is True
            logging.info('进入到红包记录页面')
        except:
            logging.warning("找不到红包记录页面")
            qianbao.get_screenshot("找不到红包记录页面")
            raise
        finally:
            qianbao.back()

class TestTaocan_xq():
    def test_liuliang_qianbao(self):  # 是否进入流量钱包页面
        taocan = mypage.Taocan_xq(driver)
        taocan.qianbao()
        try:
            assert taocan.try_find(mypage.Taocan_xq.qianbao_pan_loc) is True
            logging.info("进入流量钱包页面")
        except:
            logging.warning("无法进入流量钱包页面")
            taocan.get_screenshot("无法进入流量钱包页面")
            raise
        finally:
            taocan.back()
    def test_kajuan(self):  # 是否进入卡劵页面
        taocan = mypage.Taocan_xq(driver)
        taocan.kajuan()
        try:
            assert taocan.try_find(mypage.Taocan_xq.kajuan_pan_loc) is True
            logging.info("进入卡劵页面")
        except:
            logging.warning("无法进入卡劵页面")
            taocan.get_screenshot("无法进入卡劵页面")
            raise
        finally:
            taocan.close()
    def test_jifen(self):  # 是否进入积分页面
        taocan = mypage.Taocan_xq(driver)
        taocan.jifen()
        try:
            assert taocan.try_find(mypage.Taocan_xq.jifen_pan_loc) is True
            logging.info("进入积分页面")
        except:
            logging.warning("无法进入积分页面")
            taocan.get_screenshot("无法进入积分页面")
            raise
        finally:
            taocan.back()
    def test_quanyi(self):  # 是否进入我的权益页面
        taocan = mypage.Taocan_xq(driver)
        taocan.quanyi()
        try:
            assert taocan.try_find(mypage.Taocan_xq.quanyi_pan_loc) is True
            logging.info("进入我的权益页面")
        except:
            logging.warning("无法进入我的权益页面")
            taocan.get_screenshot("无法进入我的权益页面")
            raise
        finally:
            taocan.close()

class TestBalance():
    def setup(self):  # 每次进入话费余额
        yue = mypage.Balance(driver)
        yue.balance()
        logging.info('-------进入话费余额----------')
        # logging.info("进入话费余额")

    def teardown(self):  # 每次返回
        yue = mypage.Balance(driver)
        yue.balance_back()
        logging.info('-------返回----------')
        #       logging.info("返回")
    @pytest.mark.skip(reason="5.7版本未配置充值交费")
    def test_chongzhi_jiaofei(self):  # 是否进入充值交费
        yue = mypage.Balance(driver)
        yue.chongzhi()
        try:
            assert yue.try_find(mypage.Balance.pan_chongzhi_loc) is True
            logging.info('进入充值交费')
        except:
            logging.warning("无法进入充值交费")
            yue.get_screenshot("无法进入充值交费")
            raise
        finally:
            yue.back()
    @pytest.mark.skip(reason="5.7版本未配置套餐余量")
    def test_taocan_yuliang(self):  # 是否进入套餐余量
        yue = mypage.Balance(driver)
        yue.yuliang()
        try:
            assert yue.try_find(mypage.Balance.pan_yuliang_loc) is True
            logging.info('进入套餐余量')
        except:
            logging.warning("无法进入套餐余量")
            yue.get_screenshot("无法进入套餐余量")
            raise
        finally:
            yue.yuliang_back()
    @pytest.mark.skip(reason="5.7版本未配置套餐办理")
    def test_taocan_banli(self):  # 是否进入套餐办理
        yue = mypage.Balance(driver)
        yue.taocan()
        try:
            assert yue.try_find(mypage.Balance.pan_taocan_loc) is True
            logging.info('进入套餐办理')
        except:
            logging.warning("无法进入套餐办理")
            yue.get_screenshot("无法进入套餐办理")
            raise
        finally:
            yue.back()
    @pytest.mark.skip(reason="5.7版本未配置我的账单")
    def test_zhangdan(self):  # 能否进入我的账单
        yue = mypage.Balance(driver)
        yue.zhangdan()
        try:
            assert yue.try_find(mypage.Balance.pan_zhangdan_loc) is True
            logging.info('无法进入我的账单')
        except:
            logging.warning("无法进入我的账单")
            yue.get_screenshot("无法进入我的账单")
            raise
        finally:
            yue.back()

    def test_xiaofei(self):  # 是否显示当前消费
        yue = mypage.Balance(driver)
        try:
            assert yue.try_find(yue.xiaofei_loc) is True
            logging.info('显示当前消费')
        except:
            logging.warning("不显示当前消费")
            yue.get_screenshot("不显示当前消费")
            raise

    def test_yue(self):  # 是否显示可用余额
        yue = mypage.Balance(driver)
        try:
            assert yue.try_find(yue.keyong_loc) is True
            logging.info('显示可用余额')
        except:
            logging.warning("不显示可用余额")
            yue.get_screenshot("不显示可用余额")
            raise

    def test_qu_chongzhi(self):  # 去充值按钮是否可用
        yue = mypage.Balance(driver)
        yue.quchongzhi()
        try:
            assert yue.try_find(yue.chongzhi_pan_loc) is True
            logging.info('进入到去充值页面')
        except:
            logging.warning("无法进入到去充值页面")
            yue.get_screenshot("无法进入到去充值页面")
            raise
        finally:
            yue.back()

class TestYiding():
    def setup(self):  # 每次进入已订业务
        yiding = mypage.Yiding(driver)
        time.sleep(2)
        yiding.yiding()
        logging.info('进入已订业务')

    def teardown(self):  # 每次返回
        yiding = mypage.Yiding(driver)
        yiding.back()
        logging.info('返回')

    def test_taocan(self):  # 是否存在套餐业务
        yiding = mypage.Yiding(driver)
        try:
            assert yiding.try_find(mypage.Yiding.taocan_pan_loc) is True
            logging.info('找到套餐业务')
        except:
            logging.warning("找不到套餐业务")
            yiding.get_screenshot("找不到套餐业务")
            raise

    def test_zengzhi(self):  # 是否存在增值业务
        yiding = mypage.Yiding(driver)
        try:
            assert yiding.try_find(mypage.Yiding.zengzhi_pan_loc) is True
            logging.info('找到增值业务')
        except:
            logging.warning("找不到增值业务")
            yiding.get_screenshot("找不到增值业务")
            raise

    def test_jichu(self):  # 是否存在基础业务
        yiding = mypage.Yiding(driver)
        try:
            assert yiding.try_find(mypage.Yiding.jichu_pan_loc) is True
            logging.info('找到基础业务')
        except:
            logging.warning("找不到基础业务")
            yiding.get_screenshot("找不到基础业务")
            raise

    def test_taocan_dinggou(self):  # 能否进入套餐订购页面
        yiding = mypage.Yiding(driver)
        yiding.gengduo()
        logging.info("点击更多")
        try:
            assert yiding.try_find(mypage.Yiding.taocan_panyiding_loc) is True
            logging.info('点击更多跳到套餐订购页面')
        except:
            logging.warning("点击更多无法跳到套餐订购页面")
            yiding.get_screenshot("点击更多无法跳到套餐订购页面")
            raise
        finally:
            yiding.back()

    def test_tuiding(self):  # 是否存在退订按钮
        yiding = mypage.Yiding(driver)
        yiding.jichu_pan()
        logging.info("点击基础功能")
        try:
            assert yiding.try_find(mypage.Yiding.tuiding_loc) is True
            logging.info('找到退订的按钮')
        except:
            logging.warning("找不到退订的按钮")
            yiding.get_screenshot("找不到退订的按钮")
            raise

    def test_fenxiang(self):  # 验证分享按钮是否可用
        yiding = mypage.Yiding(driver)
        yiding.fenxiang()
        logging.info("点击分享按钮")
        try:
            assert yiding.try_find(yiding.fenxiang_pan_loc) is True
            logging.info('找到要分享的二维码')
        except:
            logging.warning("找不到要分享的二维码")
            yiding.get_screenshot("找不到要分享的二维码")
            raise
        finally:
            yiding.fenxiang_quxiao()
            logging.info("取消分享")
    def test_tuiding_anniu(self):  # 验证退订按钮是否可用
        yiding = mypage.Yiding(driver)
        yiding.jichu_pan()
        logging.info("点击基础功能")
        yiding.tuiding()
        logging.info("点击退订")
        try:
            assert yiding.try_find(mypage.Yiding.tuiding_queding_loc) is True
            logging.info('找到退订的确定按钮')
        except:
            logging.warning("找不到退订的确定按钮")
            yiding.get_screenshot("找不到退订的确定按钮")
            raise
        finally:
            yiding.tuiding_quxiao()
            logging.info("点击取消")

class TestMyorder():
    def setup(self):  # 每次进入我的订单
        myoder = mypage.Myorder(driver)
        myoder.my_order()
        logging.info('进入我的订单')
        #       logging.info("进入我的订单")

    def teardown(self):  # 每次返回
        myoder = mypage.Myorder(driver)
        myoder.back()
        logging.info('返回')
        #       logging.info("返回")

    def test_liuliang(self):  # 能否找到流量订单
        myoder = mypage.Myorder(driver)
        try:
            assert myoder.try_find(mypage.Myorder.ll_order_loc) is True
            logging.info('找到流量订单')
        except:
            logging.warning("找不到流量订单")
            myoder.get_screenshot("找不到流量订单")
            raise

    def test_chongzhi(self):  # 能否找到充值订单
        myoder = mypage.Myorder(driver)
        try:
            assert myoder.try_find(mypage.Myorder.cz_order_loc) is True
            logging.info('找到充值订单')
        except:
            logging.warning("找不到充值订单")
            myoder.get_screenshot("找不到充值订单")
            raise

    def test_shangpin(self):  # 能否找到商品订单
        myoder = mypage.Myorder(driver)
        try:
            assert myoder.try_find(mypage.Myorder.sp_order_loc) is True
            logging.info('找不到商品订单')
        except:
            logging.warning("找不到商品订单")
            myoder.get_screenshot("找不到商品订单")
            raise

    @pytest.mark.skip(reason="5.7版本未配置分享订单")
    def test_fenxiang(self):  # 能否分享订单
        myoder = mypage.Myorder(driver)
        myoder.fenxiang()
        myoder.fenxiangdao()
        try:
            assert myoder.try_find(myoder.fenxiang_pan_loc) is True
            logging.info('进入分享二维码页面')
        except:
            logging.warning("无法进入分享二维码页面")
            myoder.get_screenshot("无法进入分享二维码页面")
            raise
        finally:
            myoder.back()

class TestZhangdan():
    def setup(self):  # ，每次进入我的账单
        zhangdan = mypage.Zhangdan(driver)
        zhangdan.my_zhangdan()
        logging.info("进入我的账单")

    def teardown(self):  # 每次返回
        zhangdan = mypage.Zhangdan(driver)
        zhangdan.back()
        logging.info("返回")

    def test_zhangdan(self):  # 能否进入我的账单页面
        zhangdan = mypage.Zhangdan(driver)
        try:
            assert zhangdan.try_find(mypage.Zhangdan.zhangdan_zonge_loc) is True
            logging.info('进入我的账单')
        except:
            logging.warning("无法进入我的账单")
            zhangdan.get_screenshot("无法进入我的账单")
            raise

    def test_fenxiang(self):  # 能否进入分享页面
        zhangdan = mypage.Zhangdan(driver)
        zhangdan.zhanndan_fenxiang()
        try:
            assert zhangdan.try_find(mypage.Zhangdan.fenxiang_panding_loc) is True
            logging.info('无法进入分享页面')
        except:
            logging.warning("无法进入分享页面")
            zhangdan.get_screenshot("无法进入分享页面")
            raise
        finally:
            zhangdan.quxiao()

class TestVoucher():
    def setup(self):  # ，每次进入我的卡劵
        kajuan = mypage.My_voucher(driver)
 #       kajuan.swipe_up()
        logging.info("上滑成功")
        kajuan.my_voucher()
        logging.info("进入我的卡劵")

    def teardown(self):  # 每次返回
        kajuan = mypage.My_voucher(driver)
        kajuan.close()
        logging.info("返回")

    def test_weishiyong(self):  # 能否找到“未使用”标签
        kajuan = mypage.My_voucher(driver)
        time.sleep(6)
        try:
            assert kajuan.try_find(mypage.My_voucher.no_shiyongxuan_loc) is True
            logging.info("找到未使用页签")
        except:
            logging.warning("找不到未使用页签")
            kajuan.get_screenshot("找不到未使用页签")
            raise

    def test_yiguoqi(self):  # 能否找到“已过期”标签
        kajuan = mypage.My_voucher(driver)
        kajuan.kajuan_lishi()
        try:
            assert kajuan.try_find(mypage.My_voucher.yiguoqi_loc) is True
            logging.info("找到已过期页签")
        except:
            logging.warning("找不到已过期页签")
            kajuan.get_screenshot("找不到已过期页签")
            raise

    def test_yishiyong(self):  # 能否找到“已使用”标签
        kajuan = mypage.My_voucher(driver)
        kajuan.kajuan_lishi()
        try:
            assert kajuan.try_find(mypage.My_voucher.yiguoqi_loc) is True
            logging.info("找到已使用页签")
        except:
            logging.warning("找不到已使用页签")
            kajuan.get_screenshot("找不到已使用页签")
            raise

class TestGeren():
    def setup(self):  # ，每次进入个人信息
        geren = mypage.Geren(driver)
        geren.imglogin()
        logging.info('-------进入个人信息----------')

    def teardown(self):  # 每次返回
        geren = mypage.Geren(driver)
        geren.back()
        logging.info('-------返回----------')

    def test_bianji(self):  # 能否找到编辑按钮
        geren = mypage.Geren(driver)
        try:
            assert geren.try_find(mypage.Geren.bianji_loc) is True
            logging.info('找到编辑按钮')
        except:
            logging.warning("找不到编辑按钮")
            geren.get_screenshot("找不到编辑按钮")
            raise

# 交费历史icon在我的页面暂无入口，搜索寻找
time.sleep(10)
class TestPayhistory():
    def setup(self):  # 每次进入交费历史
        jiaofei = mypage.Payhistory(driver)
        jiaofei.payhistory()
        logging.info("进入交费历史")

    def teardown(self):  # 每次返回
        jiaofei = mypage.Payhistory(driver)
        jiaofei.back()
        logging.info("返回")

    def test_jiaofei_lishi(self):  # 是否进入交费历史页面
        jiaofei = mypage.Payhistory(driver)
        try:
            assert jiaofei.try_find(mypage.Payhistory.jiaofei_pan_loc) is True
            logging.info('交费历史页面找到充值交费')
        except:
            logging.warning("交费历史页面找不到充值交费")
            jiaofei.get_screenshot("交费历史页面找不到充值交费")
            raise

    def test_chongzhi(self):  # 是否进入充值中心
        jiaofei = mypage.Payhistory(driver)
        jiaofei.jiaofei()
        try:
            assert jiaofei.try_find(mypage.Payhistory.chongzhi_pan_loc) is True
            logging.info('进入充值中心')
        except:
            logging.warning("能否进入充值中心")
            jiaofei.get_screenshot("能否进入充值中心")
            raise
        finally:
            jiaofei.back()

    def test_fenxiang(self):  # 是否进入分享页面
        jiaofei = mypage.Payhistory(driver)
        jiaofei.fenxiang()
        try:
            assert jiaofei.try_find(mypage.Payhistory.pengyouquan_loc) is True
            logging.info('能否进入分享页面')
        except:
            logging.warning("能否进入分享页面")
            jiaofei.get_screenshot("能否进入分享页面")
            raise
        finally:
            jiaofei.erweima()
            jiaofei.back()

    def test_shuaixuan(self):  # 筛选是否可用
        jiaofei = mypage.Payhistory(driver)
        jiaofei.shaixuan()
        try:
            assert jiaofei.try_find(mypage.Payhistory.siyue_loc) is True
            logging.info("能否选择筛选的月份")
        except:
            logging.warning("能否选择筛选的月份")
            jiaofei.get_screenshot("能否选择筛选的月份")
            raise
        finally:
            jiaofei.siyue()

#流量管家icon在我的页面暂无入口，搜索寻找

class Testsearch_Guanjia():  # 搜索出流量管家的icon
    def test_search(self):
        search = shouyepage.Search(driver)
        search.chazhao("流量管家")
        time.sleep(6)
class TestGuanjia():  # 每次进入流量管家
    def setup(self):

        guan_jia = mypage.Guanjia(driver)
        guan_jia.guanjia()
        #     logging.info("进入流量管家")
        logging.info('-------进入流量管家----------')

    def teardown(self):  # 每次返回一次
        guan_jia = mypage.Guanjia(driver)
        guan_jia.back()
        #      logging.info("返回")
        logging.info('-------返回----------')

    def test_liuliang(self):  # 是否存在流量订单
        guan_jia = mypage.Guanjia(driver)
        guan_jia.dingdan()
        logging.info('-------进入流量订单----------')
        try:
            assert guan_jia.try_find(mypage.Guanjia.dingdan_pan_loc) is True
            logging.info('流量订单正常')
        except:
            logging.warning("流量订单不正常")
            guan_jia.get_screenshot("流量订单不正常")
            raise
        finally:
            guan_jia.back()

    def test_shangpin(self):  # 是否存在商品订单
        guan_jia = mypage.Guanjia(driver)
        guan_jia.shangpin()
        logging.info('-------进入商品订单----------')
        try:
            assert guan_jia.try_find(mypage.Guanjia.shangpin_pan_loc) is True
            logging.info('商品订单正常')
        except:
            logging.warning("商品订单不正常")
            guan_jia.get_screenshot("商品订单不正常")
            raise
        finally:
            guan_jia.back()

    def test_liuliang_xiangdan(self):  # 是否存在流量详单
        guan_jia = mypage.Guanjia(driver)
        guan_jia.xiangdan()
        logging.info("进入流量详单")
        try:
            assert guan_jia.try_find(mypage.Guanjia.xiangdan_pan_loc) is True
            logging.info('流量详单正常')
        except:
            logging.warning("流量详单不正常")
            guan_jia.get_screenshot("流量详单不正常")
            raise
        finally:
            guan_jia.xiangdanback_pan()
            logging.info("返回到我的页面")

    def test_bannian_bao(self):  # 是否存在流量半年包
        guan_jia = mypage.Guanjia(driver)
        guan_jia.swipe_up()
        logging.info("向上滑动")
        guan_jia.bannian()
        logging.info("点击流量半年包")
        try:
            assert guan_jia.try_find(mypage.Guanjia.liuliang_pan_loc) is True
            logging.info('无法进入半年包')
        except:
            logging.warning("无法进入半年包")
            guan_jia.get_screenshot("无法进入半年包")
            raise
        finally:
            guan_jia.back()

    def test_jibao(self):  # 是否存在流量季包
        guan_jia = mypage.Guanjia(driver)
        guan_jia.swipe_up()
        logging.info("向上滑动")
        guan_jia.jibao()
        logging.info("点击流量季包")
        try:
            assert guan_jia.try_find(mypage.Guanjia.liuliang_pan_loc) is True
            logging.info('进入季包')
        except:
            logging.warning("无法进入季包")
            guan_jia.get_screenshot("无法进入季包")
            raise
        finally:
            guan_jia.back()

    def test_ribao(self):  # 是否存在流量日包
        guan_jia = mypage.Guanjia(driver)
        guan_jia.swipe_up()
        guan_jia.ri_taocan()
        try:
            assert guan_jia.try_find(mypage.Guanjia.liuliang_pan_loc) is True
            logging.info('无法进入流量日包')
        except:
            logging.warning("无法进入流量日包")
            guan_jia.get_screenshot("无法进入流量日包")
            raise
        finally:
            guan_jia.back()

#我的电影icon在我的页面暂无入口，搜索寻找
class Testsearch_movie():  # 搜索出流量管家的icon
    def test_search(self):
        search = shouyepage.Search(driver)
        search.chazhao("我的电影")
        time.sleep(6)
class TestMy_movie():
    def setup(self):  # 每次进入我的电影
        dianying = mypage.My_movie(driver)
        dianying.my_movie()
        logging.info('进入我的电影')

    #        logging.info("进入我的电影")
    def test_taocan(self):  # 是否存在套餐业务
        dianying = mypage.My_movie(driver)
        try:
            assert dianying.try_find(mypage.My_movie.gou_piao_loc) is True
            logging.info('找到购票页面')
        except:
            logging.warning("找不到购票页面")
            dianying.get_screenshot("找不到购票页面")
            raise
        finally:
            dianying.gou_piaoclose()

#李纯代码
class TestFaPiao():
    # def setup(self):  # 每次进入发票页面
    #     fapiao = mypage.FaPiao(driver)
    #     fapiao.fapiao()
    #     logging.info("进入发票")

    def teardown(self):  # 每个用例结束返回
        fapiao = mypage.FaPiao(driver)
        time.sleep(5)
        fapiao.back()
        logging.info("返回成功")


    def test_huafei(self):  # 进入话费充值发票是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.swipe_up(t=1000,n=1)
        logging.info("上滑成功")
        time.sleep(5)
        fapiao.fapiao()
        time.sleep(5)
        fapiao.huafei()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_huafei_loc) is True
            logging.info('成功进入话费充值')
        except:
            logging.warning("找不到话费充值")
            fapiao.get_screenshot("找不到话费充值")
            raise


    def test_liuliang(self):  # 进入流量直充发票是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.liuliang()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_liuliang_loc) is True
            logging.info("成功进入流量直充")
        except:
            logging.warning("找不到流量直充")
            fapiao.get_screenshot("找不到流量直充")
            raise

    def test_kuandai(self):  # 进入宽带发票是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.kuandai()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_kuandai_loc) is True
            logging.info("成功进入宽带发票")
        except:
            logging.warning("找不到宽带发票")
            fapiao.get_screenshot("找不到宽带发票")
            raise

    def test_yuejie(self):  # 进入月结发票是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.yuejie()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_yuejie_loc) is True
            logging.info("成功进入月结发票")
        except:
            logging.warning("找不到月结发票")
            fapiao.get_screenshot("找不到月结发票")
            raise

    def test_taitou(self):  # 进入发票抬头是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.taitou()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_taitou_loc) is True
            logging.info("成功进入发票抬头")
        except:
            logging.warning("找不到发票抬头")
            fapiao.get_screenshot("找不到发票抬头")
            raise

    def test_jinruxinzeng(self):  # 进入新增发票是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.taitou()
        fapiao.xinzeng()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_xinzeng_loc) is True
            logging.info("成功进入新增发票")
        except:
            logging.warning("找不到新增发票")
            fapiao.get_screenshot("找不到新增发票")
            raise


    def test_xinzengfapiao(self):  # 新增发票
        fapiao = mypage.FaPiao(driver)
        fapiao.xinzeng()
        fapiao.riseinput("cddrsd")
        fapiao.shibiehao("530369868209019")
        fapiao.moren()
        fapiao.baocun()
        fapiao.close()
        fapiao.taitou()

        try:
            assert fapiao.try_find(mypage.FaPiao.danwei_loc) is True
            logging.info("保存")
        except:
            logging.warning("保存失败")
            fapiao.get_screenshot("保存失败")
            raise


    def test_mail(self):  # 进入邮箱推送是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.youtui()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_tuisong_loc) is True
            logging.info("进入邮箱推送")
        except:
            logging.warning("找不到邮箱推送")
            fapiao.get_screenshot("找不到邮箱推送")
            raise

    def test_xiugai_mail(self):  # 修改邮箱推送是否正常
        fapiao = mypage.FaPiao(driver)
        fapiao.youtui()
        fapiao.mail("2418261328@qq.com")
        fapiao.save()
        try:
            assert fapiao.try_find(mypage.FaPiao.pan_youxiang_loc) is True
            logging.info("修改成功")
        except:
            logging.warning("修改失败")
            fapiao.get_screenshot("修改失败")
            raise
        finally:
            fapiao.close()

    def test_kaijufapiao(self):
        fapiao = mypage.FaPiao(driver)
        logging.info("上滑成功")
        fapiao.yuejie()
        fapiao.kaiju()
        fapiao.tingkai()
        try:
            assert fapiao.try_find(mypage.FaPiao.kaiju_loc) is True
            logging.info("停止开具")
        except:
            logging.warning("找不到停止开具")
            fapiao.get_screenshot("找不到停止开具")
            raise
        finally:
            fapiao.close()

@pytest.mark.skip(reason="暂未调通")
class TestQinmifu():
     # def setup(self):  # ，每次进入亲密付
     #     qmf = mypage.Qinmifu(driver)
     #     logging.info('上滑成功')
     #     qmf.qinmifu()


    def teardown(self):  # 每次返回
        qmf = mypage.Qinmifu(driver)
        time.sleep(5)
        qmf.back()
        logging.info('返回')


    def test_001(self):  # 能否进入亲密付页面
        qmf = mypage.Qinmifu(driver)
        time.sleep(20)
        qmf.swipe_up(t=1000, n=2)
        qmf.qinmifu()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_qinmifu_loc) is True
            logging.info('进入亲密付')
        except:
            logging.warning("无法进入亲密付")
            qmf.get_screenshot("无法进入亲密付")
            raise


    def test_002(self): #进入亲密付充值订单正常
        qmf = mypage.Qinmifu(driver)
        time.sleep(5)
        qmf.chongzhijilu()
        qmf.chongzhi()
        try:
            assert qmf.try_find(mypage.Qinmifu.chongzhi_pan_loc) is True
            logging.info("进入亲密付充值订单")
        except:
            logging.warning("无法进入亲密付充值订单")
            qmf.get_screenshot("无法进入亲密付充值订单")
            raise

    def test_003(self): #进入亲密付流量订单正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        time.sleep(5)
        qmf.chongzhijilu()
        qmf.liuliang()
        try:
            assert qmf.try_find(mypage.Qinmifu.liuliang_pan_loc) is True
            logging.info("进入亲密付流量订单")
        except:
            logging.warning("无法进入亲密付流量订单")
            qmf.get_screenshot("无法进入亲密付流量订单")
            raise

    def test_004(self):  # 进入充值记录正常
         qmf = mypage.Qinmifu(driver)
         time.sleep(10)
         qmf.qinmifu()
         time.sleep(5)
         qmf.chongzhijilu()
         try:
             assert qmf.try_find(mypage.Qinmifu.qmf_dingdan_pan_loc) is True
             logging.info("进入亲密付订单")
         except:
             logging.warning("无法进入亲密付订单")
             qmf.get_screenshot("无法进入亲密付订单")
             raise

    def test_005(self):  #亲密付管理成员是否正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        time.sleep(5)
        qmf.guanli()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_guanli_loc) is True
            logging.info('管理成员正常')
        except:
            logging.warning("管理成员不正常")
            qmf.get_screenshot("管理成员不正常")
            raise

    def test_006(self):  #亲密付添加号码时取消是否正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        qmf.tianhaoquxiao()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_quxiao_loc) is True
            logging.info('添加号码时取消正常')
        except:
            logging.warning("添加号码时取消不正常")
            qmf.get_screenshot("添加号码时取消不正常")
            raise

    def test_007(self):  #亲密付添加号码是否正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        qmf.tianhao()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_lijitianjia_loc) is True
            logging.info('添加号码正常')
        except:
            logging.warning("添加号码不正常")
            qmf.get_screenshot("添加号码不正常")
            raise
    def test_008(self): #添加记录正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        time.sleep(5)
        qmf.tianjiajilu()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_tianjiajilu_loc) is True
            logging.info('添加记录正常')
        except:
            logging.warning("添加记录不正常")
            qmf.get_screenshot("添加记录不正常")
            raise

    def test_009(self):  #被添加记录正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        time.sleep(5)
        qmf.tianjiajilu()
        qmf.beitianjiajilu()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_beitianjiajilu_loc) is True
            logging.info('被添加记录正常')
        except:
            logging.warning("被添加记录不正常")
            qmf.get_screenshot("被添加记录不正常")
            raise

    def test_010(self):  # 进入充话费是否正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        qmf.chonghuafei()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_huafei_loc) is True
            logging.info('进入充话费正常')
        except:
            logging.warning("进入充话费不正常")
            qmf.get_screenshot("进入充话费不正常")
            raise

    def test_011(self):  # 进入充流量是否正常
        qmf = mypage.Qinmifu(driver)
        qmf.qinmifu()
        qmf.chongliuliang()
        try:
            assert qmf.try_find(mypage.Qinmifu.pan_liuliang_loc) is True
            logging.info('进入充流量正常')
        except:
            logging.warning("进入充流量不正常")
            qmf.get_screenshot("进入充流量不正常")
            raise
        finally:
            qmf.back()

class TestShiMing():  # 每次进入实名登记
    def setup(self):
        shi_ming = mypage.ShiMing(driver)
        shi_ming.shiming()
        logging.info('进入实名登记')

    def teardown(self):  # 每次返回一次
        shi_ming = mypage.ShiMing(driver)
        shi_ming.back()
        logging.info('返回')

    def test_shiming(self):  # 是否成功进入实名登记
        shi_ming = mypage.ShiMing(driver)
        try:
            assert shi_ming.try_find(mypage.ShiMing.pan_shiming_loc) is True
            logging.info('进入实名登记正常')
        except:
            logging.warning("进入实名登记不正常")
            shi_ming.get_screenshot("进入实名登记不正常")
            raise

class TestHeDuoHao():
    def setup(self):  #每次进入和多号
        hdh = mypage.HeDuoHao(driver)
        hdh.heduohao()
        logging.info('进入和多号')

    def teardown(self):  # 每次返回一次
        hdh = mypage.HeDuoHao(driver)
        hdh.back()
        logging.info('返回')

    def test_heduohao(self):  # 是否成功进入和多号
        hdh = mypage.HeDuoHao(driver)
        try:
            assert hdh.try_find(mypage.HeDuoHao.pan_heduohao_loc) is True
            logging.info('进入和多号正常')
        except:
            logging.warning("进入和多号不正常")
            hdh.get_screenshot("进入和多号不正常")
            raise

class TestZhiNeng():
    # def setup(self):
    #     zhineng = mypage.ZhiNeng(driver)
    #     zhineng.zhineng()
    #     logging.info('进入智能家居')

    # def teardown(self):  # 每次返回一次
    #     zhineng = mypage.ZhiNeng(driver)
    #     zhineng.back()
    #     logging.info('返回')
    def test_zhinengjiaju(self):  # 是否成功进入智能家居
        zhineng = mypage.ZhiNeng(driver)
        # zhineng.swipe_up()
        zhineng.zhineng()
        try:
            assert zhineng.try_find(mypage.ZhiNeng.pan_zhineng_loc) is True
            logging.info('进入智能家居正常')
        except:
            logging.warning("进入智能家居不正常")
            zhineng.get_screenshot("进入智能家居不正常")
            raise

    def test_wangguan(self):  #是否成功进入网关管理
        zhineng = mypage.ZhiNeng(driver)
        zhineng.wangguan()
        try:
            assert zhineng.try_find(mypage.ZhiNeng.pan_wangguan_loc) is True
            logging.info('进入网关管理正常')
        except:
            logging.warning("进入网关管理不正常")
            zhineng.get_screenshot("进入网关管理不正常")
            raise
        finally:
            zhineng.wangguan_back()

    def test_shebei(self):  #是否成功进入设备管理
        zhineng = mypage.ZhiNeng(driver)
        zhineng.shebei()
        try:
            assert zhineng.try_find(mypage.ZhiNeng.pan_shebei_loc) is True
            logging.info('进入设备管理正常')
        except:
            logging.warning("进入设备管理不正常")
            zhineng.get_screenshot("进入设备管理不正常")
            raise
        finally:
            zhineng.shebei_back()
    def test_baokuan(self):  # 是否成功进入爆款商品
        zhineng = mypage.ZhiNeng(driver)
        zhineng.baokuan()
        try:
            assert zhineng.try_find(mypage.ZhiNeng.pan_baokuan_loc) is True
            logging.info('进入爆款商品正常')
        except:
            logging.warning("进入爆款商品不正常")
            zhineng.get_screenshot("进入爆款商品不正常")
            raise
        finally:
            zhineng.back()
            zhineng.close()

class TestChaJian():
    def setup(self): #每次进入插件中心
        chajian = mypage.ChaJian(driver)
        chajian.swipe_up()
        chajian.chajian()
        logging.info('进入插件中心')

    def teardown(self):  # 每次返回一次
        chajian = mypage.ChaJian(driver)
        chajian.back()
        logging.info('返回')

    def test_chajian(self):  # 是否成功进入插件中心
        chajian = mypage.ChaJian(driver)
        try:
            assert chajian.try_find(mypage.ChaJian.pan_chajian_loc) is True
            logging.info('进入插件中心正常')
        except:
            logging.warning("进入插件中心不正常")
            chajian.get_screenshot("进入插件中心不正常")
            raise


    def test_fenxiang(self):  # 是否成功进入分享页面
        chajian = mypage.ChaJian(driver)
        chajian.fenxiang()
        try:
            assert chajian.try_find(mypage.ChaJian.pan_fenxiang_loc) is True
            logging.info('进入分享正常')
        except:
            logging.warning("进入分享不正常")
            chajian.get_screenshot("进入分享不正常")
            raise
        finally:
            chajian.quxiao()

if __name__ == '__main__':
    driver = appium_desired()
    ba = loginpage.Login(driver)
    ba.start()
    ba.login('13501585305')
    wodea = mypage.My(driver)
    wodea.wode()

