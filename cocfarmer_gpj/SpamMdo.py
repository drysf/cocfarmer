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


    farmer.dezoom_bottom_mdo_elixir_process()



    for i in range(500):
        farmer.dezoom_bottom()

        time.sleep(random.uniform(4, 4.5))
        farmer.attack_mdo()

        while True:
            if farmer.couleur_proche(pyautogui.pixel(682, 662), (119, 186, 47), tolerance=10):
                x, y = farmer.generateRandomCoord(maxH=672, minH=652, maxW=692, minW=672)
                pyautogui.click(x, y)
                break
            if farmer.couleur_proche(pyautogui.pixel(880, 663), (174, 61, 224), tolerance=10):
                x, y = farmer.generateRandomCoord(maxH=673, minH=653, maxW=890, minW=870)
                pyautogui.click(x, y)
                break
            time.sleep(1)

        farmer.dezoom_mdo()
        time.sleep(random.uniform(3, 3.2))


        time.sleep(random.uniform(1.9, 2.5)) 

        farmer.dropTroop_mdo()

        if farmer.check_and_click_pixel_mdo():
            x, y = farmer.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
            pyautogui.click(x=x, y=y)  

        farmer.get_elixir_mdo()
        time.sleep(random.uniform(3, 3.2))



if __name__ == "__main__":
    main()
