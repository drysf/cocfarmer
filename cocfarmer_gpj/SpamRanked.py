import Utils
import pyautogui
import random
import time
import json


def main():
    farmer = Utils.Utils()
    time.sleep(random.uniform(3.1, 3.3))
    while True: 

        farmer.attack_ranked()
        time.sleep(random.uniform(3, 4))



if __name__ == "__main__":
    main()
