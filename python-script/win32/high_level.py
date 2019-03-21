import win32gui
import win32.lib.win32con as win32con
import win32api
import win32process
import win32clipboard
import time


def get_hwnds_for_Class(class_name):
    """
    获得所有 符合 class name 的 句柄
    """
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            if class_name == win32gui.GetClassName(hwnd):
                hwnds.append(hwnd)
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


# 获取微信 单独聊天窗口的 句柄
wx = 0
hwnds = get_hwnds_for_Class(class_name='ChatWnd')
for hwnd in hwnds:
    title = win32gui.GetWindowText(hwnd)
    print(title, '窗口句柄:', hwnd)
    if title == '哈哈':
        wx = hwnd

print(wx)
# win32process.GetWindowThreadProcessId()
# 参数：窗口句柄 handle to the window
# 结果：The result is a tuple of (threadId, processId)
threadId, processId = win32process.GetWindowThreadProcessId(wx)
print(threadId)
tid = win32api.GetCurrentThreadId()
# AttachThreadInput 参数：
#       idAttach : int    The id of a thread
#       idAttachTo : int  The id of the thread to which it will be attached
#       Attach : bool
win32process.AttachThreadInput(tid, threadId, 1)


# 将窗口调到前台，激活
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
win32gui.SetForegroundWindow(hwnd)

s = '你的我的的'
for char in list(s):
    win32api.PostMessage(wx, win32con.WM_CHAR, ord(char), 0)

print(ord(s))

# win32api.PostMessage(wx, win32con.WM_CHAR, 65, 0)
# win32api.PostMessage(wx, win32con.WM_CHAR, 85, 0)
# win32api.PostMessage(wx, win32con.WM_CHAR, ord(s), 0)


win32api.PostMessage(wx, win32con.WM_KEYUP, win32con.VK_CONTROL, 0)


