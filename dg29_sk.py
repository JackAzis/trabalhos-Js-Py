import pyautogui
import time 


pyautogui.FAILSAFE = True
#pyautogui.PAUSE = 5
repeticoes = [2000]

def target_pilar():
    # Clica no pilar e vai até ele
    pyautogui.click(693, 335)
    time.sleep(1)
    pyautogui.click(693, 335)
    time.sleep(4)

def pegar_missao():
    # Pega missão (reconhecimento por foto)
    pyautogui.click(r"C:/Program Files/Macro/missao.png")
    time.sleep(1)
    # Aceita e completa quest
    pyautogui.click(873, 418) 
    time.sleep(1)
    pyautogui.click(873, 418)
    time.sleep(1)    

def salao_boss():
    # Entra na sala do boss
    pyautogui.click(1614, 139)
    time.sleep(8)
    # Borrão
    pyautogui.press('7')
    time.sleep(1)
    # Procura target
    pyautogui.press('tab')
    # Ataca em área
    pyautogui.press('8')
    time.sleep(5)
    # Procura target
    pyautogui.press('tab')
    # Ataca boss
    pyautogui.press('2')
    time.sleep(5)
    pyautogui.press('2')
    time.sleep(60)
    # Pega os itens no chão
    pyautogui.press('1')

def reset_dg():
    pyautogui.click(1082, 293)
    time.sleep(2)
    # aceita pergaminho
    pyautogui.click(1036, 519)
    time.sleep(5)

def script():
    for repeticao in repeticoes:
        for _ in range(repeticao):
            #selecionar tela
            pyautogui.click(993, 55)
            time.sleep(1)

            #buffs
            pyautogui.press('9')
            time.sleep(5)

            #pilar pega quest
            target_pilar()

            #pegando a missão
            pegar_missao()

            #primeiro rush
            pyautogui.click(1649, 143)
            time.sleep(14)
            pyautogui.press('f1')

            #rush salão redondo
            pyautogui.click(1619, 145)
            time.sleep(5)

            #rush sala torre 1
            pyautogui.click(1600, 135)
            time.sleep(9) 
            #borrao
            pyautogui.press('7') 
            time.sleep(1)
            #rush sala torre 2
            pyautogui.click(1626, 160)
            time.sleep(4)
            #rush sala torre 3
            pyautogui.click(1605, 157)
            time.sleep(5)
            pyautogui.press('4')
            time.sleep(0.5)
            pyautogui.press('f1')
            time.sleep(2)
            pyautogui.press('1')
            time.sleep(1)

            #rush corredor 1
            pyautogui.click(1578, 206)
            time.sleep(20)

            #rush corredor 2
            pyautogui.click(1612, 151)
            time.sleep(5)

            salao_boss()

            reset_dg()
                

if __name__=='__main__':
    script()