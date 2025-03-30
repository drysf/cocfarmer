import Utils
import pyautogui
import random
import time
import json
import build


amount = build.rempart16["cost"]
rgb = build.rempart16["rgb"]



def main():
    farmer = Utils.Utils()
    time.sleep(random.uniform(3.1, 3.3))
    for i in range(300): 

        farmer.attack()
        time.sleep(random.uniform(3, 4))
        farmer.dezoom()


        ressource = farmer.getAmountUpgrade(amount)
        if ressource:
            farmer.upgrade(rgb=rgb, ressource=ressource)
        else:
            print("Pas assez de ressources")

        time.sleep(random.uniform(3, 4))



if __name__ == "__main__":
    main()