import requests
from Base import read_yaml
import json


class RequestBase:

    def __init__(self,request_num,intf_type=None):
        """
        请求接口公共类
        :param request_num: request.yaml中对应的几号请求
        :param intf_type:  接口类型：webservice， api，分别对应接口数据格式：xml， json
        """
        self.request_type = read_yaml.ReadYaml().get_value('request.yaml',request_num +'.request_type')
        self.request_url = read_yaml.ReadYaml().get_value('request.yaml',request_num +'.url')
        self.request_body = read_yaml.ReadYaml().get_value('request.yaml',request_num +'.payload')
        self.request_headers = read_yaml.ReadYaml().get_value('request.yaml',request_num +'.headers')

        self.intf_type = intf_type
        self.res = self.__send_request()

    # 发送请求
    def __send_request(self):
        if not isinstance(self.request_type, str):
            print('请求类型格式错误。')
            return None
        if self.request_type.upper() not in ['GET', 'POST']:
            print('请求类型不存在。')
            return None
        res = requests.request(method=self.request_type, url=self.request_url, data=self.request_body.encode('utf-8'), headers=self.request_headers)
        return res

    # 获取响应
    def get_respond(self):
        return self.res

    # 获取响应头
    def get_respond_head(self):
        head = self.res.headers
        return head

    # 获取响应体
    def get_respond_body(self):
        res_body = self.res.content
        return json.loads(res_body)

