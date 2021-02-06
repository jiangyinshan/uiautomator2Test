import time
import uiautomator2 as u2
from AutoInput import Util
from AutoInput.Keyboard_Key import Keyboard_Key
from AutoInput.manage_case_road import manage_case_road
from AutoInput.openypxl_util import excel
import unittest
import os
import logging


class EnterHomePage(unittest.TestCase):
    intputContent = [5, 2]
    expectContent = [5, 3]
    finalContent = [5, 4]
    conclusion = [5, 5]

    def setUp(self):
        logging.info("setup完成")

    def tearDown(self):
        logging.info("tearDown完成")

    def test_start(self):
        deviceName = Util.get_deviceName()
        keyboard = Keyboard_Key(deviceName)
        d = u2.connect_usb(deviceName)
        d.app_start("kika.emoji.keyboard.teclados.clavier")
        time.sleep(7)
        keyboard.closeOpenAD()
        time.sleep(2)
        keyboard.clickUserTabButton()
        time.sleep(1)
        keyboard.clickLanguageButton()
        time.sleep(1)
        keyboard.addEspanol()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Test2是要测试的类名，test_two是要执行的测试方法
    suite.addTest(EnterHomePage("test_start"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
