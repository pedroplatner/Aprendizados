import pyautogui
import time

pyautogui.PAUSE = 0.2
pyautogui.press("win")
#ESCREVER GOOGLE
pyautogui.write("google")

#DAR UM ENTER
pyautogui.press("enter")
time.sleep(1)

#DAR UM CLICK NO PERFIL
pyautogui.click(x=990, y=609)
time.sleep(2)

#COLOCAR SENHA
pyautogui.write("1003")
time.sleep(2)
pyautogui.press("Enter")
time.sleep(2)

#POSICIONAR O MOUSE EM CIMA DO "ENTRAR"
entrar = pyautogui.locateCenterOnScreen('entrar.png')
pyautogui.click(entrar.x, entrar.y)
time.sleep(5)
img = pyautogui.locateCenterOnScreen('validador.png')
pyautogui.click(img.x, img.y)
time.sleep(5)

#POSICIONAR O MOUSE EM CIMA DO "TEMPO DE COLETA"
tempo = pyautogui.locateCenterOnScreen('tempo.png')
pyautogui.click(tempo.x, tempo.y)
time.sleep(5)

#DAR UM SCROLL NO MOUSE
pyautogui.scroll(-10000)

#POSICIONAR O MOUSE NO "VISUALIZAR"
pyautogui.click(x=1210, y=896)
time.sleep(15)

#POSICIONAR O MOUSE NO "SIM"
#sim = pyautogui.locateCenterOnScreen('sim.png')
pyautogui.click(x=1321, y=370)
time.sleep(6)
pyautogui.click(x=1321, y=370)
time.sleep(30)

#POSICIONAR O MOUSE NA SETINHA DE BAIXO DA "ULTIMA COLETA"
pyautogui.click(x=876, y=449)
time.sleep(30)

#TIRAR PRINT
pyautogui.click(x=481, y=242)
time.sleep(2)
pyautogui.press("printscreen")

pyautogui.drag(1300,800,3)
time.sleep(1)
pyautogui.click(x=1654, y=1052)
time.sleep(1)
pyautogui.click(x=334, y=416)
time.sleep(1)

#FECHAR GOOGLE
pyautogui.click(x=1895, y=18)