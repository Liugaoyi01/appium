import logging
from logging import config
from os import path
import datetime

'''
    定义一个日志采集器
'''


def getLog():
    log_file_path = 'log.conf'

    CON_LOG = path.join(path.join(path.dirname(path.dirname(path.abspath(__file__))), "config"), log_file_path)

    #  读取配置文件
    config.fileConfig(CON_LOG)  # 读取日志配置表
    #  生成一个日志采集器
    logger = logging.getLogger()  # 定义一个日志采集器
    return logger


if __name__ == '__main__':
    getLog()
