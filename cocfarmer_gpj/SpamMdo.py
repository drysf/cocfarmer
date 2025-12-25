import Utils as Utils
import pyautogui
import random
import time
import json


def main():
    farmer = Utils.Utils()
    time.sleep(random.uniform(3.1, 3.3))


    farmer.dezoom_bottom()

    farmer.switch_mdo()
    time.sleep(random.uniform(3, 3.2))


    for i in range(100):
        time.sleep(random.uniform(4, 4.5))
        farmer.attack_mdo()

        time.sleep(random.uniform(120, 124))

        farmer.dezoom_mdo()
        time.sleep(random.uniform(3, 3.2))


        time.sleep(random.uniform(1.9, 2.5)) 

        farmer.dropTroop_mdo()

        if farmer.check_and_click_pixel_mdo():
            x, y = farmer.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
            pyautogui.click(x=x, y=y)  



if __name__ == "__main__":
    main()
