import Utils as Utils
import pyautogui
import random
import time
import json


def main():
    farmer = Utils.Utils()
    time.sleep(random.uniform(3.1, 3.3))
    farmer.dezoom_bottom()

if __name__ == "__main__":
    main()
