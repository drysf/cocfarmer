import Utils
import pyautogui
import random
import time



def main():
    farmer = Utils.Utils()

    farmer.incrementor()
    time.sleep(random.uniform(2.1, 2.3))
    for i in range(15): 
        time.sleep(5)
        farmer.attack()
        time.sleep(random.uniform(3, 4))
        farmer.dezoom()
        farmer.formTroop()
        time.sleep(random.uniform(0.1, 0.3))
        for minute in range(9):
            time.sleep(random.uniform(310, 315))
            print("Minute: ", minute)
            x, y = farmer.generateRandomCoord(minH=130, maxH=180, minW=900, maxW=950)
            pyautogui.click(x, y)

    



if __name__ == "__main__":
    main()