import time
import uiautomator2 as u2
from AutoInput import Util
from AutoInput.Keyboard_Key import Keyboard_Key
from AutoInput.manage_case_road import manage_case_road
from AutoInput.openypxl_util import excel
import unittest
import os
import logging


class En_ClickSugg_Input(unittest.TestCase):
    intputContent = [2, 2]
    expectContent = [2, 3]
    finalContent = [2, 4]
    conclusion = [2, 5]

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
        d.app_start("com.facebook.orca", "com.facebook.orca.auth.StartScreenActivity")
        if keyboard.deviceName == keyboard.yijia7:
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[4]').click()
            """点击messenger对话框"""
        elif keyboard.deviceName == keyboard.sanxing6:
            d.xpath(
                '//android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[4]').click()
        time.sleep(1)

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
    suite.addTest(En_ClickSugg_Input("test_start"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
