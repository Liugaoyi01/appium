# -*- coding:utf-8 -*-
import pytest
import sys, os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from auto_test_client.baseView import basepage
from auto_test_client.businessView import shouyepage,loginpage
from auto_test_client.public.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import time
import logging

driver = appium_desired()


def setup_module():  # 整个.py模块启动一次客户端
    base = loginpage.Login(driver)
    base.start()
    base= shouyepage.Shouye(driver)
    base.check_guide_know()



def teardown_module():  # 整个.py模块退出客户端
    driver.close_app()


class TestCard:
    def teardown(self):  # 每个用例结束返回
        card = shouyepage.Card(driver)
        card.back()

    def test_001(self):  # 未登录提示语是否正确
        card = shouyepage.Card(driver)
        try:
            assert card.try_find(shouyepage.Card.tishi_loc) is True
            logging.info('卡片码表登录提示')
        except:
            logging.error("码表无未登录提示语")
            card.get_screenshot("无未登录提示语")
            raise

    def test_002(self):  # 未登录数值是否正确
        card = shouyepage.Card(driver)
        try:
            assert card.try_find(shouyepage.Card.jine_loc) is True
            logging.info('码表未登录数值')
        except:
            logging.error("码表未登录数值不正确")
            card.get_screenshot("未登录数值不正确")
            raise

    def test_003(self):  # 未登录拉起登录是否正确
        card = shouyepage.Card(driver)
        card.look()
        login = loginpage.Login(driver)
        try:
            assert login.try_text(loginpage.Login.title_loc) == "欢迎登录"
            logging.info('跳转登录页面')
        except:
            logging.error("拉起登录错误")
            login.get_screenshot("拉起登录错误")
            raise
        finally:
            login.close()

    def test_biejing(self):  #首次启动客户端，默认定位      新增
        shouye = shouyepage.Shouye(driver)
        try:
            assert shouye.try_text(shouyepage.Shouye.beijin_loc) == "北京"
            logging.info('客户端定位默认为北京')
        except:
            logging.info('客户端定位默认失败')
            raise

    def test_xiaoxi(self): #未登录状态，右上角更多按钮显示    新增
        shouye = shouyepage.Shouye(driver)
        shouye.upper_right()
        time.sleep(3)
        try:
            assert shouye.try_text(shouyepage.Shouye.xiaoxi_loc) == "消息"
            logging.info('右上角更多按钮显示正确')
        except:
            logging.error("右上角更多按钮显示失败")
            shouye.get_screenshot("右上角更多按钮显示失败")
            raise
        finally:
            shouye.xiaoxi()

    def test_dingdanxi(self):  #未登录状态，消息中心页面显示     新增
        shouye = shouyepage.Shouye(driver)
        shouye.upper_right()
        shouye.xiaoxi()
        time.sleep(3)
        try:
            assert shouye.try_find(shouyepage.Shouye.dingdanxi_loc) is True
            logging.info('消息中心页面显示正确')
        except:
            logging.error("消息中心页面显示失败")
            shouye.get_screenshot("消息中心页面显示失败")
            raise

    def test_denglu(self): #未登录状态，点击消息订单，拉起登录页面      新增
        shouye = shouyepage.Shouye(driver)
        shouye.upper_right()
        shouye.xiaoxi()
        shouye.dingdanxi()
        time.sleep(3)
        try:
            assert shouye.try_text(shouyepage.Shouye.denglu_loc) == "欢迎登录"
            logging.info('拉起登录页面')
        except:
            logging.error("拉起登录失败")
            shouye.get_screenshot("拉起登录失败")
            raise
        finally:
            shouye.fanhui()

    def test_008(self):  # 未登录是否可登录
        card = shouyepage.Card(driver)
        card.look()
        login = loginpage.Login(driver)
        login.login('13715307043')
        card = shouyepage.Shouye(driver)
        card.close_c()
        try:
            assert card.try_find(shouyepage.Card.tishi_loc) is False
            logging.info('登录成功')
        except:
            logging.error("登录失败")
            card.get_screenshot("登录失败")
            raise

    def test_009(self):  # 流量剩余跳转是否正确
        card = shouyepage.Card(driver)
        card.liuliang()
        try:
            assert card.try_text(shouyepage.Shouye.title_loc) == "流量查询"
            logging.info('跳转流量查询')
        except:
            logging.error("流量剩余跳转错误")
            card.get_screenshot("流量剩余跳转错误")
            raise

    def test_010(self):  # 语音剩余跳转是否正确
        card = shouyepage.Card(driver)
        card.yuyin()
        try:
            assert card.try_find(shouyepage.Card.shengyu_loc) is True
            logging.info('语音跳转语音查询')
        except:
            logging.error("语音剩余跳转错误")
            card.get_screenshot("语音剩余跳转错误")
            raise

    def test_011(self):  # 语音查询页面分享
        card = shouyepage.Card(driver)
        card.yuyin()
        try:
            assert card.try_find(shouyepage.Card.fenxiang_loc) is True
            logging.info('语音页面分享')
        except:
            logging.error("语音页面无分享")
            card.get_screenshot("语音页面无分享")
            raise

    def test_012(self):  # 语音去充值
        card = shouyepage.Card(driver)
        card.yuyin()
        card.gobutton()
        try:
            assert card.try_find(shouyepage.Recharge.content2_loc) is True
            logging.info('去充值跳转')
        except:
            logging.error("去充值跳转错误")
            card.get_screenshot("去充值跳转错误")
            raise
        finally:
            card.back()

    def test_013(self):  # 话费余额跳转是否正确
        card = shouyepage.Card(driver)
        card.huafei()
        try:
            assert card.try_find(shouyepage.Card.yue_loc) is True
            logging.info('跳转话费余额')
        except:
            logging.error("话费余额跳转错误")
            card.get_screenshot("话费余额跳转错误")
            raise

    def test_014(self):  # 话费余额是否有可用余额
        card = shouyepage.Card(driver)
        card.huafei()
        try:
            assert card.try_find(shouyepage.Card.keyong_loc) is True
            logging.info('话费余额有可用余额')
        except:
            logging.error("话费余额无可用余额")
            card.get_screenshot("话费余额无可用余额")
            raise

    def test_015(self):  # 话费去充值
        card = shouyepage.Card(driver)
        card.huafei()
        card.gopay()
        try:
            assert card.try_find(shouyepage.Recharge.content2_loc) is True
            logging.info('去充值跳转')
        except:
            logging.error("去充值跳转错误")
            card.get_screenshot("去充值跳转错误")
            raise
        finally:
            card.back()

  #话费去掉了套餐余量入口
    # def test_016(self):  # 点就话费套餐余量
    #     card = shouyepage.Card(driver)
    #     card.huafei()
    #     card.taocan()
    #     try:
    #         assert card.try_text(shouyepage.Shouye.title_loc) == "套餐余量"
    #         logging.info('套餐余量跳转')
    #     except:
    #         logging.error("套餐余量跳转错误")
    #         card.get_screenshot("套餐余量跳转错误")
    #         raise
    #     finally:
    #         card.back()

#话费去掉了套餐办理入口
    # def test_017(self):  # 点就话费套餐办理
    #     card = shouyepage.Card(driver)
    #     card.huafei()
    #     card.banli()
    #     try:
    #         assert card.try_text(shouyepage.Shouye.title_loc) =="业务"
    #         logging.info('套餐办理跳转')
    #     except:
    #         logging.error("套餐办理跳转错误")
    #         card.get_screenshot("套餐办理跳转错误")
    #         raise
    #     finally:
    #         card.back()

#话费去掉了我的账单入口
    # def test_018(self):  # 点就话费我的账单
    #     card = shouyepage.Card(driver)
    #     card.huafei()
    #     card.zhangdan()
    #     try:
    #         assert card.try_text(shouyepage.Card.zonge_loc) == "本期账单总额: "
    #         logging.info('我的账单跳转')
    #     except:
    #         logging.error("我的账单跳转错误")
    #         card.get_screenshot("我的账单跳转错误")
    #         raise
    #     finally:
    #         card.back()

class TestShouye:
    def test_006(self):  # 语音搜索跳转
        shouye = shouyepage.Search(driver)
        shouye.yuyin()
        try:
            assert shouye.try_find(shouyepage.Search.yuyin_s_loc) is True
            logging.info('跳转语音搜索')
        except:
            logging.error("未跳转语音搜索")
            shouye.get_screenshot("未跳转语音搜索")
            raise
        finally:
            shouye.yuyin_c()

    def test_007(self):  # 语音搜索默认
        shouye = shouyepage.Search(driver)
        shouye.yuyin()
        try:
            assert shouye.try_find(shouyepage.Search.yuyin_m_loc) is True
            logging.info('语音搜索默认普通话')
        except:
            logging.error("语音搜索未默认普通话")
            shouye.get_screenshot("语音搜索未默认普通话")
            raise
        finally:
            shouye.yuyin_c()

    def test_008(self):  # 是否有情感化插件
        shouye = shouyepage.Shouye(driver)
        try:
            assert shouye.try_find(shouyepage.Shouye.qinggan_loc) is True
            logging.info('有情感化插件')
        except:
            logging.error("无情感化插件")
            shouye.get_screenshot("无情感化插件")
            raise

    def test_009(self):  # 情感化插件关闭
        shouye = shouyepage.Shouye(driver)
        shouye.close_c()
        try:
            assert shouye.try_find(shouyepage.Shouye.qinggan_loc) is False
            logging.info('情感化插件关闭')
        except:
            logging.error("情感化插件关闭失败")
            shouye.get_screenshot("情感化插件关闭失败")
            raise

    def test_010(self):  # 是否有和信用分
        shouye = shouyepage.Shouye(driver)
        try:
            assert shouye.try_find(shouyepage.Shouye.xinyong_loc) is True
            logging.info('有和信用分')
        except:
            logging.error("无和信用分入口")
            shouye.get_screenshot("无和信用分入口")
            raise

    def test_011(self):  # 和信用分跳转是否正确
        shouye = shouyepage.Shouye(driver)
        shouye.jingxi()
        time.sleep(3)
        try:
            assert shouye.try_find(shouyepage.Shouye.liaojie_loc) is True
            logging.info('和信用分跳转')
        except:
            logging.error("和信用分跳转错误")
            shouye.get_screenshot("和信用分跳转错误")
            raise
        finally:
            shouye.close()

    # def test_012(self):  # 猜你喜欢是否有换一批
    #     shouye = shouyepage.Shouye(driver)
    #     shouye.swipe_up(t=1000, n=3)
    #     try:
    #         assert shouye.try_find(shouyepage.Shouye.huanyi_loc) is True
    #         logging.info('猜你喜欢换有换一批')
    #     except:
    #         logging.error("猜你喜欢无换一批")
    #         shouye.get_screenshot("猜你喜欢无换一批")
    #         raise
    #
    # def test_013(self):  # 新疆是否有维语入口
    #     city = shouyepage.Cities(driver)
    #     city.dishi()
    #     city.qiehuan("新疆", "乌鲁木齐")
    #     try:
    #         assert city.try_find(shouyepage.Shouye.weiyu_loc) is True
    #         logging.info('新疆有维语入口')
    #     except:
    #         logging.error("新疆无维语入口")
    #         city.get_screenshot("新疆无维语入口")
    #         raise
    #     finally:
    #         city.close_c()
    #         city.qiehuan("广东", "深圳")


class TestRecharge:
    def setup(self):  # 每个用例执行进入充值交费
        test = shouyepage.Recharge(driver)
        test.content()

    def teardown(self):  # 每个用例结束返回
        test = shouyepage.Cities(driver)
        test.back()
        test.login_s()

    def test_chongzhi(self):#充值交费        新增
        test = shouyepage.Recharge(driver)
        time.sleep(7)
        test.goto_login_Btn()
        assert "充值中心" == test.check_content()

    def test_dianzifapiao(self): #电子发票      新增
        test = shouyepage.Recharge(driver)
        time.sleep(4)
        # test.goto_login_Btn()
        test.invoice()
        assert "我的发票" == test.check_invoice()

    def test_huafeiliucheng(self):  #充值话费流程判断    新增
        test = shouyepage.Recharge(driver)
        time.sleep(4)
        # test.goto_login_Btn()
        test.call_charge()
        time.sleep(3)
        try:
            assert test.try_find(shouyepage.Recharge.text1_loc) is True
            logging.info('话费充值正确')
        except:
            logging.error('话费充值错误')
            test.get_screenshot('话费充值错误')
            raise
        finally:
            test.return_s()

    def test_liuliangliucheng(self):  #充值流量流程判断   新增
        test = shouyepage.Recharge(driver)
        time.sleep(4)
        # test.goto_login_Btn()
        test.flow()
        time.sleep(3)
        try:
            assert test.try_find(shouyepage.Recharge.text1_loc) is True
        except:
            logging.info('流量充值错误')
            test.return_s()
            test.get_screenshot('流量充值错误')
            raise
        finally:
            test.return_s()
            logging.info('流量充值正确')

# @pytest.mark.skipif(sys.platform =='win32',reason="想跳过")
# class TestPersonalized:
#     def test_shouji(self):   #买手机专区 新增
#         shouye = shouyepage.Personalized(driver)
#         shouye.maishouji()
#         try:
#             assert shouye.try_text(shouyepage.Shouye.title_loc) == "商品详情"
#             logging.info('买手机功能展示正确')
#         except:
#             logging.info('买手机功能展示错误')
#             shouye.get_screenshot('买手机功能展示错误')
#             raise
#         finally:
#             shouye.close()
#
#     # @pytest.mark.skip(reason="no way of currently testing this")
#     def test_kuandai(self):   #宽带专区   新增
#         shouye = shouyepage.Personalized(driver)
#         shouye.kuandai()
#         time.sleep(5)
#         try:
#             assert shouye.try_text(shouyepage.Shouye.title_loc) == "宽带业务"
#             logging.info('已进入宽带业务页面，页面显示正确')
#         except:
#             logging.info('宽带业务页面显示错误')
#             shouye.get_screenshot('宽带业务页面显示错误')
#             raise
#         finally:
#             shouye.back()
#
#     @pytest.mark.skip(reason="no way of currently testing this")
#     def test_zhinengjiaju(self):   #智能家居   新增
#         shouye = shouyepage.Personalized(driver)
#         shouye.zhineng_jiaju()
#         time.sleep(4)
#         try:
#             assert shouye.try_text(shouyepage.Shouye.title_loc) == "智能家居"
#             logging.info('已进入智能家居页面，页面显示正确')
#         except:
#             logging.info('智能家居页面显示错误')
#             shouye.get_screenshot('智能家居页面显示错误')
#             raise
#         finally:
#             shouye.back()
#
#     @pytest.mark.skip(reason="no way of currently testing this")
#     def test_zhinengyingjian(self):   #智能硬件专区   新增
#         shouye = shouyepage.Personalized(driver)
#         shouye.zhineng_yingjian()
#         try:
#             assert shouye.try_text(shouyepage.Shouye.title_loc) == "商品详情"
#             logging.info('智能硬件功能展示正确')
#         except:
#             logging.info('智能硬件功能展示错误')
#             shouye.get_screenshot('智能硬件功能展示错误')
#             raise
#         finally:
#             shouye.back()
#
#     @pytest.mark.skip(reason="no way of currently testing this")
#     def test_zhengzhao(self):   #证照信息   新增
#         shouye = shouyepage.Personalized(driver)
#         shouye.zhengzhao()
#         try:
#             assert shouye.try_text(shouyepage.Shouye.title_loc) == "证照信息_中国移动官方网站"
#             logging.info('“证照信息”显示正确')
#         except:
#             logging.info('“证照信息”显示错误')
#             shouye.get_screenshot('“证照信息”显示错误')
#             raise
#         finally:
#             shouye.back()
#             shouye.swipe_down(t=1000,n=7)


class TestTraffic:
    def setup(self):  # 每个用例执行进入流量管家
        traffic = shouyepage.Traffic(driver)
        traffic.liuliang()

    def teardown(self):  # 每个用例结束返回
        traffic = shouyepage.Traffic(driver)
        traffic.back()

    def test_001(self):  # 跳转流量管家是否正确
        traffic = shouyepage.Traffic(driver)
        try:
            assert traffic.try_text(shouyepage.Shouye.title_loc) == "流量查询"
            logging.info('跳转流量查询页面')
        except:
            logging.error("跳转流量管家错误")
            traffic.get_screenshot("跳转流量管家错误")
            raise

    def test_002(self):  # 分享增加微信快照
        traffic = shouyepage.Traffic(driver)
        traffic.fenxiang()
        try:
            assert traffic.try_find(shouyepage.Traffic.kuaizhao_loc) is True
            logging.info('分享增加微信快照')
        except:
            logging.error("分享未增加微信快照")
            traffic.get_screenshot("分享未增加微信快照")
            raise
        finally:
            traffic.quxiao()

    def test_003(self):  # 流量订单跳转是否正确
        traffic = shouyepage.Traffic(driver)
        traffic.dingdan()
        try:
            assert traffic.try_find(shouyepage.Traffic.chongzhi_loc) is True
            logging.info('流量订单跳转正确')
        except:
            logging.error("流量订单跳转错误")
            traffic.get_screenshot("流量订单跳转错误")
            raise
        finally:
            traffic.back()

    def test_004(self):  # 境外流量跳转是否正确
        traffic = shouyepage.Traffic(driver)
        traffic.jingwai()
        time.sleep(3)
        try:
            assert traffic.try_text(shouyepage.Shouye.title_loc) == "国际/港澳台业务"
            logging.info('境外流量跳转正确')
        except:
            logging.error("境外流量跳转错误")
            traffic.get_screenshot("境外流量跳转错误")
            raise
        finally:
            traffic.back()

    def test_005(self):  # 流量商品跳转是否正确
        traffic = shouyepage.Traffic(driver)
        traffic.shangpin()
        try:
            assert traffic.try_text(shouyepage.Shouye.title_loc) == "业务"
            logging.info('流量商品跳转正确')
        except:
            logging.error("流量商品跳转错误")
            traffic.get_screenshot("流量商品跳转错误")
            raise
        finally:
            traffic.back()

    def test_006(self):  # 流量详单跳转是否正确
        traffic = shouyepage.Traffic(driver)
        traffic.xiangdan()
        try:
            assert traffic.try_find(shouyepage.Traffic.shenfen_loc) is True
            logging.info('流量详单跳转正确')
        except:
            logging.error("流量详单跳转错误")
            traffic.get_screenshot("流量订单跳转错误")
            raise
        finally:
            traffic = loginpage.Login(driver)
            traffic.close()

class TestJifen:
    def setup(self):  # 每个用例执行进入积分
        jifen = shouyepage.Jifen(driver)
        jifen.points()
        time.sleep(5)

    def teardown(self):  # 每个用例结束返回
        jifen = shouyepage.Jifen(driver)
        jifen.close()

    def test_001(self):  # 跳转积分商城是否正确
        jifen = shouyepage.Jifen(driver)
        time.sleep(3)
        try:
            assert jifen.try_text(shouyepage.Shouye.title_loc) == "中国移动积分商城"
            logging.info('跳转积分商城')
        except:
            logging.error("跳转积分商城错误")
            jifen.get_screenshot("跳转积分商城错误")
            raise

    def test_002(self):  # 已登录跳转我的账户是否正确
        jifen = shouyepage.Jifen(driver)
        jifen.account()
        try:
            assert jifen.try_find(shouyepage.Jifen.jifen_loc) is True
            logging.info('跳转我的账户')
        except:
            logging.error("我的账户登录状态错误")
            jifen.get_screenshot("我的账户登录状态错误")
            raise

    def test_003(self):  # 跳转购物车是否正确
        jifen = shouyepage.Jifen(driver)
        jifen.account()
        jifen.shop()
        try:
            assert jifen.try_text(shouyepage.Shouye.title_loc) == "购物车"
            logging.info('跳转购物车')
        except:
            logging.error("跳转购物车错误")
            jifen.get_screenshot("跳转购物车错误")
            raise

    def test_004(self):  # 礼品分类兑换是否正确
        jifen = shouyepage.Jifen(driver)
        jifen.gift()
        try:
            assert jifen.try_text(shouyepage.Jifen.shi_title_loc) == "视听"
            logging.info('礼品分类兑换')
        except:
            logging.error("礼品分类兑换错误")
            jifen.get_screenshot("礼品分类兑换错误")
            raise

    def test_005(self):  # 商品兑换流程是否正确
        jifen = shouyepage.Jifen(driver)
        jifen.jifen()
        try:
            assert jifen.try_text(shouyepage.Shouye .title_loc) == "订单确认"
            logging.info('积分兑换流程')
        except:
            logging.error("商品兑换失败")
            jifen.get_screenshot("商品兑换失败")
            raise

# #升级中
# class TestSearch:
#     def setup(self):  # 每个用例执行进入搜索
#         search = shouyepage.Search(driver)
#         search.search()
#
#     def teardown(self):  # 每个用例结束返回
#         search = shouyepage.Search(driver)
#         search.close()
#
#     def test_001(self):  # 跳转搜索是否正确
#         search = shouyepage.Search(driver)
#         time.sleep(2)
#         try:
#             assert search.try_text(shouyepage.Shouye.title_loc) == "搜索"
#             logging.info('跳转搜索页')
#         except:
#             logging.error("跳转搜索错误")
#             search.get_screenshot("跳转搜索错误")
#             raise
#
#     def test_002(self):  # 跳转搜索是否有热搜
#         search = shouyepage.Search(driver)
#         time.sleep(2)
#         try:
#             assert search.try_find(shouyepage.Search.resou_loc) is True
#             logging.info('搜索也有热搜')
#         except:
#             logging.error("搜索页无热门搜索")
#             search.get_screenshot("搜索页无热门搜索")
#             raise
#
#     def test_003(self):  # 搜索流程是否正确
#         search = shouyepage.Search(driver)
#         search.chazhao("增值业务")
#         time.sleep(5)
#         search.chazhao("增值业务")
#         search.choose()
#         try:
#             assert search.try_text(shouyepage.Shouye.title_loc) != "搜索"
#             logging.info('搜索流程正确')
#         except:
#             logging.error("搜索流程错误")
#             search.get_screenshot("搜索流程错误")
#             raise
#         finally:
#             search.close()
#
#     def test_004(self):  # 搜索无结果是否有推荐内容
#         search = shouyepage.Search(driver)
#         search.chazhao("史蒂夫")
#         try:
#             assert search.try_find(shouyepage.Search.tuijian_loc) is True
#             logging.info('搜索无结果有推荐内容')
#         except:
#             logging.error("搜索无结果没有推荐内容")
#             search.get_screenshot("搜索无结果没有推荐内容")
#             raise
#         finally:
#             search.close()
#
#     def test_005(self):  # 搜索热搜内容--
#         search = shouyepage.Search(driver)
#         search.neirong()
#         try:
#             assert search.try_find(shouyepage.Search.tuijian_loc) is False
#             logging.info('热搜搜索')
#         except:
#             logging.error("搜索热搜内容无结果")
#             search.get_screenshot("搜索热搜内容无结果")
#             raise
#
#     def test_006(self):  # 搜索历史是否正确
#         search = shouyepage.Search(driver)
#         search.neirong()
#         search.back()
#         try:
#             assert search.try_find(shouyepage.Search.lishi_loc) is True
#             logging.info('有搜索历史')
#         except:
#             logging.error("无搜索历史")
#             search.get_screenshot("无搜索历史")
#             raise

class TestCities:
    def setup(self):  # 每个用例执行进入地市
        city = shouyepage.Cities(driver)
        city.dishi()

    def teardown(self):  # 每个用例结束返回
        city = shouyepage.Cities(driver)
        city.back()

    def test_001(self):  # 跳转地市是否正确
        city = shouyepage.Cities(driver)
        try:
            assert city.try_text(shouyepage.Shouye.title_loc) == "省市选择"
            logging.info('跳转地市选择')
        except:
            logging.error("跳转省市选择错误")
            city.get_screenshot("跳转省市选择错误")
            raise

    def test_002(self):  # 省会置顶是否正确
        city = shouyepage.Cities(driver)
        city.search("广东")
        city.choose()
        try:
            assert city.try_text(shouyepage.Cities.c_choose_loc) == "广州"
            logging.info('省会置顶')
        except:
            logging.error("省会不置顶")
            city.get_screenshot("省会不置顶")
            raise
        finally:
            city.back()

    def test_003(self):  # 省市切换流程是否正确
        city = shouyepage.Cities(driver)
        city.qiehuan("广东", "清远")
        city.close_c()
        try:
            assert city.try_text(shouyepage.Cities.city_loc) == "清远"
            logging.info('地市切换成功')
        except:
            logging.error("地市切换错误")
            city.get_screenshot("地市切换错误")
            raise


    def test_004(self):  # 切换省市是否正确
        city = shouyepage.Cities(driver)
        city.search("北京")
        city.choose()
        city.close_c()
        try:
            assert city.try_text(shouyepage.Cities.city_loc) == "北京"
        except:
            logging.error('直辖市直接切换')
            city.get_screenshot("直辖市切换失败")
            raise

class TestScan:
    def setup(self):  # 每个用例执行进入扫一扫
        scan = shouyepage.Scan(driver)
        scan.scan()

    def teardown(self):  # 每个用例结束返回
        scan = shouyepage.Scan(driver)
        scan.back()

    def test_001(self):  # 扫一扫进入
        scan = shouyepage.Scan(driver)
        try:
            assert scan.try_text(shouyepage.Shouye.title_loc) == "扫一扫"
            logging.info('跳转扫一扫')
        except:
            logging.error("未跳转扫一扫")
            scan.get_screenshot("未跳转扫一扫")
            raise

    def test_002(self):  # 非二维码识别
        scan = shouyepage.Scan(driver)
        scan.pic()
        try:
            assert scan.try_text(shouyepage.Scan.tishi_loc) == "图片中未识别到有效的二维码"
            logging.info('非二维码识别')
        except:
            logging.error("本地图片扫码")
            scan.get_screenshot("本地图片扫码")
            raise
        finally:
            scan.zhidao()


# @pytest.mark.skipif(sys.platform =='win32',reason="想跳过")
class TestPackage:
    def setup(self):  # 每个用例执行进入更多icon
        city = shouyepage.Cities(driver)
        city.dishi()
        city.qiehuan("湖南","长沙")
        city.check_adBtn()
        test = shouyepage.Package(driver)
        test.gengduo()

    def teardown(self):  # 每个用例结束返回
        test = shouyepage.Package(driver)
        test.back()
        test.check_adBtn()   #关闭广告

    def test_fenlei(self):  #更多icon跳转到分类页，查看跳转是否正确    新增
        test = shouyepage.Shouye(driver)
        time.sleep(5)
        try:
            assert test.try_text(shouyepage.Shouye.title_loc) == "分类"
            logging.info('更多icon跳转正确')
        except:
            logging.error('更多icon跳转错误')
            test.get_screenshot('更多icon跳转错误')
            raise


    def test_taocanyuliang(self):  # 套餐余量跳转是否正确   新增
        test = shouyepage.Package(driver)
        test.taocan()
        try:
            assert test.try_text(shouyepage.Package.title_loc) == "套餐余量"
            logging.info('套餐余量跳转正确')
        except :
            logging.error('套餐余量跳转错误')
            test.get_screenshot('套餐余量跳转错误')
            raise
        finally:
            test.back()

    def test_liuliangzhichong(self):  #已登录-流量直充流程     新增
        test = shouyepage.Package(driver)
        time.sleep(4)
        test.liuliang()
        time.sleep(3)
        try:
            assert test.try_find(shouyepage.Package.text1_loc) is True
            logging.info('流量直充正确')
        except:
            logging.error('流量直充错误')
            test.get_screenshot('流量直充错误')
            raise
        finally:
            test.return_s()
            test.back()

# @pytest.mark.skipif(sys.platform =='win32',reason="想跳过")
class TestBill:
    def setup(self):  # 每个用例执行进入我的账单
        city = shouyepage.Cities(driver)
        city.dishi()
        city.qiehuan("湖南","长沙")
        city.check_adBtn()
        test = shouyepage.Bill(driver)
        test.gengduo()

    def teardown(self):  # 每个用例结束返回
        test = shouyepage.Bill(driver)
        test.back()
        test.check_adBtn()   #关闭广告

    def test_wdezhangdan(self):  # 跳转我的账单是否正确    新增
        test = shouyepage.Bill(driver)
        time.sleep(3)
        test.bill()
        try:
            assert test.try_text(shouyepage.Shouye.title_loc) == "我的账单"
            logging.error('我的账单跳转正确')
        except:
            logging.info('我的账单跳转错误')
        finally:
            test.back()

    def test_dangyue(self):  # 当月账单是否显示账户余额    新增
        test = shouyepage.Bill(driver)
        time.sleep(3)
        test.bill()
        try:
            assert test.try_find(shouyepage.Bill.yue_loc) is True
            logging.info('单月账单显示账户余额')
        except:
            logging.error('单月账单未账户余额')
            test.get_screenshot('单月账单未账户余额')
            raise
        finally:
            test.back()

    def test_quchongzhi(self):  #去充值按钮跳转否正确     新增
        test = shouyepage.Bill(driver)
        test.bill()
        test.gobutton()
        try:
            assert test.try_text(shouyepage.Shouye.title_loc) == "充值中心"
            logging.info('充值中心跳转正确')
        except:
            logging.error('充值中心跳转错误')
            test.get_screenshot('充值中心跳转错误')
            raise
        finally:
            test.back()
            test.back()


if __name__ == "__main__":
    pytest.main(["s", "shouye_test.py"])
