import pyautogui
import time
from datetime import datetime, timedelta

def execute_code_if_program_open(RS1):
    if pyautogui.getWindowsWithTitle(RS1):
        print(f"O programa {RS1} está aberto. Executando código para quando o programa está aberto.")
        pyautogui.click(x=123, y=1064)
    else:
        print(f"O programa {RS1} está fechado. Executando código para quando o programa está fechado.")
        # Insira aqui o código que você deseja executar quando o programa estiver fechado
        pyautogui.press("win")
        pyautogui.write("RS1")
        pyautogui.press("enter")
        time.sleep(10)
        
# Chamada da função para executar o código apropriado
execute_code_if_program_open("RS1")

dia_anterior = datetime.now() - timedelta(days=1)
dia_anterior_formatado = dia_anterior.strftime("%d/%m/%Y")

mes_atual = datetime.now().strftime("%m")
ano_atual = datetime.now().strftime("%Y")

# Criar a data para o primeiro dia do mês atual
primeiro_dia_mes = f"01/{mes_atual}/{ano_atual}"


#UTILIZAÇÃO DE EQUIPAMENTO POR PERIODO
time.sleep(5)
pyautogui.press('F3')
time.sleep(2)
pyautogui.write('utiliza')
time.sleep(5)
pyautogui.click(x=705, y=535)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=76, y=108)
time.sleep(2)
pyautogui.press('Del')
time.sleep(2)
pyautogui.write(primeiro_dia_mes)
time.sleep(3)
pyautogui.click(x=213, y=110) #clica na data
time.sleep(5)
pyautogui.press('del')
time.sleep(1)
pyautogui.write(dia_anterior_formatado)
time.sleep(2)
pyautogui.click(x=1730, y=1023)
time.sleep(30)
pyautogui.click(x=200, y=37)
time.sleep(10)

#VOLTAR PRO RS
pyautogui.click(x=130, y=1051)
time.sleep(5)
pyautogui.click(x=612, y=359)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.press('delete')
time.sleep(3)

#KM PERDIDA DETALHADA
pyautogui.write('km perdida')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(x=51, y=110)
time.sleep(3)
pyautogui.press('del')
time.sleep(1)
pyautogui.write(primeiro_dia_mes)
time.sleep(5)
pyautogui.click(x=48, y=188)
pyautogui.press('del')
time.sleep(1)
pyautogui.write(primeiro_dia_mes)
time.sleep(5)
pyautogui.click(x=199, y=109) #clica na data
time.sleep(3)
pyautogui.press('del')
time.sleep(1)
pyautogui.write(dia_anterior_formatado)
time.sleep(2)
pyautogui.click(x=194, y=186) #clica na data
time.sleep(3)
pyautogui.press('del')
time.sleep(1)
pyautogui.write(dia_anterior_formatado)
time.sleep(2)
pyautogui.click(x=1723, y=1022)
time.sleep(60)
pyautogui.click(x=200, y=35)
time.sleep(10)

#VOLTAR PRO RS
pyautogui.click(x=130, y=1051)
time.sleep(5)
pyautogui.click(x=612, y=359)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.press('delete')
time.sleep(3)

#CONSUMO DE ITENS POR EQUIPAMENTO
pyautogui.write('consumo dos itens')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=209, y=107) #clica na data
time.sleep(2)
pyautogui.press('del')
time.sleep(0.5)
pyautogui.write(dia_anterior_formatado)
time.sleep(2)
pyautogui.click(x=1721, y=1022)


