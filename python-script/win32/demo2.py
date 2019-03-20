import win32gui
import win32.lib.win32con as win32con
import win32api

# 从顶层窗口向下搜索主窗口，无法搜索子窗口
# FindWindow(lpClassName=None, lpWindowName=None)  窗口类名 窗口标题名
handle = win32gui.FindWindow("Notepad", None)


# 获取窗口位置
left, top, right, bottom = win32gui.GetWindowRect(handle)
# 获取某个句柄的类名和标题
title = win32gui.GetWindowText(handle)
clsname = win32gui.GetClassName(handle)

# 打印句柄
# 十进制
print(handle)
# 十六进制
print("%x" %(handle) )


# 搜索子窗口
# 枚举子窗口
hwndChildList = []
win32gui.EnumChildWindows(handle, lambda hwnd, param: param.append(hwnd), hwndChildList)

# FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None, lpszWindow=None) 父窗口句柄 若不为0，则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体，否则从第一个子窗体开始搜索。 子窗口类名 子窗口标题
subHandle = win32gui.FindWindowEx(handle, 0, "EDIT", None)

# 获得窗口的菜单句柄
menuHandle = win32gui.GetMenu(subHandle)
# 获得子菜单或下拉菜单句柄
# 参数：菜单句柄 子菜单索引号
subMenuHandle = win32gui.GetSubMenu(menuHandle, 0)
# 获得菜单项中的的标志符，注意，分隔符是被编入索引的
# 参数：子菜单句柄 项目索引号
menuItemHandle = win32gui.GetMenuItemID(subMenuHandle, 0)
# 发送消息，加入消息队列，无返回
# 参数：句柄 消息类型 WParam IParam
win32gui.postMessage(subHandle, win32con.WM_COMMAND, menuItemHandle, 0)

