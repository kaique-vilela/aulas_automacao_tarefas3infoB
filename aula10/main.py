import pyautogui
import time

campoAtleta = pyautogui.locateCenterOnScreen("aula10/atleta.png", grayscale=True, confidence=0.9)
pyautogui.click(campoAtleta,duration=0.3)
pyautogui.write("Tainá Lemes")
campoModalidade = pyautogui.locateCenterOnScreen("aula10/modalidade.png", grayscale=True, confidence=0.9)
pyautogui.click(campoModalidade,duration=0.3)
pyautogui.write("Corrida 100m")
campoMedalha = pyautogui.locateCenterOnScreen("aula10/medalha.png", grayscale=True, confidence=0.9)
pyautogui.click(campoMedalha,duration=0.3)
pyautogui.write("Prata")
campoComite = pyautogui.locateCenterOnScreen("aula10/comite.png", grayscale=True, confidence=0.9)
pyautogui.click(campoComite,duration=0.3)
pyautogui.write("Brasil")
btnEnviar = pyautogui.locateCenterOnScreen("aula10/enviar.png", grayscale=True, confidence=0.9)
pyautogui.click(btnEnviar)