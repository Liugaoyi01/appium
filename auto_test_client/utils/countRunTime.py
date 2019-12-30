# -*- encoding: utf-8 -*-
"""
@File    : countRunTime.py
@Time    : 2019/12/26 16:26
@Software: PyCharm
"""
import time, logging
import functools


def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        res = func(*args, **kw)
        print('函数%s执行的时间为：%f' % (func.__name__, time.time() - start))
        return res

    return wrapper

