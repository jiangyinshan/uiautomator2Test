import time
import uiautomator2 as u2
from AutoInput import Util
from AutoInput.Keyboard_Key import Keyboard_Key
from AutoInput.manage_case_road import manage_case_road
from AutoInput.openypxl_util import excel
import unittest
import os
import logging


class Es_ClickSugg_Input(unittest.TestCase):
    intputContent = [6, 2]
    expectContent = [6, 3]
    finalContent = [6, 4]
    conclusion = [6, 5]

    def setUp(self):
        logging.info("西班牙语测试用例setup完成")

    def tearDown(self):
        logging.info("西班牙语测试用例tearDown完成")

    def test_start(self):
        """get_road获取xlsx文件路径，创建excel对象"""
        xls_road = manage_case_road().get_road()  # 获取回归用例文件路径
        xls = excel(xls_road)
        deviceName = Util.get_deviceName()
        keyboard = Keyboard_Key(deviceName)
        d = u2.connect_usb(deviceName)
        d.app_start("com.facebook.orca", "com.facebook.orca.auth.StartScreenActivity")
        time.sleep(2)
        # if keyboard.deviceName == keyboard.yijia7:
        #     d(className="android.widget.EditText").click()
        #     """点击输入messenger框,拉起键盘"""
        # elif keyboard.deviceName == keyboard.sanxing6:
        #     d.xpath('//*[@text="Aa"]').click()
        keyboard.showKeyboard()
        time.sleep(1)
        inputContent = xls.getCellValue(self.intputContent[0], self.intputContent[1])
        expectContent = xls.getCellValue(self.expectContent[0], self.expectContent[1])
        Util.tapByWord(inputContent)
        keyboard.clickSugg()
        finalContent = d(className="android.widget.EditText").get_text()
        xls.saveResult(self.finalContent, finalContent)
        xls.equalAssert(finalContent, expectContent, self.conclusion)
        time.sleep(1)
        d(className="android.widget.EditText").clear_text()
        xls.saveData(xls_road)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Test2是要测试的类名，test_two是要执行的测试方法
    suite.addTest(Es_ClickSugg_Input("test_start"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
