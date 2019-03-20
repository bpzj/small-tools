import win32gui
import win32.lib.win32con as win32con
import win32api
import win32clipboard
import time


# 根据 className 获得主句柄（主窗口）
class_name = "WeChatMainWndForPC"
title_name = "微信"
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
# hwnd = win32gui.FindWindow(class_name, None)
# hwnd = win32gui.FindWindow('Notepad', None)
hwnd = win32gui.FindWindow('ChatWnd', None)
# 根据 className 和 titleName 获得主句柄（主窗口）
# hwnd = win32gui.FindWindow(class_name, title_name)

# 打印句柄，十进制
print("主句柄:", hwnd)
# 获取某个句柄的类名和标题
title = win32gui.GetWindowText(hwnd)
clsname = win32gui.GetClassName(hwnd)

# 将窗口调到前台
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
# 指定句柄设置为前台，也就是激活
win32gui.SetForegroundWindow(hwnd)
# 设置为后台
# win32gui.SetBkMode(hwnd, win32con.TRANSPARENT)

# 获取窗口位置
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)

# 屏幕坐标到客户端坐标
print(win32gui.ScreenToClient(hwnd, (1215, 770)))

# win32api.keybd_event(0x0D, hwnd, 0, 0)
# 这样就是在记事本里按enter键了, 微信不行

# win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 2080193)
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 2080193)
# win32gui.SendMessage(hwnd, win32con.WM_CHAR, 22, 2080193)
# win32gui.SendMessage(hwnd, win32con.WM_PASTE, 0, 0)
win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, None, 'hello')


# win32gui.PostMessage(handle, win32con.WM_PASTE, 0, 0)  # 向窗口发送剪贴板内容

# time.sleep(0.3)

# win32gui.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 向窗口发送 回车键
# win32gui.PostMessage(handle, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 父窗口句柄 若不为0，则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体，否则从第一个子窗体开始搜索。 子窗口类名 子窗口标题
# subHandle = win32gui.FindWindowEx(handle, 0, "EDIT", None)
# print(subHandle)
subHandle = win32gui.FindWindowEx(hwnd, None, None, None)
if subHandle == 0:
    print("未找到子句柄")
else:
    print("第一个个子句柄:", subHandle)
    # 枚举子窗口
    hwndChildList = []
    win32gui.EnumChildWindows(hwnd, lambda handle, param: param.append(handle), hwndChildList)
    print("所有子句柄:", hwndChildList)



