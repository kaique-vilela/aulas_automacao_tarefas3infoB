import pyautogui
import pyscreeze

#mover

#pyautogui.moveTo(1185, 1052, duration=.5)
#pyautogui.moveRel(100, 0, duration=.5)
#pyautogui.moveRel(0, 100, duration=.5)

#arrastar

#pyautogui.moveTo(45,45,duration=0.5)
#pyautogui.dragTo(200,220,duration=0.5)

#clicar

#pyautogui.click(45, 45, duration=.5,clicks=2,)

##Localizar um item na tela
btnXY = pyautogui.locateCenterOnScreen('./aula7/btn_edit.png')
pyautogui.click(btnXY,duration=0.5)

#rolar