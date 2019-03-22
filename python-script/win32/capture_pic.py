# 截图整个桌面
import win32gui
import win32ui
import win32con
import win32api

# 获取桌面
hdesktop = win32gui.GetDesktopWindow()

# 分辨率适应
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
# 参数定义：
# SM_CXSCREEN = 0 'X Size of screen
# SM_CYSCREEN = 1 'Y Size of Screen
# SM_CXVSCROLL = 2 'X Size of arrow in vertical scroll bar.
# SM_CYHSCROLL = 3 'Y Size of arrow in horizontal scroll bar
# SM_CYCAPTION = 4 'Height of windows caption
# SM_CXBORDER = 5 'Width of no-sizable borders
# SM_CYBORDER = 6 'Height of non-sizable borders
# SM_CXDLGFRAME = 7 'Width of dialog box borders
# SM_CYDLGFRAME = 8 'Height of dialog box borders
# SM_CYHTHUMB = 9 'Height of scroll box on horizontal scroll bar
# SM_CXHTHUMB = 10 ' Width of scroll box on horizontal scroll bar
# SM_CXICON = 11 'Width of standard icon
# SM_CYICON = 12 'Height of standard icon
# SM_CXCURSOR = 13 'Width of standard cursor
# SM_CYCURSOR = 14 'Height of standard cursor
# SM_CYMENU = 15 'Height of menu
# SM_CXFULLSCREEN = 16 'Width of client area of maximized window
# SM_CYFULLSCREEN = 17 'Height of client area of maximized window
# SM_CYKANJIWINDOW = 18 'Height of Kanji window
# SM_MOUSEPRESENT = 19 'True is a mouse is present
# SM_CYVSCROLL = 20 'Height of arrow in vertical scroll bar
# SM_CXHSCROLL = 21 'Width of arrow in vertical scroll bar
# SM_DEBUG = 22 'True if deugging version of windows is running
# SM_SWAPBUTTON = 23 'True if left and right buttons are swapped.
# SM_CXMIN = 28 'Minimum width of window
# SM_CYMIN = 29 'Minimum height of window
# SM_CXSIZE = 30 'Width of title bar bitmaps
# SM_CYSIZE = 31 'height of title bar bitmaps
# SM_CXMINTRACK = 34 'Minimum tracking width of window
# SM_CYMINTRACK = 35 'Minimum tracking height of window
# SM_CXDOUBLECLK = 36 'double click width
# SM_CYDOUBLECLK = 37 'double click height
# SM_CXICONSPACING = 38 'width between desktop icons
# SM_CYICONSPACING = 39 'height between desktop icons
# SM_MENUDROPALIGNMENT = 40 'Zero if popup menus are aligned to the left of the memu bar item. True if it is aligned to the right.
# SM_PENWINDOWS = 41 'The handle of the pen windows DLL if loaded.
# SM_DBCSENABLED = 42 'True if double byte characteds are enabled
# SM_CMOUSEBUTTONS = 43 'Number of mouse buttons.
# SM_CMETRICS = 44 'Number of system metrics
# SM_CLEANBOOT = 67 'Windows 95 boot mode. 0 = normal, 1 = safe, 2 = safe with network
# SM_CXMAXIMIZED = 61 'default width of win95 maximised window
# SM_CXMAXTRACK = 59 'maximum width when resizing win95 windows
# SM_CXMENUCHECK = 71 'width of menu checkmark bitmap
# SM_CXMENUSIZE = 54 'width of button on menu bar
# SM_CXMINIMIZED = 57 'width of rectangle into which minimised windows must fit.
# SM_CYMAXIMIZED = 62 'default height of win95 maximised window
# SM_CYMAXTRACK = 60 'maximum width when resizing win95 windows
# SM_CYMENUCHECK = 72 'height of menu checkmark bitmap
# SM_CYMENUSIZE = 55 'height of button on menu bar
# SM_CYMINIMIZED = 58 'height of rectangle into which minimised windows must fit.
# SM_CYSMCAPTION = 51 'height of windows 95 small caption
# SM_MIDEASTENABLED = 74 'Hebrw and Arabic enabled for windows 95
# SM_NETWORK = 63 'bit o is set if a network is present.
# SM_SECURE = 44 'True if security is present on windows 95 system
# SM_SLOWMACHINE = 73 'true if machine is too slow to run win95.


# 创建设备描述表
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# 创建一个内存设备描述表
mem_dc = img_dc.CreateCompatibleDC()

# 创建位图对象
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)

# 截图至内存设备描述表
mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

# 将截图保存到文件中
screenshot.SaveBitmapFile(mem_dc, 'screenshot.bmp')

# 内存释放
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())