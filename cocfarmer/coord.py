import pyautogui


while True: 
    #afficher les coordonnées de la souris
    print(pyautogui.position())

    #afficher la couleur du pixel sous la souris
    # print(pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1]))