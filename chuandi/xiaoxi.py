#coding:utf-8
from chuandi.studenttoken import token
import requests,json,unittest




class testLoginApi(unittest.TestCase):
     def test_LoginApi(self):
         u'''学生给家长发消息'''
         url="http://at.ilr1000.com/api/messages.json?token="
         headers={"Content-Type": "application/json;charset=utf-8"
               }

         n=token().testLoginApi()
         params={
                "title":"autotest",
 "receivers":[147539],
 "content":"test content"
                }
         print params
         print type(params)
         r=requests.post(url=url+n,json=params,headers=headers)
         #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
         print(r.status_code)
         self.assertEqual(r.status_code,200)
         #通过text方法获取到响应报文的内容
         repones=r.text
         print r.text


