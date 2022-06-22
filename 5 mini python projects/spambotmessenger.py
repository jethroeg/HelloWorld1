import pyautogui, time
time.sleep(3)
x = ["spam"]
while True:
    for i in x:
        time.sleep(1)
        pyautogui.write(i)
        pyautogui.press("enter")
        
