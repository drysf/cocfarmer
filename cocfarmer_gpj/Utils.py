from PIL import Image
import json
import random
import time
import pyautogui
import mouse
import os
from PIL import Image, ImageGrab, ImageEnhance, ImageFilter, ImageOps
import easyocr

import conf 




class Utils:

    def __init__(self):
        self.reader = easyocr.Reader(['en'])

  


    def takePictureAttack(self):
        """
        Prend une capture d'écran d'une certaine zone, analyse le texte
        et retourne True si le texte contient un chiffre
        supérieur à 1 000 000, sinon retourne False.
        """
        folder_path = "cocfarmer_gpj/atk"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        elixir_image_name = "elixir_attack_screen.png"
        elixir_image_path = os.path.join(folder_path, elixir_image_name)

        gold_image_name = "gold_attack_screen.png"
        gold_image_path = os.path.join(folder_path, gold_image_name)

        try:
            # ELIXIR
            screenshot = ImageGrab.grab(bbox=(60, 120, 160, 145)) 
            screenshot.save(elixir_image_path)
            screenshot.close()
            result = self.reader.readtext(elixir_image_path)

            elixir = "0"
            for (bbox, text, prob) in result:
                elixir = text.replace(" ", "").replace(",", "").replace(".", "")  # Supprimer espaces et séparateurs
                print(elixir)

            # GOLD
            screenshot = ImageGrab.grab(bbox=(60, 85, 160, 110))  # Ajustez les coordonnées ici
            screenshot.save(gold_image_path)
            screenshot.close()
            result = self.reader.readtext(gold_image_path)

            gold = "0"
            for (bbox, text, prob) in result:
                gold = text.replace(" ", "").replace(",", "").replace(".", "")  # Même traitement
                print(gold)

            # Conversion en int
            elixir = int(elixir) if elixir.isdigit() else 0
            gold = int(gold) if gold.isdigit() else 0

            numbers = elixir + gold
            print("total",numbers)

            if conf.seuil_attaque < numbers < 5_000_000:
                return True
            else:
                return False

        except Exception as e:
            print(f"Erreur lors de la capture ou de l'analyse de l'image : {e}")
            return False


    def check_and_click_pixel(self):
        """
        Vérifie si le pixel aux coordonnées (x, y) correspond à target_rgb.
        Si oui, clique dessus et retourne True. Répète toutes les 5 secondes.
        """
        try:
            while True:
                x = 678
                y = 679
                target_rgb = (112, 187, 29)

                target2 = (108, 187, 31)
                current_color = pyautogui.pixel(x, y)
                
                if current_color == target_rgb or current_color == target2:
                    return True
                
                print(f"Pixel ({x}, {y}) couleur actuelle {current_color}, attente...")
                time.sleep(5)
        except KeyboardInterrupt:
            print("Interruption de la fonction.")
            return False
            

    def attack(self):
        """
        Réalise une série d'actions pour une attaque.
        """
        attacked = False
        time.sleep(random.uniform(1.3, 1.9))

        x, y = self.generateRandomCoord(maxH=700, minH=690, maxW=110, minW=90)
        pyautogui.click(x, y)  # Clic sur le bouton "attaquer"
        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=550, minH=500, maxW=200, minW=100)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"

        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=660, minH=650, maxW=1200, minW=1050)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"


        while attacked is False:

            time.sleep(random.uniform(4.3, 5.9))


            if self.takePictureAttack():
                attacked = True
                self.dezoom()

                time.sleep(random.uniform(0.4, 0.6))
                print("Attaque trouvée !")

                self.dropTroop()
                if self.check_and_click_pixel():
                    x, y = self.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
                    pyautogui.click(x=x, y=y)  
            else:
                print("pas de ressources suffisantes pour attaquer")

                # Réessayer l'attaque
                x, y = self.generateRandomCoord(maxH=575, minH=550, maxW=1270, minW=1200)
                time.sleep(random.uniform(0.4, 0.6))
                pyautogui.click(x=x, y=y)  # Clic sur le bouton "suivant"
                continue

    def dropTroop(self):
        """
        Effectue un drag-and-drop pour les 2 premières catégories de troupes,
        puis un clic pour les autres catégories de troupes avec des coordonnées aléatoires.
        Les 2 dernières catégories utilisent des coordonnées spécifiques pour la zone de dépôt.
        """
        try:
            troop_bounds = [
                (210, 250, 670, 740),  # Troupe 1 (minW, maxW, minH, maxH)
                (290, 340, 670, 740),  # Troupe 2
                (390, 440, 670, 740),  # Troupe 3
                (490, 500, 670, 740),  # Troupe 4
                (590, 630, 670, 740),  # Troupe 5
                (690, 710, 670, 740),  # Troupe 6
                (750, 790, 670, 740),  # Troupe 7
                (840, 890, 670, 740),  # Troupe 8
                (930, 980, 670, 740),  # Troupe 9
                (1020, 1070, 670, 740),  # Troupe 10
            ]

            # Limites pour la zone de dépôt par défaut (x, y)
            drop_bounds = (528, 555, 135, 140)  # (minW, maxW, minH, maxH)

            # Parcourir toutes les catégories de troupes
            for troop_index, bounds in enumerate(troop_bounds):
                # Générer des coordonnées aléatoires pour la troupe
                troop_x, troop_y = self.generateRandomCoord(bounds[3], bounds[2], bounds[1], bounds[0])


                pyautogui.click(troop_x, troop_y)  # Cliquer sur la troupe
                time.sleep(random.uniform(0.2, 0.3))  # Pause pour simuler un délai humain
                for i in range(16):
                    drop_x, drop_y = self.generateRandomCoord(
                    drop_bounds[3], drop_bounds[2],
                    drop_bounds[1], drop_bounds[0]
                )
                    time.sleep(random.uniform(0, 0.1))  # Pause pour simuler un délai humain=
                    pyautogui.click(drop_x, drop_y)  # Cliquer pour poser la troupe

                if troop_index >= 5 and troop_index <= 8:
                    pyautogui.click(troop_x, troop_y)  # actriver la capa sur la troupe
                time.sleep(random.uniform(0.5, 1.0))

            print("Toutes les troupes ont été posées avec succès.")

        except Exception as e:
            print(f"Erreur lors du dépôt des troupes : {e}")




    def generateRandomCoord(self, maxH, minH, maxW, minW):
        """
        Génère des coordonnées aléatoires.
        """
        x = random.randint(minW, maxW)
        y = random.randint(minH, maxH)
        return x, y


    def dezoom(self):
        """
        Dézoome pour avoir une vue complète du village, puis effectue un drag and drop vers le bas.
        """
        try:
            pyautogui.click(13, 345)
            time.sleep(1)  
            pyautogui.keyDown('ctrl')
            time.sleep(1.5) 
            pyautogui.scroll(-1300)  
            pyautogui.keyUp('ctrl')  
            time.sleep(3)  

            start_x, start_y = 700, 150  
            end_x, end_y = 0, 700       

            pyautogui.moveTo(start_x, start_y)  
            pyautogui.mouseDown()             
            time.sleep(0.2)  
            pyautogui.dragTo(end_x, end_y, duration=0.5)  
            pyautogui.mouseUp()                 
        except Exception as e:
            print(f"Erreur lors de l'exécution de la fonction dezoom : {e}")


        
    def getAmountUpgrade(self, amount):
        """
        Prend une capture d'écran d'une certaine zone, analyse le texte
        et retourne "elixir" ou "gold" si le montant est supérieur au paramètre.
        Sinon retourne False.
        """
        folder_path = "cocfarmer_gpj/build"
        image_elixir = "elixir_amount_screen.png"
        image_path_elixir = os.path.join(folder_path, image_elixir)

        image_gold = "gold_amount_screen.png"
        image_path_gold = os.path.join(folder_path, image_gold)

        os.makedirs(folder_path, exist_ok=True)  # S'assurer que le dossier existe

        try:
            # Capture Elixir
            screenshot_elixir = ImageGrab.grab(bbox=(1170, 83, 1300, 109))
            screenshot_elixir.save(image_path_elixir)
            screenshot_elixir.close()

            # Prétraitement de l'image
            img = image_path_elixir
            elixir = self.reader.readtext('cocfarmer_gpj/build/elixir_amount_screen.png')
            for (bbox, text, prob) in elixir:
                elixir = text.replace(" ", "").replace(",", "").replace(".", "")  # Même traitement


            # Capture Gold
            screenshot_gold = ImageGrab.grab(bbox=(1170, 21, 1300, 50))
            screenshot_gold.save(image_path_gold)
            screenshot_gold.close()

            # Prétraitement de l'image
            img = image_path_gold
            gold = self.reader.readtext('cocfarmer_gpj/build/gold_amount_screen.png')
            for (bbox, text, prob) in gold:
                gold = text.replace(" ", "").replace(",", "").replace(".", "")  # Même traitement

            elixir = int(elixir) if elixir.isdigit() else 0
            gold = int(gold) if gold.isdigit() else 0
            
            # Comparaison avec amount
            if elixir > conf.seuil_upgrade_rempart and elixir < 35_000_000:
                return "elixir"
            if gold > conf.seuil_upgrade_rempart and gold < 35_000_000:
                return "gold"
            return False

        except Exception as e:
            print(f"Erreur lors de la capture ou de l'analyse de l'image : {e}")
            return False




    def upgrade(self, ressource, rgb):
        """
        Cherche un pixel de la couleur donnée dans une zone spécifique et clique dessus.

        :param ressource: Type de ressource ("elixir" ou "gold").
        :param rgb: Tuple (R, G, B) représentant la couleur à rechercher.
        :return: True si un clic a été effectué, False sinon.
        """
        print("Recherche de la couleur...")

        x_start, y_start, width, height = 468, 93, 913, 419  

        screenshot = pyautogui.screenshot(region=(x_start, y_start, width, height))  # Capture uniquement la zone définie
        time.sleep(random.uniform(0.5, 1.0))

        for x in range(width):
            for y in range(height):
                if self.couleur_proche(screenshot.getpixel((x, y)), rgb, tolerance=1):  
                    abs_x, abs_y = x_start + x, y_start + y  # Convertit en coordonnées globales
                    print(f"Clic détecté en ({abs_x}, {abs_y}) pour la couleur {rgb}")
                    
                    pyautogui.click(abs_x, abs_y)
                    time.sleep(random.uniform(2.5, 3.0))

                    return self.process_upgrade(ressource)  # Exécuter l'amélioration et arrêter la recherche

        print("Aucun pixel trouvé avec cette couleur.")
        return False  # Aucun pixel trouvé

    def couleur_proche(self, couleur1, couleur2, tolerance=1):
        """
        Vérifie si deux couleurs sont proches en tenant compte d'une tolérance.
        Une tolérance faible (ex: 5) signifie que les couleurs doivent être presque identiques.
        """
        return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(couleur1, couleur2))

    def process_upgrade(self, ressource):
        """
        Exécute la procédure d'amélioration en fonction de la ressource.
        """
        if ressource == "elixir":
            print("Amélioration avec l'élixir lancée.")
            x, y = self.generateRandomCoord(maxH=610, minH=580, maxW=860, minW=810)
        elif ressource == "gold":
            print("Amélioration avec l'or lancée.")
            x, y = self.generateRandomCoord(maxH=610, minH=580, maxW=760, minW=700)
        else:
            print("La ressource n'est pas valide")
            return False

        time.sleep(random.uniform(1.5, 2.0))
        pyautogui.click(x, y)  # Clic sur "améliorer"

        time.sleep(random.uniform(1.5, 2.0))
        print("Amélioration en cours...")

        x, y = self.generateRandomCoord(maxH=670, minH=640, maxW=970, minW=900)
        time.sleep(random.uniform(1.5, 2.0))
        pyautogui.click(x, y)  # Clic sur "confirmer"

        print("Amélioration terminée.")
        return True

    def get_trophys(self):
        """
        Prend une capture d'écran d'une certaine zone, analyse le texte
        et retourne le nombre de trophées.
        """
        folder_path = "cocfarmer_gpj/trophies"
        image_name = "trophies_screen.png"
        image_path = os.path.join(folder_path, image_name)

        os.makedirs(folder_path, exist_ok=True)
        # Vérifier si le dossier existe, sinon le créer
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        try:
            # Capture d'écran de la zone des trophées
            screenshot = ImageGrab.grab(bbox=(82, 96, 145, 119))  # Ajustez les coordonnées ici
            screenshot.save(image_path)
            screenshot.close()

            # Analyse de l'image avec easyocr
            result = self.reader.readtext(image_path)

            trophies = "0"
            for (bbox, text, prob) in result:
                trophies = text.replace(" ", "").replace(",", "").replace(".", "")  # Supprimer espaces et séparateurs
                print(trophies)

            # Conversion en int
            trophies = int(trophies) if trophies.isdigit() else 0

            return trophies

        except Exception as e:
            print(f"Erreur lors de la capture ou de l'analyse de l'image : {e}")
            return 0
        
    def lose_trophys(self):
        """
        fais une attaque et pose une troupe puis appuie sur capituler et rentrer pour perdre des trophées
        """
        attacked = False
        time.sleep(random.uniform(4.3, 4.9))

        x, y = self.generateRandomCoord(maxH=700, minH=680, maxW=110, minW=90)
        pyautogui.click(x, y)
        time.sleep(random.uniform(4.1, 4.6))
        x, y = self.generateRandomCoord(maxH=470, minH=430, maxW=1000, minW=900)
        pyautogui.click(x, y)
        time.sleep(random.uniform(7.1, 8.6))
        x, y = self.generateRandomCoord(maxH=700, minH=680, maxW=240, minW=210)
        pyautogui.click(x, y)
        self.dezoom()
        time.sleep(random.uniform(4.1, 4.6))
        x, y = self.generateRandomCoord(maxH=110, minH=101, maxW=563, minW=562)
        pyautogui.click(x, y)
        time.sleep(random.uniform(4.1, 4.6))
        x, y = self.generateRandomCoord(maxH=620, minH=600, maxW=110, minW=90)
        pyautogui.click(x, y)
        time.sleep(random.uniform(4.1, 4.6))
        x, y = self.generateRandomCoord(maxH=500, minH=450, maxW=800, minW=750)
        pyautogui.click(x, y)
        time.sleep(random.uniform(4.1, 4.6))
        if self.check_and_click_pixel():
            x, y = self.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
            pyautogui.click(x=x, y=y)  



    def spam(self):
        """
        Réalise une série d'actions pour une attaque.
        """
        attacked = False
        time.sleep(random.uniform(0.3, 0.9))

        x, y = self.generateRandomCoord(maxH=700, minH=680, maxW=110, minW=90)
        pyautogui.click(x, y)  # Clic sur le bouton "attaquer"
        time.sleep(random.uniform(0.1, 0.6))
        x, y = self.generateRandomCoord(maxH=470, minH=430, maxW=1000, minW=900)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"


        while attacked is False:

            time.sleep(random.uniform(4.3, 5.9))


            if self.takePictureAttack():
                attacked = True
                self.dezoom()

                time.sleep(random.uniform(0.4, 0.6))
                print("Attaque trouvée !")

                self.dropTroop()
                if self.check_and_click_pixel():
                    x, y = self.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
                    pyautogui.click(x=x, y=y)  
            else:
                print("pas de ressources suffisantes pour attaquer")

                # Réessayer l'attaque
                x, y = self.generateRandomCoord(maxH=575, minH=550, maxW=1270, minW=1200)
                time.sleep(random.uniform(0.4, 0.6))
                pyautogui.click(x=x, y=y)  # Clic sur le bouton "suivant"
                continue


    def attack_spam(self):
        """
        Réalise une série d'actions pour une attaque.
        """
        time.sleep(random.uniform(0.3, 0.9))

        x, y = self.generateRandomCoord(maxH=700, minH=690, maxW=110, minW=90)
        pyautogui.click(x, y)  # Clic sur le bouton "attaquer"
        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=550, minH=500, maxW=200, minW=100)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"

        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=660, minH=650, maxW=1200, minW=1050)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"

        time.sleep(random.uniform(4.3, 5.9))


        self.dezoom()

        time.sleep(random.uniform(2.4, 2.6))
        print("Attaque trouvée !")

        self.dropTroop()
        if self.check_and_click_pixel():
            x, y = self.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
            pyautogui.click(x=x, y=y)  

    def attack_ranked(self):
        """
        Réalise une série d'actions pour une attaque en classé.
        """
        time.sleep(random.uniform(0.3, 0.9))

        x, y = self.generateRandomCoord(maxH=700, minH=690, maxW=110, minW=90)
        pyautogui.click(x, y)  # Clic sur le bouton "attaquer"
        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=550, minH=500, maxW=600, minW=450)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"


        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=660, minH=650, maxW=1200, minW=1050)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"


        x, y = self.generateRandomCoord(maxH=500, minH=460, maxW=800, minW=750)
        pyautogui.click(x, y)  # Clic sur le bouton "Confirmer attaquer"


        time.sleep(random.uniform(4.3, 5.9))


        self.dezoom()

        time.sleep(random.uniform(2.4, 2.6))
        print("Attaque trouvée !")

        self.dropTroop()
        if self.check_and_click_pixel():
            x, y = self.generateRandomCoord(maxH=650, minH=630, maxW=736, minW=620)
            pyautogui.click(x=x, y=y)  

    def dezoom_bottom(self):
        """
        Dézoome pour avoir une vue complète du village, puis effectue un drag and drop vers le bas.
        """
        try:
            pyautogui.click(13, 345)
            time.sleep(1)  
            pyautogui.keyDown('ctrl')
            time.sleep(1.5) 
            pyautogui.scroll(-500)  
            pyautogui.keyUp('ctrl')  
            time.sleep(3)  

            start_x, start_y = 0, 700  
            end_x, end_y = 700, 150       

            pyautogui.moveTo(start_x, start_y)  
            pyautogui.mouseDown()             
            time.sleep(0.2)  
            pyautogui.dragTo(end_x, end_y, duration=0.5)  
            pyautogui.mouseUp()                 
        except Exception as e:
            print(f"Erreur lors de l'exécution de la fonction dezoom : {e}")


    def switch_mdo(self):
        x, y = self.generateRandomCoord(maxH=535, minH=515, maxW=390, minW=350)
        pyautogui.click(x, y)  # Clic sur le bateau


    def attack_mdo(self):
        """
        Réalise une série d'actions pour une attaque en mdo.
        """
        time.sleep(random.uniform(0.3, 0.9))

        x, y = self.generateRandomCoord(maxH=700, minH=690, maxW=110, minW=90)
        pyautogui.click(x, y)  # Clic sur le bouton "attaquer"
        time.sleep(random.uniform(1.1, 1.6))
        x, y = self.generateRandomCoord(maxH=530, minH=470, maxW=1100, minW=900)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"


        time.sleep(random.uniform(4.3, 5.9))

        self.dezoom()
        time.sleep(random.uniform(2.4, 2.6))
        self.dropTroop_mdo()


    def dropTroop_mdo(self):

        pyautogui.keyDown('ctrl')
        time.sleep(1.5) 
        for i in range(5):
            pyautogui.scroll(-500)  
            time.sleep(0.5)
        pyautogui.keyUp('ctrl')  

        time.sleep(random.uniform(1.9, 2.5)) 
        try:
            troop_bounds = [
                (210, 250, 670, 740),  # Troupe 1 (minW, maxW, minH, maxH)
                (300, 340, 670, 740),  # Troupe 2
                (390, 440, 670, 740),  # Troupe 3
                (490, 540, 670, 740),  # Troupe 4
                (590, 630, 670, 740),  # Troupe 5
                (690, 710, 670, 740),  # Troupe 6
                (750, 790, 670, 740),  # Troupe 7
                (840, 890, 670, 740),  # Troupe 8
                (930, 980, 670, 740),  # Troupe 9
            ]

            # Limites pour la zone de dépôt par défaut (x, y)
            drop_bounds = (630, 640, 215, 230)  # (minW, maxW, minH, maxH)


            # Parcourir toutes les catégories de troupes
            for troop_index, bounds in enumerate(troop_bounds):
                # Générer des coordonnées aléatoires pour la troupe
                troop_x, troop_y = self.generateRandomCoord(bounds[3], bounds[2], bounds[1], bounds[0])


                pyautogui.click(troop_x, troop_y)  # Cliquer sur la troupe
                time.sleep(random.uniform(0.2, 0.3))  # Pause pour simuler un délai humain
                for i in range(2):
                    drop_x, drop_y = self.generateRandomCoord(drop_bounds[3], drop_bounds[2],drop_bounds[1], drop_bounds[0])
                    time.sleep(random.uniform(0, 0.1))
                    pyautogui.click(drop_x, drop_y)  # Cliquer pour poser la troupe

                pyautogui.click(troop_x, troop_y) 


        except Exception as e:
            print(f"Erreur lors du dépôt des troupes : {e}")

    def check_and_click_pixel_mdo(self):
        """
        Vérifie si le pixel aux coordonnées (x, y) correspond à target_rgb.
        Si oui, clique dessus et retourne True. Répète toutes les 5 secondes.
        """
        try:
            while True:
                x = 682
                y = 662
                target_rgb = (136, 212, 54)
                current_color = pyautogui.pixel(x, y)
                
                if current_color == target_rgb:
                    return True
                
                print(f"Pixel ({x}, {y}) couleur actuelle {current_color}, attente...")
                time.sleep(5)
        except KeyboardInterrupt:
            print("Interruption de la fonction.")
            return False
        
    def check_and_click_pixel_mdo_second_attack(self):
        """
        Vérifie si le pixel aux coordonnées (x, y) correspond à target_rgb.
        Si oui, clique dessus et retourne True. Répète toutes les 5 secondes.
        """
        try:
            while True:
                x = 880
                y = 663
                target_rgb = (198, 73, 255)
                current_color = pyautogui.pixel(x, y)
                
                if current_color == target_rgb:
                    return True
                
                print(f"Pixel ({x}, {y}) couleur actuelle {current_color}, attente...")
                time.sleep(5)
        except KeyboardInterrupt:
            print("Interruption de la fonction.")
            return False
        

    def dezoom_mdo(self):
        """
        Dézoome pour avoir une vue complète du village, puis effectue un drag and drop vers le bas.
        """
        try:

            for i in range(5):
                pyautogui.scroll(-1300)  

            start_x, start_y = 700, 150  
            end_x, end_y = 0, 700       

            pyautogui.moveTo(start_x, start_y)  
            pyautogui.mouseDown()             
            pyautogui.dragTo(end_x, end_y, duration=0.5)  
            pyautogui.mouseUp()                 
        except Exception as e:
            print(f"Erreur lors de l'exécution de la fonction dezoom : {e}")

    def get_elixir_mdo(self):

        pass



    def dezoom_bottom_mdo_elixir_process(self):
        """
        Dézoome pour avoir une vue complète du village, puis effectue un drag and drop vers le bas.
        """
        try:
            pyautogui.click(13, 345)
            time.sleep(1)  
            pyautogui.keyDown('ctrl')
            time.sleep(1.5) 
            pyautogui.scroll(-500)  
            pyautogui.keyUp('ctrl')  
            time.sleep(3)  

            start_x, start_y = 800, 800  
            end_x, end_y = 10, 10       

            pyautogui.moveTo(start_x, start_y)  
            time.sleep(0.2)  
            pyautogui.mouseDown()             
            time.sleep(0.2)  
            pyautogui.dragTo(end_x, end_y, duration=0.5)  
            time.sleep(0.2)  
            pyautogui.mouseUp()    


            start_x, start_y = 10, 10  
            end_x, end_y = 10, 800       


            pyautogui.moveTo(start_x, start_y)  
            time.sleep(0.2)  
            pyautogui.mouseDown()             
            time.sleep(0.2)  
            pyautogui.dragTo(end_x, end_y, duration=0.5)  
            time.sleep(0.2)  
            pyautogui.mouseUp()       

            
                 
        except Exception as e:
            print(f"Erreur lors de l'exécution de la fonction dezoom : {e}")
