import win32gui
import win32.lib.win32con as win32con
import win32api
import win32clipboard
import time


def get_text():
    # 读取剪切板
    win32clipboard.OpenClipboard()
    d = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()
    return d


def set_text(string):
    # 写入剪切板
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, string.encode(encoding='gbk'))
    win32clipboard.CloseClipboard()


def send_keys(hwd, *args):
    """
    定义组合按键
    """
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYDOWN, arg, 0)
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYUP, arg, 0)


def send_click_left(hwd, x_position, y_position, sleep):
    """
    鼠标左键点击指定坐标，使用 SendMessage api对微信不起作用
    :param hwd:
    :param x_position:
    :param y_position:
    :param sleep:
    :return:
    """
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    # win32api.SendMessage(hwnd, win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP, long_position)
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
    time.sleep(int(sleep))


def send_click_right(hwd, x_position, y_position, sleep):
    """
    鼠标左键点击指定坐标
    :param hwd:
    :param x_position:
    :param y_position:
    :param sleep:
    :return:
    """
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    # win32api.SendMessage(hwnd, win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP, long_position)
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_RBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_RBUTTON, long_position)
    time.sleep(int(sleep))


def input_content(hwd, content, sleep, is_enter):
    """
    从站贴板中查找输入的内容
    :param hwd:
    :param content:
    :param sleep:
    :param is_enter 是否要在最后输入enter键,内容与enter之间间隔一秒
    :return:
    """
    set_text(content)
    time.sleep(0.3)
    # click_keys(hwd, win32con.VK_CONTROL, 86)
    send_keys(hwd, win32con.VK_LCONTROL, win32api.VkKeyScan("v"))
    if is_enter:
        time.sleep(1)
        send_keys(hwd, win32con.VK_RETURN)
    time.sleep(sleep)