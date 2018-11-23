# coding = utf-8
# author = 'liugaoyi'
from appium import webdriver

import yaml


def appium_desired():

    with open('driver.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    driver = webdriver.Remote('http://'+str(data['ip'])+':' + str(data['port'])+'/wd/hub', desired_caps)

    driver.implicitly_wait(30)
    return driver


if __name__ == '__main__':
    appium_desired()