#coding:utf-8
from libs import baseTest
from libs.ReadExcel import readExcel
from libs.baseTest import testApi
import unittest


class testLoginApi(unittest.TestCase):
     def setUp(self):
         pass

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
             if apicode == code[i]:
                 print(u'{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
             else:
                 print(u'{}、{}:测试失败'.format(i + 1, name[i]))

     def tearDown(self):
         pass


