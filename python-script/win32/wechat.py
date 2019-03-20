import win32gui
import win32.lib.win32con as win32con
import win32api
import win32clipboard
import time


def click_position(hwd, x_position, y_position, sleep):
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
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
    time.sleep(int(sleep))


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


if __name__ == '__main__':
    # 查找句柄
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
    if hwnd <= 0:
        print("未找到微信")
        exit()

    # 打印句柄，十进制
    print("找到微信主句柄:", hwnd)
    # 屏幕坐标到客户端坐标
    print(win32gui.ScreenToClient(hwnd, (1206, 744)))
