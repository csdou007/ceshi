#coding:utf-8
from libs import baseTest
from libs.ReadExcel import readExcel
from libs.baseTest import testApi


class jiazhang():
     def jia(self):
         u'''家长登录接口'''
         excel = readExcel("E:\\jiekou\\data\\shuju.xlsx")
         name = excel.getName
         data = excel.getData
         print type(data)
         url = excel.getUrl
         method = excel.getMethod
         uid = excel.getUid
         code = excel.getCode
         row = excel.getRows
         for i in range(1, row - 2):
             api = testApi(method[i], url[i], data[i])
             apicode = api.getCode()
             apijson = api.getJson()
             id=apijson["user"]["id"]
             print id
         return id




