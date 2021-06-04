import pyautogui
import time
while True:

    time.sleep(3)

    # walk to mission camp
    pyautogui.keyDown('s')
    time.sleep(500/1000)
    pyautogui.keyUp('s')
    time.sleep(1)
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')
    time.sleep(1)
    pyautogui.keyDown('d')
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('d')
    pyautogui.keyUp('w')
    time.sleep(750/1000)
    pyautogui.keyDown('a')
    pyautogui.keyDown('w')
    time.sleep(200/1000)
    pyautogui.keyUp('w')
    pyautogui.keyUp('a')

    # join mission
    time.sleep(200/1000)
    pyautogui.click(x=964, y=553)
    time.sleep(1500/1000)
    pyautogui.click(x=873, y=550, clicks=2, interval=0.25)
    time.sleep(7)
    pyautogui.click(x=1430, y=660, clicks=4, interval=1)
    time.sleep(40)

    # go to safe location
    pyautogui.keyDown('s')    
    time.sleep(150)
    pyautogui.keyUp('s')

    # exit mission
    pyautogui.press('f3')
    time.sleep(500/1000)
    pyautogui.click(x=1553, y=794, clicks=4, interval=0.25)