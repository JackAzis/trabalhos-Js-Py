import pandas as pd

import pyautogui
import time

tabela = pd.read_csv('produtos.csv')
'''Abertura do excel'''
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write ('excel')
pyautogui.press('enter')

'''Criação de nova tabela'''
time.sleep(3)
pyautogui.hotkey('ctrl','n')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')

'''Inserção dos danos da tabela'''
for linha in tabela.index:
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha,'obs']))
    
    pyautogui.press('enter')

