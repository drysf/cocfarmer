import Utils

import random
import time

farmer = Utils.Utils()
farmer.incrementor()


time.sleep(random.uniform(2.1, 2.3))
for i in range(1): 
    
    time.sleep(5)
    # farmer.dezoom()
    # farmer.dropTroop()
    farmer.attack()
    time.sleep(random.uniform(0.1, 0.3))
    

