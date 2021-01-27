import unittest
import uiautomator2 as u2

from AutoInput import Util
from AutoInput.Keyboard_Key import Keyboard_Key


class En_AutoCorrect_Input:
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teatDown")

    def case(self):
        deviceName = Util.get_deviceName()
        keyboard = Keyboard_Key(deviceName)
        d = u2.connect_usb(deviceName)
        print(d.info)
