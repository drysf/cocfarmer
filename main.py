import Utils
import pyautogui
import random
import time
import json
import build


amount = build.rempart14["cost"]
rgb = build.rempart14["rgb"]



def main():
    time.sleep(5)
    farmer = Utils.Utils()

    farmer.incrementor()
    time.sleep(random.uniform(2.1, 2.3))
    for i in range(100): 
        farmer.attack()
        time.sleep(random.uniform(3, 4))
        farmer.dezoom()
        farmer.formTroop()

        time.sleep(random.uniform(3, 4))

        ressource = farmer.getAmountUpgrade(amount)

        if ressource:
            print(ressource)
            print(rgb)
            farmer.upgrade(rgb=rgb, ressource=ressource)
        else:
            print("Pas assez de ressources")

        for minute in range(4):
            time.sleep(random.uniform(340, 355))
            print("5 minutes : ", minute)
            x, y = farmer.generateRandomCoord(minH=130, maxH=180, minW=900, maxW=950)
            pyautogui.click(x, y)

# print(rgb)
# rgb = (42, 46, 63)

# def main():
#     farmer = Utils.Utils()
#     print(farmer.upgrade(rgb=rgb, ressource="elixir"))

    

if __name__ == "__main__":
    main()