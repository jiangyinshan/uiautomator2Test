import time
import uiautomator2 as u2
from AutoInput import Util
from AutoInput.Keyboard_Key import Keyboard_Key
from AutoInput.manage_case_road import manage_case_road
from AutoInput.openypxl_util import excel
import unittest
import os
import logging


class En_LongClick_Input(unittest.TestCase):
    intputContent = [4, 2]
    expectContent = [4, 3]
    finalContent = [4, 4]
    conclusion = [4, 5]

    def setUp(self):
        logging.info("setup完成")

    def tearDown(self):
        logging.info("tearDown完成")

    def test_start(self):
        """get_road获取xlsx文件路径，创建excel对象"""
        xls_road = manage_case_road().get_road()  # 获取回归用例文件路径
        xls = excel(xls_road)
        deviceName = Util.get_deviceName()
        keyboard = Keyboard_Key(deviceName)
        d = u2.connect_usb(deviceName)
        keyboard.back()
        time.sleep(1)
        keyboard.showKeyboard()
        time.sleep(1)
        """获取xlsx文件中准备进行输入的文本intputContent，预期上屏内容expectContent"""
        inputContent = xls.getCellValue(self.intputContent[0], self.intputContent[1])
        expectContent = xls.getCellValue(self.expectContent[0], self.expectContent[1])

        Util.tapByWord(inputContent)
        keyboard.longClick(keyboard.Sugg, 2)
        time.sleep(1)
        d.click(0.488, 0.546)
        time.sleep(1)
        finalContent = d(className="android.widget.EditText").get_text()
        xls.saveResult(self.finalContent, finalContent)
        xls.containAssert(finalContent, expectContent, self.conclusion)
        d(className="android.widget.EditText").clear_text()
        xls.saveData(xls_road)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Test2是要测试的类名，test_two是要执行的测试方法
    suite.addTest(En_LongClick_Input("test_start"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
