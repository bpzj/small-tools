import os
import re
from sre_parse import Pattern

path = r"D:\Android\sdk\platform-tools\adb.exe "
adb_devices = path + r"devices"


def exe_out(command):
    # popen() 返回文件对象，跟open操作一样
    file = os.popen(command, "r")
    info = file.read()
    file.close()
    return info


def link_device():
    info = exe_out(adb_devices)
    s = info.split("\n")  # 切割换行
    serials = [x for x in s if x.find('List of devices') < 0 and x != ""]  # 去掉空''
    # 可能有多个手机设备  获取设备名称
    devices = []
    for serial in serials:
        devices.append(str(serial).replace('\tdevice', ''))
    if not devices:
        print("手机没连上")
    else:
        print("当前手机序列号:%s" % str(devices))
    return devices


def get_device_info(serial=""):
    if serial == "":
        pass


def current_ui():
    exe_out(path + "shell uiautomator dump")
    exe_out(path + r"pull /sdcard/window_dump.xml D:\adb_pull")
    f = open(r"D:\adb_pull\window_dump.xml", "r", encoding='UTF-8')
    data = f.read()
    f.close()
    return data


def monkey_app(package):
    print(exe_out(path + r'shell monkey -p ' + package + " 1"))


def open_app(activity):
    print(exe_out(path + r'shell am start -n ' + activity))


def tap_x1_y1_x2_y2(x_y_scope):
    x = (int(x_y_scope[0]) + int(x_y_scope[2])) / 2
    y = (int(x_y_scope[1]) + int(x_y_scope[3])) / 2
    exe_out(path + r"shell input tap " + str(x) + " " + str(y))


def tap_by_content_regexp(pattern: str, ui_content=None):
    if not ui_content:
        ui_content = current_ui()

    pos_str = re.findall(re.compile(pattern, re.S), ui_content)
    if pos_str:
        tap_x1_y1_x2_y2(str(pos_str[0]).replace("][", ",").replace("[", "").replace("]", "").split(","))


if __name__ == '__main__':
    link_device()
    exe_out(path)
