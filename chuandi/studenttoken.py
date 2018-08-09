#coding:utf-8
from libs import baseTest
from libs.ReadExcel import readExcel
from libs.baseTest import testApi
class token():
    def testLoginApi(self):
         u'''学生登录接口'''
         excel = readExcel("E:\\jiekou\\data\\shuju.xlsx")
         name = excel.getName
         data = excel.getData
         url = excel.getUrl
         method = excel.getMethod
         uid = excel.getUid
         code = excel.getCode
         row = excel.getRows
         for i in range(0, row - 3):
             api = testApi(method[i], url[i], data[i])
             apicode = api.getCode()
             apijson = api.getJson()
             token=apijson["token"]
             print token
         return token