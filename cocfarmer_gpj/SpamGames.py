import Utils
import pyautogui
import random
import time



def main():
    farmer = Utils.Utils()
    time.sleep(random.uniform(3.1, 3.3))
    for i in range(300): 

        if farmer.get_trophys() >= 4900:
            farmer.lose_trophys()
            
        else :
            farmer.attack()
            time.sleep(random.uniform(3, 4))







if __name__ == "__main__":
    main()