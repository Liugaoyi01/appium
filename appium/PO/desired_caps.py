# coding = utf-8

from appium import webdriver
import yaml
import logging
from logging import config
import threading

CON_LOG = '../Log/log.conf'
config.fileConfig(CON_LOG)  # 读取日志配置表
logging = logging.getLogger()  # 定义一个日志采集器
# from os import path
# log_file_path = path.join(path.dirname(path.abspath(__file__)), '../Log/log.conf')
# fileConfig(log_file_path)
# logging = logging.getLogger()  # 定义一个日志采集器


def appium_desired():
    with open("..\Yaml\driver.yaml", "r", encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['udid'] = data['udid']

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    return driver

def appium_desired2():
    with open("..\Yaml\driver.yaml", "r", encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps2 = {}
    desired_caps2['platformName'] = data['platformName']
    desired_caps2['deviceName'] = data['deviceName2']
    desired_caps2['platformVersion'] = data['platformVersion']
    desired_caps2['appPackage'] = data['appPackage']
    desired_caps2['appActivity'] = data['appActivity']
    desired_caps2['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps2['resetKeyboard'] = data['resetKeyboard']
    desired_caps2['udid'] = data['udid2']

    driver2 = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port2']) + '/wd/hub', desired_caps2)
    driver2.implicitly_wait(30)
    return driver2

threads = []
t1 = threading.Thread(target=appium_desired)
threads.append(t1)

t2 = threading.Thread(target=appium_desired2)
threads.append(t2)

if __name__ == '__main__':
    # for t in threads:
    #     t.start()
    appium_desired()
