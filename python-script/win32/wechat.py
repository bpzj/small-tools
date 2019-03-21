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
    args = list(args)
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYDOWN, arg, 0)

    args.reverse()
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYUP, arg, 0)


def get_right_click_pos(handle):
    """
    根据句柄获得右键点击的坐标，右键点击此坐标后，弹出粘贴按钮
    """
    # 此坐标为： 真实分辨率 / 屏幕缩放比列
    left, top, right, bottom = win32gui.GetWindowRect(handle)
    horizontal = 96     # 水平间距, X方向
    vertical = 64       # 垂直间距, Y方向
    return left + horizontal, bottom-vertical


def get_paste_pos_from_right_click(right_click_pos):
    """
    根据 右键点击的位置，获取粘贴按钮出现的位置
    :param right_click_pos:
    :return:
    """
    return right_click_pos[0]+10, right_click_pos[1]+6


def click_right_at_pos(position, sleep_time=0.1):
    """
    在 pos位置单击 鼠标右键
    使用 mouse_event api，在 SendMessage api无效时使用
    """
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    time.sleep(sleep_time)


def click_left_at_pos(position, sleep_time=0.1):
    """
    在 pos 位置单击 鼠标左键键
    使用 mouse_event api，在 SendMessage api无效时使用
    """
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(sleep_time)


def click_ctrl_v():
    """
    定义组合按键 使用 keybd_event api，在 SendMessage api无效时使用
    """
    win32api.keybd_event(win32con.VK_LCONTROL, 0, 0, 0)
    win32api.keybd_event(win32api.VkKeyScan('v'), 0, 0, 0)
    win32api.keybd_event(win32api.VkKeyScan('v'), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_LCONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def click_ctrl_v():
    """
    定义组合按键 使用 keybd_event api，在 SendMessage api无效时使用
    """
    win32api.keybd_event(win32con.VK_LCONTROL, 0, 0, 0)
    win32api.keybd_event(win32api.VkKeyScan('v'), 0, 0, 0)
    win32api.keybd_event(win32api.VkKeyScan('v'), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_LCONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def wechat_send_msg(handle, content):
    """
    微信发送消息的操作
    :param handle: 句柄
    :param content
    :return:
    """

    # 点击聊天文本框，SendMessage 方法模拟鼠标点击，对微信无效果，使用 mouse_event 方法
    pos = get_right_click_pos(handle)
    # 左键点击输入框
    click_left_at_pos(pos, sleep_time=0.1)
    # 方法一：直接向输入框发送字符
    for char in list(content):
        win32api.PostMessage(handle, win32con.WM_CHAR, ord(char), 0)
    time.sleep(0.1)

    # 方法二：先把内容放到粘贴板，然后按 模拟 ctrl v 按键
    # set_text(content)
    # click_ctrl_v()
    # time.sleep(0.1)

    #
    # 方法三：右键弹出 粘贴按钮，左键点击 粘贴按钮
    # click_right_at_pos(pos)
    # click_left_at_pos(get_paste_pos_from_right_click(pos), sleep_time=0.2)

    # 发送 enter 键，使用 SendMessage api 可以成功
    send_keys(handle, win32con.VK_RETURN)

    #
    #
    # SendMessage 方法模拟 ctrl v 组合键，对微信无效果
    # send_keys(hwd, win32con.VK_LCONTROL, win32api.VkKeyScan("v"))
    #


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
    # print(win32gui.ScreenToClient(hwnd, (1206, 744)))
    # right_click = get_right_click_pos(hwnd)
    # print(right_click)

    for i in range(0, 1):
        wechat_send_msg(hwnd, "你\n在")

