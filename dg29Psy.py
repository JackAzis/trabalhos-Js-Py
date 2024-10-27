import threading
import time
import tkinter as tk
import pyautogui

pyautogui.FAILSAFE = True
# variavel global para controlar o loop
parar_loop = False
vezes = [2000]

def pilar():
    # click janela
    pyautogui.click(1133, 14)    
    time.sleep(0.5)
    
    # target pilar
    pyautogui.click(947, 321)
    time.sleep(0.5)
    pyautogui.click(947, 321)
    time.sleep(3)
    # missão
    pyautogui.click(1070, 398)
    time.sleep(0.5)
    # aceita
    pyautogui.click(1085, 376) 
    time.sleep(0.5)
    # sim
    pyautogui.click(1085, 376)
    time.sleep(1)
    # buff
    pyautogui.press('esc')
    pyautogui.press('f3')

def primeiroRush():
    pyautogui.click(1890, 102)
    time.sleep(11)
    pyautogui.press('tab')
    pyautogui.press('f5') 
    time.sleep(1)

def salaoRedondo():
    pyautogui.click(1858, 108)
    time.sleep(5)
    pyautogui.press('f5') 
    time.sleep(1)

def torre1():
    pyautogui.click(1839, 96)
    time.sleep(8) 
    pyautogui.press('tab')
    pyautogui.press('f5') 
    time.sleep(1)
    pyautogui.press('f5') 
    time.sleep(1)

def torre2():
    pyautogui.click(1867, 120)
    time.sleep(4)
    pyautogui.press('f5') 
    time.sleep(1)
    pyautogui.press('f5') 
    time.sleep(1)

def torre3():
    pyautogui.click(1845, 118)
    time.sleep(5)
    pyautogui.press('f5') 
    time.sleep(1)
    pyautogui.press('f1')
    time.sleep(1)
    pyautogui.press('f5') 
    time.sleep(1)
    pyautogui.press('f5') 
    time.sleep(1)

def corredor():
    pyautogui.click(1817, 166)
    time.sleep(18)
    pyautogui.press('f5') 
    time.sleep(1)

def corredor2():
    pyautogui.click(1852, 98)
    time.sleep(5)
    pyautogui.press('f5') 
    time.sleep(1)

def boss():
    pyautogui.click(1859, 112)
    time.sleep(8)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('f5')
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.press('f5')
    time.sleep(8)
    pyautogui.press('f5')

    pyautogui.press('f1')

def reset():
    pyautogui.click(1323, 248)
    time.sleep(1)
    # aceita pergaminho
    pyautogui.click(1270, 484)
    time.sleep(4)

def executar_loop():
    global parar_loop
    for vez in vezes:
        for _ in range(vez):
            # Verifica se o loop foi interrompido
            if parar_loop:
                print("Loop interrompido!")
                return

            pilar()
            # 1rush
            primeiroRush()
            # salao redondo
            salaoRedondo()
            # salao torre 1
            torre1()
            # salao torre 2
            torre2()
            # salao torre 3
            torre3()
            # corredor
            corredor()
            # corredor 2
            corredor2()
            # boss
            boss()
            # pergaminho
            reset()

# Função chamada pelo botão Iniciar
def iniciar():
    global parar_loop
    parar_loop = False
    # inicia o loop em uma nova thread
    thread = threading.Thread(target=executar_loop)
    thread.start()

# função chamada pelo botão Parar
def parar():
    global parar_loop
    pyautogui.FailSafeException = True

# interface gráfica
root = tk.Tk()
root.title("Controle de Loop")

btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar)
btn_iniciar.pack(pady=10)

btn_parar = tk.Button(root, text="Parar", command=parar)
btn_parar.pack(pady=10)

root.mainloop()
