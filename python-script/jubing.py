
# -*- coding: utf-8 -*-

import win32con
import win32gui
import time


titles = set()
wx = 0


def foo(hwnd, mouse):
    # 去掉下面这句就所有都输出了，但是我不需要那么多
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        titles.add(title)
        if title == '微信':
            print(hwnd)


win32gui.EnumWindows(foo, 0)

lt = [t for t in titles if t]
lt.sort()
for t in lt:
    print(t)

hwnd = 723410
win32gui.PostMessage(hwnd, win32con.WM_PASTE, 0, 0)  # 向窗口发送剪贴板内容

time.sleep(0.3)

win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 向窗口发送 回车键
win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

