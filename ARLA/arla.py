import pyautogui
import time
from datetime import datetime, timedelta
import pandas as pd

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

# Chamada da função para executar o código apropriado
execute_code_if_program_open("RS1")

dia_anterior = datetime.now() - timedelta(days=1)
dia_anterior_formatado = dia_anterior.strftime("%d/%m/%Y")

#ABRIR FONTE DE INSUMO
pyautogui.click(x=82, y=97)
pyautogui.click(x=82, y=97)
pyautogui.click(x=51, y=228)
time.sleep(2)
pyautogui.click(x=355, y=292)
time.sleep(1)
pyautogui.press('enter')
time.sleep(8)

tabela = pd.read_excel("dados.xlsx")

#LANÇAR O ARLA
pyautogui.write(dia_anterior_formatado)
pyautogui.press('tab')
pyautogui.write(dia_anterior_formatado)
time.sleep(3)
pyautogui.press('tab')
time.sleep(3)
pyautogui.write('6')
pyautogui.press('enter')
time.sleep(3)
for linha in tabela.index:
    carro = tabela.loc[linha, "carro"]
    hora = tabela.loc[linha, "hora"]
    litro = tabela.loc[linha, "litro"]
    # preencher oS campoS
    pyautogui.write(str(tabela.loc[linha, "carro"]))
    time.sleep(3)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "hora"]))
    time.sleep(3)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "litro"]))
    time.sleep(3)
    pyautogui.press('+')

