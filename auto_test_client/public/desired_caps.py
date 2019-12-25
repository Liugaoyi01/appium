# coding = utf-8

import os
import sys
from appium import webdriver
import threading
from auto_test_client.utils import getLoger, openYaml

log = getLoger.getLog()
# sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

def appium_desired():
    path = os.path.dirname(os.getcwd())
    driver_path = path+"/config/driver.yaml"
    data = openYaml.get_yaml_data(driver_path)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['udid'] = data['udid']
    log.info("=====准备启动=====")
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    return driver


# threads = []
# t1 = threading.Thread(target=appium_desired)
# threads.append(t1)
#
# t2 = threading.Thread(target=appium_desired2)
# threads.append(t2)

if __name__ == '__main__':
    appium_desired()
