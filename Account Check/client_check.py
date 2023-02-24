import pyautogui
from time import sleep

sleep(2)
cont = 0
contas = open("./combo.txt", "r").readlines()

for linha in contas:
    conta = linha.strip().split(":")
    cont += 1
    
    pyautogui.typewrite(conta[0])
    pyautogui.press('tab')
    pyautogui.typewrite(conta[1])
    pyautogui.press('enter')
    print(f"Conta: {conta[0]}/{conta[1]} na linha {cont}.")
    sleep(3)
    pyautogui.press('enter')