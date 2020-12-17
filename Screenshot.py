import pyautogui
import time

x=1
while x<4:                                                             #numero de prints da tela           
    pyautogui.screenshot('/Users/Mezzo/Desktop/image'+str(x)+'.png')    #diretorio para salvar print
    x+=1
    time.sleep(2)
