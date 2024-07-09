import pyautogui, time

pyautogui.click(200,200, interval=0.5)
pyautogui.press('space')

while True:
    if pyautogui.pixelMatchesColor(250,410,[83,83,83],70):
        pyautogui.press('space')

    elif pyautogui.pixelMatchesColor(232,395,[83,83,83],70):
        pyautogui.press('down', interval=2)
                 