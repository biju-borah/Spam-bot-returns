import time,pyautogui
time.sleep(10)
f = open('name.txt','r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')