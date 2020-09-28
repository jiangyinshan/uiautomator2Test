import os

from AutoInput.Keyboard_Key import Keyboard_Key


def tapByWord(word):
    k = Keyboard_Key(get_deviceName())
    for i in word:
        k.tapWord(i)


def get_deviceName():
    """通过adb获取设备名称"""
    values = os.popen("adb devices").readlines()
    try:
        dev = values[1].split()[0]
        if len(values) == 3:
            print(u'手机设备为：' + dev)
            return dev
        elif len(values) >= 4:
            print(u'电脑连接的设备超过一个，请确保只连接一个设备')
    except IndexError:
        print("Index错误，没有连接任何设备")
    return dev
