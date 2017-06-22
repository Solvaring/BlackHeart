from PIL import ImageGrab
import time
import win32api, win32con

def grabcolor(x, y):
    a = ImageGrab.grab().getpixel(x, y)
    return a

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP)
    
while 1:
    targetpixel = ImageGrab.grab().getpixel((1280, 717))
    if targetpixel[2] < 20:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(.5)      
# 195, 16, 22