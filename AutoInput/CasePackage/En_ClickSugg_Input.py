import time
import uiautomator2 as u2
from AutoInput import Util
from AutoInput.Keyboard_Key import Keyboard_Key
from AutoInput.manage_case_road import manage_case_road
from AutoInput.openypxl_util import excel
import unittest


class CaseOne(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("tearDown")
    def case(self):
        deviceName = Util.get_deviceName()
        keyboard = Keyboard_Key(deviceName)
        d = u2.connect_usb(deviceName)
        print(d.info)
        d.app_start("com.facebook.orca", "com.facebook.orca.auth.StartScreenActivity")
        if keyboard.deviceName == keyboard.yijia7:
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[4]').click()
            """点击messenger对话框"""
        elif keyboard.deviceName == keyboard.sanxing6:
            d.xpath(
                '//android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[4]').click()
        time.sleep(1)
        if keyboard.deviceName == keyboard.yijia7:
            d(className="android.widget.EditText").click()
            """点击输入messenger框,拉起键盘"""
        elif keyboard.deviceName == keyboard.sanxing6:
            d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        time.sleep(1)

        xls_road = manage_case_road().get_road()  # 获取回归用例文件路径
        xls = excel(xls_road)
        """get_road获取xlsx文件路径，创建excel对象"""
        words = xls.getCellValue(2, 2)
        Util.tapByWord(words)
        print("words为:" + words)
        text = d(className="android.widget.EditText").get_text()
        xls.setCellValue(9, 5, text)
        if text is not None or text != "":
            xls.setCellValue(9, 4, "通过")
        else:
            xls.setCellValue(9, 4, "未通过")
        d(className="android.widget.EditText").clear_text()
        xls.saveData(xls_road)
        print("text为:" + text)
        # a = init_device("Android")
        # print("Airtest初始化成功")
        # touch(Template("/Users/xm20190901/Downloads/tpl1611647488736.png", record_pos=(0.332, 0.297),
        #                resolution=(1080, 2340)))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # Test2是要测试的类名，test_two是要执行的测试方法
    suite.addTest(CaseOne("case"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
