import pyautogui
from time import sleep
sleep(3)
activeWindow = pyautogui.getActiveWindow()
pyautogui.Window.close(activeWindow)

'''winTitles = pyautogui.getAllTitles()
pyautogui.getWindowsWithTitle('Python pyautogui window handle - Stack Overflow - Brave')[0].restore()
print(winTitles)


sleep(3)
def shortcut(cmd):
    finalcmd = cmd.replace('press', '').split()
    if len(finalcmd)>2:
        key1 = finalcmd[0]
        key2 = finalcmd[1]
        key3 = finalcmd[2]
    else:
        key1 = finalcmd[0]
        key2 = finalcmd[1]
        key3 = ''
    #print(finalcmd)
    #pyautogui.hotkey(key1, key2, key3)
    #print(key1, key2, key3)'''