import pyautogui
import time


pyautogui.hotkey('alt', 'tab')
time.sleep(1)

pyautogui.press('enter')

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_excel("dados.xlsx")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.hotkey('alt', 'a')
    # pegar da tabela o valor do campo que a gente quer preencher
    servico = tabela.loc[linha, "servico"]
    item = tabela.loc[linha, "item"]
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "servico"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "item"]))
    pyautogui.press("tab")
    pyautogui.click(x=1722, y=1017)
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')





