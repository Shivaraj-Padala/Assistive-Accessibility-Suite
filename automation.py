from time import sleep
import pyautogui
from word2number import w2n

UNWANTED_CHARS = '?.!:;}{]['
COORDINATES = {}

def gridController(showGrid = False):
    if pyautogui.getActiveWindow().title == 'Assistive Accessibility Suite' or showGrid == True:
        gridPos = pyautogui.locateCenterOnScreen('static/assets/grid.png', confidence=0.8)
        pyautogui.click(gridPos)

def typeWrite(txtData):
    try:
        pyautogui.typewrite(txtData[1:len(txtData)], interval=0.10)
        return True
    except:
        return False
    
def cursorMover(command):
    subCommand = command.replace('move cursor to', '').replace('click on', '')
    gridController()
    sleep(0.5)
    try:
        pyautogui.moveTo(COORDINATES[subCommand[1:len(subCommand)]], duration=0.5)
    except KeyError:
        subCommand = subCommand.split()
        pyautogui.moveTo(COORDINATES[f'{subCommand[0]} {w2n.word_to_num(subCommand[1])}'], duration=0.5)
    except:
        return False
    return True

def commandManager(command):
    command = command.lower()
    command = command.strip(UNWANTED_CHARS)
    commandStatus = False
    if 'type text' in command:
        commandStatus = typeWrite(command.replace('type text', ''))
    elif 'show number grid' in command or 'hide number grid' in command:
        gridController(showGrid = True)
        commandStatus = True
    elif 'move cursor to' in command:
        commandStatus = cursorMover(command)
    elif 'click on' in command:
        commandStatus = cursorMover(command)
        if commandStatus == True:
            sleep(0.5)
            pyautogui.click()
    elif 'double click' in command:
        pyautogui.doubleClick()
        commandStatus = True
    elif 'tripple click' in command:
        pyautogui.tripleClick()
        commandStatus = True
    elif 'right click' in command:
        pyautogui.click(button='right')
        commandStatus = True
    elif 'left click' in command:
        pyautogui.click(button='left')
        commandStatus = True
    elif 'press down arrow' in command or 'press up arrow' in command or 'press left arrow' in command or 'press right arrow' in command:
        subcommand = command.split()
        clickTimes = 0
        if len(subcommand) == 3:
            pyautogui.press(subcommand[1])
        else:
            try:
                clickTimes = w2n.word_to_num(subcommand[3])
                for i in range(clickTimes):
                    pyautogui.press(subcommand[1])
                commandStatus = True
            except:
                commandStatus = False
    elif 'move cursor left' in command or 'move cursor right' in command or 'move cursor up' in command or 'move cursor down' in command:
        xpos, ypos = pyautogui.position()
        subcommand = command.split()
        if subcommand[2] == 'left':
            pyautogui.moveTo(xpos-20, ypos)
        elif subcommand[2] == 'right':
            pyautogui.moveTo(xpos+20, ypos)
        elif subcommand[2] == 'up':
            pyautogui.moveTo(xpos, ypos-20)
        elif subcommand[2] == 'down':
            pyautogui.moveTo(xpos, ypos+20)
        commandStatus = True
    elif 'scroll up' in command:
        pyautogui.press('pgup')
        commandStatus = True
    elif 'scroll down' in command:
        pyautogui.press('pgdn')
        commandStatus = True
    elif 'minimize window' in command:
        activeWindow = pyautogui.getActiveWindow()
        pyautogui.Window.minimize(activeWindow)
        commandStatus = True
    elif 'maximize window' in command:
        activeWindow = pyautogui.getActiveWindow()
        pyautogui.Window.maximize(activeWindow)
        commandStatus = True
    elif 'close window' in command:
        activeWindow = pyautogui.getActiveWindow()
        pyautogui.Window.close(activeWindow)
        commandStatus = True

    #! dynamic restoration of windows pending

    return commandStatus

#print(commandManager('press left arrow'))