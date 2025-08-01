import Utils
import pyautogui
import random
import time
import json
import build


amount = build.rempart15["cost"]
rgb = build.rempart15["rgb"]



def main():
    farmer = Utils.Utils()
    time.sleep(random.uniform(3.1, 3.3))
    for i in range(300): 

        farmer.attack()
        time.sleep(random.uniform(3, 4))

        time.sleep(random.uniform(4, 5))
        farmer.dezoom()


        ressource = farmer.getAmountUpgrade(amount)
        if ressource:
            farmer.upgrade(rgb=rgb, ressource=ressource)
        else:
            print("Pas assez de ressources")

        time.sleep(random.uniform(3, 4))



if __name__ == "__main__":
    main()