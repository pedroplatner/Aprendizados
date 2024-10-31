import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import os
from datetime import datetime, timedelta

data_atual = datetime.now()
data_formatada = data_atual.strftime("%d-%m-%y %H:%M")
dia_anterior = datetime.now() - timedelta(days=1)
dia_anterior_formatado = dia_anterior.strftime("%d/%m/%Y")

def execute_code_if_program_open(RS1):
    if pyautogui.getWindowsWithTitle(RS1):
        print(f"O programa {RS1} está aberto. Executando código para quando o programa está aberto.")
        pyautogui.click(x=123, y=1064)
    else:
        print(f"O programa {RS1} está fechado. Executando código para quando o programa está fechado.")
        pyautogui.press("win")
        pyautogui.write("RS1")
        pyautogui.press("enter")
        time.sleep(10)

    time.sleep(5)

    # ABRIR O ITEM
    img = pyautogui.locateCenterOnScreen('Ponto.png')
    if img:
        pyautogui.click(img.x, img.y)
        pyautogui.press("enter")
        time.sleep(10)

    # Filtrar batidas noite pt1
    pyautogui.hotkey('CTRL', 'g')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(dia_anterior_formatado)
    time.sleep(1)
    pyautogui.press("space")  
    time.sleep(1)
    pyautogui.write("170000")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write(dia_anterior_formatado)
    time.sleep(1)
    pyautogui.press("space")  
    time.sleep(1)
    pyautogui.write("200000")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(3)

    #POSICIONAR BATIDAS
    pyautogui.click(x=537, y=105)
    time.sleep(1)
    pyautogui.press("home")
    time.sleep(5)

    # Posicionar o mouse
    pyautogui.moveTo(5, 98)

    # Tirar print
    pyautogui.press("printscreen")
    time.sleep(2)
    pyautogui.drag(700, 910, 3)
    time.sleep(3)
    pyautogui.click(x=615, y=1004)
    time.sleep(5)

    # Abrir email
    os.startfile(r"C:\Program Files\Microsoft Office 15\root\office15\OUTLOOK.EXE")
    time.sleep(10)
    pyautogui.click(x=20, y=106)
    time.sleep(5)
    pyautogui.write("EMAIL QUE SERA ENVIADO")
    pyautogui.press('TAB')
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(5)
    pyautogui.write("CARTAO PONTO ")
    time.sleep(2)
    pyautogui.write(data_formatada)
    time.sleep(2)
    pyautogui.press("TAB")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    barra = pyautogui.locateCenterOnScreen('Barra.png') 
    pyautogui.click(barra.x, barra.y)
    

    # Filtrar batidas noite pt2
    pyautogui.click(x=648, y=255)
    time.sleep(2)
    pyautogui.press("end")
    time.sleep(5)
    pyautogui.moveTo(5, 626)
    time.sleep(1)
    pyautogui.press("printscreen")
    time.sleep(2)
    pyautogui.drag(700, 400, 3)
    time.sleep(3)
    pyautogui.click(x=614, y=1039)
    time.sleep(5)
    pyautogui.hotkey("alt", "tab")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(3)
    pyautogui.click(barra.x, barra.y)
    time.sleep(2)

    #FILTRAR BATIDAS DO DIA
    pyautogui.click(x=648, y=255)
    time.sleep(2)
    pyautogui.press("F9")
    time.sleep(3)
    pyautogui.write("HH")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=537, y=105)
    time.sleep(1)
    pyautogui.press("end")
    time.sleep(3)
    pyautogui.moveTo(15, 626)
    time.sleep(3)
    pyautogui.press("printscreen")
    time.sleep(2)
    pyautogui.drag(700, 400, 3)
    time.sleep(1)
    pyautogui.click(x=622, y=1037)
    time.sleep(2)
    pyautogui.hotkey("alt", "tab")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)

    #ENVIAR O EMAIL
    pyautogui.click(x=37, y=201) 
    time.sleep(10)
    pyautogui.click(x=1904, y=10) 
    
def ask_permission():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    if messagebox.askokcancel("Permissão para Executar Código", "Você permite executar o código?"):
        execute_code_if_program_open("RS1")
    else:
        print("Execução do código cancelada pelo usuário.")

# Chamada da função para solicitar permissão
ask_permission()