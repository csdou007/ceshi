#coding:utf-8
from libs import baseTest
from libs.ReadExcel import readExcel
from libs.baseTest import testApi
from chuandi.studenttoken import token
from chuandi.jiazhangid import jiazhang
import unittest,json


class testLoginApi(unittest.TestCase):
     def setUp(self):
         pass

     def testLoginApi(self):
         u'''学生给家长发消息'''
         excel = readExcel("E:\\jiekou\\data\\shuju.xlsx")
         name = excel.getName
         data = excel.getData
         url = excel.getUrl
         method = excel.getMethod
         uid = excel.getUid
         code = excel.getCode
         row = excel.getRows
         n=token().testLoginApi()
         m=jiazhang().jia()
         for i in range(2, row - 1):
             if name[i]==u"学生给家长发消息":
                 url[i]=url[i]+n
                 r=json.loads(data[i])
                 r["receivers"]=[m]
             api = testApi(method[i], url[i], str(r))
             apicode = api.getCode()
             print apicode
             apijson = api.getJson()
             if apicode == code[i]:
                 print(u'{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
             else:
                 print(u'{}、{}:测试失败'.format(i + 1, name[i]))

     def tearDown(self):
         pass


