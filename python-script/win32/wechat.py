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


def click_right(hwd, x_position, y_position, sleep):
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


def click_keys(hwd, *args):
    """
    定义组合按键
    :param hwd:
    :param args:
    :return:
    """
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYDOWN, arg, 0)
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYUP, arg, 0)


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
    click_keys(hwd, win32con.VK_LCONTROL, win32api.VkKeyScan("v"))
    if is_enter:
        time.sleep(1)
        click_keys(hwd, win32con.VK_RETURN)
    time.sleep(sleep)


def wechat_send_msg(hwd, content):
    """
    阿里旺旺的操作
    :param hwd: 句柄
    :param content
    :return:
    """
    set_text(content)

    # 点击聊天文本框，SendMessage 方法模拟鼠标点击，对微信无效果，使用 mouse_event 方法
    # 右键弹出 粘贴按钮
    pos = (1000, 620)
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    time.sleep(0.1)
    pos_2 = (pos[0]+10, pos[1]+6)
    win32api.SetCursorPos(pos_2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    time.sleep(0.1)
    # 发送 enter 键
    click_keys(hwd, win32con.VK_RETURN)

    #
    #
    #
    # SendMessage 方法模拟鼠标点击，对微信无效果
    # click_keys(hwd, win32con.VK_RETURN)
    # time.sleep(1)
    # click_keys(hwd, win32api.VkKeyScan("1"))
    # win32gui.SendMessage(hwnd, win32con.WM_PASTE, 0, 0)
    # click_keys(hwd, win32con.VK_RETURN)
    # input_content(hwd, content, 1, False)

    # 发送 enter 键
    # click_keys(hwd, win32con.VK_RETURN)

    # 点击发送消息
    # click_position(hwd, 847, 782, 1)


if __name__ == '__main__':
    # 查找句柄
    hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
    if hwnd <= 0:
        print("未找到微信")
        exit()

    # 打印句柄，十进制
    print("找到微信主句柄:", hwnd)

    hwnd = win32gui.FindWindow('ChatWnd', None)
    if hwnd <= 0:
        print("未找到聊天窗口")
        exit()

    # 将窗口调到前台，激活
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(hwnd)

    # 屏幕坐标到客户端坐标
    print(win32gui.ScreenToClient(hwnd, (1206, 744)))

    for i in range(1, 100):
        wechat_send_msg(hwnd, "haha")

