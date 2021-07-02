import os
import datetime
import time

'''
按照执行时间自动生成测试报告文件
'''
def make_file():
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    cur_res = os.path.join('/Users/hudongqi/PycharmProjects/Nice/result', cur_time + '.html')

    return cur_res

