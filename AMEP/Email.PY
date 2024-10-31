import pyautogui
import time
import os
import pyperclip
import tkinter as tk
from tkinter import simpledialog

def obter_nome_arquivo():
    root = tk.Tk()
    root.withdraw() 
    nome_arquivo = simpledialog.askstring("Entrada", "Digite o nome do documento PDF:")
    root.destroy()
    return nome_arquivo

# Solicita o nome do arquivo PDF
nome_arquivo_pdf = obter_nome_arquivo()

# Define o caminho completo do arquivo PDF
diretorio = r'Diretório que o PDF está'
caminho_completo = os.path.join(diretorio, f"{nome_arquivo_pdf}.pdf")


if not os.path.exists(caminho_completo):
    print(f"Arquivo {caminho_completo} não encontrado.")
    exit()

# Abre o Outlook
os.startfile(r"C:\Program Files\Microsoft Office 15\root\office15\OUTLOOK.EXE")
time.sleep(10)

# Cria um novo email
pyautogui.click(x=20, y=87)
time.sleep(2)

# Preenche os campos do email
pyautogui.write("EMAILS")
time.sleep(2)
pyautogui.press('tab')
pyautogui.write("Email cópia")
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
pyautogui.write("NOME DO ARQUIVO")
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)

# Mensagem do email
mensagem = """
mensagem para os destinatários"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# Clica no botão para anexar o arquivo
pyautogui.click(x=629, y=94)
time.sleep(2)

# Cola o caminho completo do arquivo PDF e anexa
pyperclip.copy(caminho_completo)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
