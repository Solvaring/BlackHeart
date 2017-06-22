import pywinauto.controls.common_controls as controls
import win32gui

handle = win32gui.FindWindow("EsoClientWndClass", "Elder Scrolls Online")

targetwindow = controls.AnimationWrapper(handle)

targetwindow.MoveMouseInput(coords=(1299, 880))