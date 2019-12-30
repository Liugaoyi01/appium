# coding = utf-8
from time import ctime
import os
import sys
from appium import webdriver
import multiprocessing

from auto_test_client.utils import getLoger, openYaml
from auto_test_client.public.startFunction import start_index

log = getLoger.getLog()
# sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
path = os.path.dirname(os.getcwd())
driver_path = path + "/config/driver.yaml"
data = openYaml.get_yaml_data(driver_path)


def appium_desired(udid, port):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['udid'] = udid
    log.info('appium port:%s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    # 多进程启动
    start_index(driver)
    return driver


def creat_process_list():
    # 设备列表
    devices_list = ['P79LPJUO9DM7PZF6', 'HB6CE1RPL002YU']
    # 构建desired进程租
    desired_process = []

    for i in range(len(devices_list)):
        port = 4723 + 3 * i
        desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))
        desired_process.append(desired)
    return desired_process


if __name__ == '__main__':
    # 启动多设备执行测试
    desired_process = creat_process_list()
    # appium_desired('P79LPJUO9DM7PZF6', 4723)
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()
