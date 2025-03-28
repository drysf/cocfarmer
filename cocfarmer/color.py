import pyautogui
import time

while True:
    x, y = pyautogui.position()  # Récupère la position de la souris
    try:
        rgb = pyautogui.pixel(x, y)  # Récupère la couleur du pixel sous la souris
        print(f"Position: ({x}, {y}) | RGB: {rgb}")
    except Exception as e:
        print(f"Erreur : {e}")

    time.sleep(0.1)  # Petite pause pour éviter une surcharge CPU
