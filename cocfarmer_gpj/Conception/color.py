import pyautogui
import time

while True:
    x, y = pyautogui.position()  
    try:
        rgb = pyautogui.pixel(x, y)  
        print(f"Position: ({x}, {y}) | RGB: {rgb}")
    except Exception as e:
        print(f"Erreur : {e}")

    time.sleep(0.1)  
