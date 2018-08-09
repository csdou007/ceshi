#-*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import os,time
list="E:\\jiekou\\testcases\\"
REPORT_PATH = "E:\\jiekou\\report\\testreport"
def createsuit():
    testunit=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(list,pattern='*.py',top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:

            testunit.addTest(test_case)
            print(testunit)
    return testunit
alltestnames=createsuit()


now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
result_dir = REPORT_PATH + day

if os.path.exists(result_dir):

    filename=result_dir+"\\"+now+'report.html'
    fp=file(filename,'wb')


    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                       title=u'接口测试',
                                                       description=u'用例执行情况:')
    runner.run(alltestnames)
    fp.close()
else:
    os.mkdir(result_dir)
    filename=result_dir+"\\"+now+'report.html'
    fp=file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                       title=u'接口测试',
                                                       description=u'用例执行情况:')

    runner.run(alltestnames)
    fp.close()