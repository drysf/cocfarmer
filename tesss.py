import pyautogui
import time

def test_ctrl_scroll():
    print("Maintien de la touche Ctrl...")
    pyautogui.keyDown('ctrl')
    time.sleep(0.5)  # Attendre un peu pour simuler un dézoom
    print("Défilement pour dézoomer...")
    pyautogui.scroll(-500)  # Faire défiler vers le bas
    time.sleep(0.5)  # Attendre avant de relâcher Ctrl
    print("Relâchement de la touche Ctrl...")
    pyautogui.keyUp('ctrl')


time.sleep(5)
test_ctrl_scroll()
