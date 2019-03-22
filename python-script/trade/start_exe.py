import time
import win32api
import win32gui

import win32con


def open_exe(exe_path=None):
    login_hwnd = win32gui.FindWindow("#32770", "用户登录")
    if login_hwnd <= 0:
        if exe_path is None:
            win32api.WinExec("D:\\Program Files (x86)\\CaiTongZhengQuan\\xiadan.exe", win32con.SW_SHOWNORMAL)
        else:
            win32api.WinExec(exe_path, win32con.SW_SHOWNORMAL)
        time.sleep(8)


def get_useful_handle(hwnd, extra):
    if win32gui.GetClassName(hwnd) == "Edit":
        extra.append(hwnd)
    elif win32gui.GetClassName(hwnd) == "Button":
        print(hwnd)


def login(username=None, password=None):
    if username is None:
        exit()
    login_hwnd = win32gui.FindWindow("#32770", "用户登录")

    child_list = []
    win32gui.EnumChildWindows(login_hwnd, get_useful_handle, child_list)
    print(child_list)


if __name__ == '__main__':
    open_exe()
    login(username="name", password="pass")

