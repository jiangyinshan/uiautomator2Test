# encoding=utf-8
import time
import os
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'iOS',
            'deviceName': 'iphone',
            'platformVersion': '12.4',
            'bundleId': 'com.jack.TongHua',
            'udid': '00008020-001855CC0105002E',
            'startIWDP': 'true'

        }
# 初始化驱动
self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def testRefresh(self):
    # 点击刷新按钮
    self.driver.find_element_by_accessibility_id("btn update").click()


def tearDown(self):
    # 退出
    self.driver.quit()
    #测试


if __name__ == '__main__':
    unittest.main()
