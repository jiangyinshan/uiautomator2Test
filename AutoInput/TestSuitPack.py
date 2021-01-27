import os

from HtmlTestRunner import HTMLTestRunner
from airtest.core.api import *
import time
import uiautomator2 as u2
from AutoInput import Util
from AutoInput.CasePackage import En_ClickSugg_Input
from AutoInput.Keyboard_Key import Keyboard_Key
from AutoInput.manage_case_road import manage_case_road
from AutoInput.openypxl_util import excel
import unittest
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 使用这种方法可以对测试用例排序
    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # suite.addTests(tests)
    suite.addTest(En_ClickSugg_Input.CaseOne("case"))
    # 使用TestLoader的方法传入TestCase
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(En_ClickSugg_Input.CaseOne))
    # 在同目录下生成txt格式的测试报告
    # with open('UnittestTextReport.txt', 'a') as f:
    # runner = unittest.TextTestRunner(stream=f, verbosity=2)
    # runner.run(suite)
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                report_title=u'测试报告',
                                verbosity=2,
                                output="/Users/xm20190901/PycharmProjects/uiautomator2Test/AutoInput/Reports"
                                )
        runner.run(suite)
