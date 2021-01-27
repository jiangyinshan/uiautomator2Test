from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# 通过ADB连接本地Android设备
init_device()
print("Airtest初始化成功")
touch(Template("/Users/xm20190901/Downloads/tpl1611647488736.png", record_pos=(0.332, 0.297), resolution=(1080, 2340)))