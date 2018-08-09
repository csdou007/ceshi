#coding:utf-8
import requests
import json
from libs import ReadExcel
#from pubulic_way.get_token import get_token

class testApi(object):
     def __init__(self, method, url, data):
         self.method = method
         self.url = url
         self.data = data
         self.headers={"Content-Type":"application/json"}

     @property #装饰器作为一个属性
     def testApi(self):
         # 根据不同的访问方式来访问接口
         try:
             if self.method == 'post':
                 r = requests.post(self.url, data=json.dumps(eval(self.data)), headers=self.headers)
                 print r.cookies
             elif self.method == 'get':
                 r = requests.get(self.url, params=eval(self.data))
                 print r.cookies
             return r
         except:
             print('失败')


     def getCode(self):
         # 获取访问接口的状态码
         code = self.testApi.status_code
         return code

     def getJson(self):
         # 获取返回信息的json数据
         json_data = self.testApi.json()
         return json_data
