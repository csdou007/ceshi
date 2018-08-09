#coding:utf-8
from libs import baseTest
from libs.ReadExcel import readExcel
from libs.baseTest import testApi
from libs.db import *
from chuandi.config import *
import unittest


class testLoginApi(unittest.TestCase):
     def setUp(self):
         pass

     def testLoginApi(self):
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
             if apicode == code[i]:
                 try:
                    mysql = MySQLEngine()
                    mysql.open(db.host,int(db.port),db.user,db.passwd,db.dbname)
                    (result,affRows)=mysql.searchOne("SELECT * FROM `tb_user` where userName='6502XX00100133'")
                    print result
                    print affRows
                    mysql.close()
                    self.assertEqual(id, result[0], msg='id错误')
                    print(u'{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
                 except Exception as e:
                    print('%s' % e)

             else:
                 print(u'{}、{}:测试失败'.format(i + 1, name[i]))

     def tearDown(self):
         pass


