import requests
from Nice_tools.nice_datebase import Nice_db
import json
import cookiejar
import pdfplumber
import pandas as pd
import camelot

url = 'http://api.snowy.lab.oneniceapp.com/Log/changeStorageGatherStatus'

apply_id = 422124716325601768
# 接口方法
# 到仓
data1 = {'apply_id':apply_id,'detail_id':'','status':'nice_recv'}

# sql
sql = 'select * from storage_gather_apply_item_detail where apply_id = 422124716325601768 '

# 改状态
data2 ={'apply_id':apply_id,'detail_id':'417227451099775664','status':'nice_recv','flaw_degree':'slight',\
        'refuse_reason':'假货','recv_all':'1','money':'950','repair':'no'}

# 加多件
url2 = 'http://api.snowy.lab.oneniceapp.com/Log/addAdditionalDetail'
data3 = {'detail_id':416132911965669705,'goods_id':99037,'size_id':10112,'apply_ids':apply_id}




d = Nice_db()
len1 = d.get_cell_value(10011,sql)

class Baserequest:
        def send_get(self,url,data1):
                res = requests.get(url=url,params=data1).json()
                return res
test1 = Baserequest()

# 收货
def nice_recv():

        for i in len1[:19]:
                data1['detail_id'] = i
                res = test1.send_get(url,data1)

        print(res)

# 加多件
def add_kucun():
        #             数量
        for i in range(3):

                res1 = test1.send_get(url2,data3)
                data3['detail_id']+=1
                #a = int(data3['detail_id']) + 1
                #data3['detail_id'] = a
        print(res1)

# 全部到仓
def allrecive():
        data1['detail_id'] = len1[0]
        data1["recv_all"] = "1"
        res = test1.send_get(url,data1)
        print(res)


# 改状态
def change_staus():

        for i in len1[14:25]:
                data1['detail_id'] = i
                data1['status'] = 'pass'
                # data1['flaw_degree'] = 'common'
                #data1['refuse_reason'] = '使用痕迹'
                # data1['money'] = '5'
                # data1['repair'] = 'yes'
                res = test1.send_get(url,data1)
        print(res)



if __name__ == '__main__':
        nice_recv()
        #change_staus()
        #add_kucun()
        #allrecive()



    





