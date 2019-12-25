import yaml
from os import path
'''
    定义一个yaml文件读取方法
'''


def get_yaml_data(file_path):

    with open(file_path, "r", encoding='utf-8') as fp:
        data = yaml.load(fp)
        return data
