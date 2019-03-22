import win32gui
import win32ui
import win32con


def cap_img(handle=None):
    hwnd = 0xA0b12
    hwnd = 0x70810
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = int((right - left)/1.25)
    h = int((bot - top)/1.25)

    # 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hwndDC = win32gui.GetWindowDC(hwnd)

    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()

    # 创建位图对象
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)

    # 截图至内存设备描述表
    img_dc = mfcDC
    mem_dc = saveDC
    mem_dc.BitBlt((0, 0), (w, h), img_dc, (125, 125), win32con.SRCCOPY)

    # 将截图保存到文件中
    saveBitMap.SaveBitmapFile(mem_dc, 'screenshot1.bmp')
    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)


if __name__ == '__main__':
    cap_img()
