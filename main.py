from PIL import ImageGrab
from SendKeys import SendKeys
import time
import win32gui
import pywinauto.controls.common_controls as controls
import winsound
from sys import argv

app, condition = argv
handle = win32gui.FindWindow("EsoClientWndClass", "Elder Scrolls Online") #get handle on game
targetarrayr = [] #empty list to store RGB color values
targetarrayg = []
targetarrayb = []
"""Fill the list with 110 Red Color values, make sure the pixel being
referenced matches the pixel being checked against in main loop"""
if condition == "Y":
    for i in xrange(110):
        targetarrayr.append(ImageGrab.grab().getpixel((1702, 1086))[0])
        #targetarrayg.append(ImageGrab.grab().getpixel((1702, 1086))[1])
        #targetarrayb.append(ImageGrab.grab().getpixel((1702, 1086))[2])
    """Grab the smallest red color value, this is the value
    to be checked against since the rod almost always
    has more red than the ground"""
    print "R " + str(min(targetarrayr)) + ' ' + str(max(targetarrayr))
    #print "G " + str(min(targetarrayg)) + ' ' + str(max(targetarrayg))
    #print "B " + str(min(targetarrayb)) + ' ' + str(max(targetarrayb))
    polled_value = input("Enter min R, G, or B value or something a bit smaller: ")
    pos = int(input("enter 0 -2 "))
else:
    polled_value = input("Enter min R value or something a bit smaller: ")
    pos = int(input("enter 0 -2 "))


"""Main loop, check target pixel and then compare it against polled_value
If window is not in the foreground, set it to foreground, mouseover and click in
the middle, then send a period to disengage mouse cursor mode before sending
the 'e' key to reel in. Finally, wait 2 and a half seconds."""
#time_start = time.time()
while 1:
    targetpixel =  ImageGrab.grab().getpixel((1702, 1086))
    time.sleep(.5)
    if targetpixel[pos] < int(polled_value):
        if win32gui.GetForegroundWindow() != handle:
            win32gui.SetForegroundWindow(handle)
            targetwin = controls.AnimationWrapper(handle)
            targetwin.ClickInput(button="left", coords=(1280, 720), 
                                double=False, 
                                wheel_dist=0, 
                                use_log=False, 
                                pressed="", 
                                absolute=False)
            SendKeys(".", pause= 1, turn_off_numlock= False)
        SendKeys("e",  pause= 1, turn_off_numlock= False)
        time.sleep(2.5)
    # Haven't got this bit working yet, want it to notify me if character
    # Is sitting around doing nothing.
    #if targetpixel[0] < int(polled_value) and time_start + 10:
        #while targetpixel[0] < int(polled_value):
            #winsound.MessageBeep()
            #if targetpixel[0] >= int(polled_value):
                #break
        #time_start = time.time()