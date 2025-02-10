import pytesseract
from PIL import Image
import json
import random
import time
import pyautogui
import mouse
import os
from PIL import ImageGrab


class Utils:

    def __init__(self):
        # Initialisation du chemin pour pytesseract si nécessaire
        pytesseract.pytesseract.tesseract_cmd = r'C:\D\tesseract\tesseract.exe'


    def incrementor(self):
        """
        Cette fonction incrémente une valeur stockée dans un fichier JSON.
        """
        file_name = "const.json"
        try:
            # Charger le fichier JSON
            with open(file_name, "r") as file:
                data = json.load(file)

            # Incrémenter la valeur
            value = data.get("value", 0) + 1
            data["value"] = value

            # Enregistrer la nouvelle valeur
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)

            return value

        except FileNotFoundError:
            # Si le fichier n'existe pas, le créer avec une valeur initiale
            data = {"value": 1}
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            return 1

  
    def takePictureAttack(self):
        """
        Prend une capture d'écran d'une certaine zone, analyse le texte
        et retourne True si le texte contient un chiffre
        supérieur à 1 000 000, sinon retourne False.
        et ensuite il baize ta mere bien comme il faut
        """
        # Définir le chemin pour sauvegarder l'image
        folder_path = "atk"
        image_name = "attack_screen.png"
        image_path = os.path.join(folder_path, image_name)

        # S'assurer que le dossier existe
        os.makedirs(folder_path, exist_ok=True)

        try:
            # Prendre une capture d'écran d'une zone spécifique
            screenshot = ImageGrab.grab(bbox=(90, 118, 250, 201))  # Ajustez les coordonnées ici
            screenshot.save(image_path)  # Sauvegarder l'image dans le dossier "atk"
            screenshot.close()
            print(f"Capture d'écran sauvegardée dans : {image_path}")

            # Charger l'image et extraire le texte
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)
            print(f"Texte trouvé : {text}")

            # Nettoyer et extraire les nombres
            cleaned_text = text.replace(",", "").replace(".", "").replace(" ", "")  # Retirer les séparateurs potentiels
            print(f"Texte nettoyé : {cleaned_text}")

            # Rechercher les nombres valides
            numbers = [int(num) for num in cleaned_text.split() if num.isdigit()]
            print(f"Nombres extraits : {numbers}")

            # Vérifier si un nombre dépasse 1 000 000
            if any(num > 900_000 for num in numbers):
                return True
            else:
                return False

        except Exception as e:
            print(f"Erreur lors de la capture ou de l'analyse de l'image : {e}")
            return False
        
        finally:
            # Supprimer l'image après analyse
            # self.deleteImage(image_path)
            pass
            
    


    def takePictureRempart(self):
        """
        Prend une photo et analyse le texte ou la couleur spécifique des
        remparts.
        """
        # Cette fonction dépendra des besoins exacts pour les remparts.
        pass

    def passAttack(self):
        """
        Appuie sur un bouton en cliquant sur des coordonnées spécifiques.
        """
        # Coordonnées du bouton "suivant" (adapter selon l'écran)
        x, y = 500, 500  # Remplacez par vos coordonnées
        pyautogui.click(x, y)

    def attack(self):
        """
        Réalise une série d'actions pour une attaque.
        """
        attacked = False
        self.dezoom()
        time.sleep(random.uniform(0.3, 0.9))

        x, y = self.generateRandomCoord(maxH=700, minH=610, maxW=170, minW=70)
        pyautogui.click(x, y)  # Clic sur le bouton "attaquer"

        time.sleep(random.uniform(0.1, 0.6))

        x, y = self.generateRandomCoord(maxH=500, minH=430, maxW=1000, minW=850)
        pyautogui.click(x, y)  # Clic sur le bouton "trouver une partie"


        while attacked is False:

            time.sleep(random.uniform(4.3, 5.9))

            self.takePictureAttack()

            time.sleep(random.uniform(1.3, 1.9))
            # Si le texte contient un nombre supérieur à 1 000 000
            # alors l'attaque a été
            # lancée avec succès
            if self.takePictureAttack():
                attacked = True
                self.dezoom()

                time.sleep(random.uniform(0.4, 0.6))
                print("Attaque trouvée !")

                self.dropTroop()

                time.sleep(random.uniform(190, 200))
                print("on rentre a la baraque")
                x, y = self.generateRandomCoord(maxH=650, minH=610, maxW=736, minW=589)
                pyautogui.click(x=x, y=y)  # Clic sur le bouton "attaquer"
            else:
                print("pas de ressources suffisantes pour attaquer")

                # Réessayer l'attaque
                x, y = self.generateRandomCoord(maxH=575, minH=500, maxW=1270, minW=1080)
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
                (130, 200, 650, 720),  # Troupe 1 (minW, maxW, minH, maxH)
                (225, 300, 650, 720),  # Troupe 2
                (340, 400, 650, 720),  # Troupe 3
                (440, 500, 650, 720),  # Troupe 4
                (540, 600, 650, 720),  # Troupe 5
                (630, 700, 650, 720),  # Troupe 6
                (740, 800, 650, 720),  # Troupe 7
                (830, 900, 650, 720),  # Troupe 8
                (930, 1000, 650, 720),  # Troupe 9
            ]

            # Limites pour la zone de dépôt par défaut (x, y)
            drop_bounds = (518, 555, 135, 140)  # (minW, maxW, minH, maxH)

            # Limites spéciales pour la zone de dépôt des 2 dernières catégories (x, y)
            special_drop_bounds = (420, 640, 400, 550)  # (minW, maxW, minH, maxH)

            # Parcourir toutes les catégories de troupes
            for troop_index, bounds in enumerate(troop_bounds):
                # Générer des coordonnées aléatoires pour la troupe
                troop_x, troop_y = self.generateRandomCoord(bounds[3], bounds[2], bounds[1], bounds[0])

                if troop_index >= 7:  # Utiliser les coordonnées spéciales pour les 2 dernières catégories


                    pyautogui.click(troop_x, troop_y)  # Cliquer sur la troupe
                    time.sleep(random.uniform(0.2, 0.3))  # Pause pour simuler un délai humain
                    for i in range(10):
                        drop_x, drop_y = self.generateRandomCoord(
                        special_drop_bounds[3], special_drop_bounds[2],
                        special_drop_bounds[1], special_drop_bounds[0]
                    )
                        time.sleep(random.uniform(0, 0.1))  # Pause pour simuler un délai humain=
                        pyautogui.click(drop_x, drop_y)  # Cliquer pour poser la troupe

                else:  # Utiliser les coordonnées par défaut pour les autres catégories

                    pyautogui.click(troop_x, troop_y)  # Cliquer sur la troupe
                    time.sleep(random.uniform(0.2, 0.3))  # Pause pour simuler un délai humain
                    for i in range(10):
                        drop_x, drop_y = self.generateRandomCoord(
                        drop_bounds[3], drop_bounds[2],
                        drop_bounds[1], drop_bounds[0]
                    )
                        time.sleep(random.uniform(0, 0.1))  # Pause pour simuler un délai humain=
                        pyautogui.click(drop_x, drop_y)  # Cliquer pour poser la troupe

                if troop_index >= 3 and troop_index <= 6:
                    pyautogui.click(troop_x, troop_y)  # actriver la capa sur la troupe
                time.sleep(random.uniform(0.5, 1.0))

            print("Toutes les troupes ont été posées avec succès.")

        except Exception as e:
            print(f"Erreur lors du dépôt des troupes : {e}")



    def upgradeRempart(self):
        """
        Améliore un rempart après avoir identifié sa couleur.
        """
        image_path = "rempart_screen.png"  # Spécifiez le chemin de l'image
        try:
            img = Image.open(image_path)
            # Analyser les couleurs ou du texte avec pytesseract
            # Exemple : Analyse des remparts
            text = pytesseract.image_to_string(img)
            print(f"Texte trouvé : {text}")

            # Simuler un clic sur la couleur trouvée
            x, y = 500, 500  # Coordonnées à ajuster
            pyautogui.click(x, y)
            print("Amélioration du rempart lancée.")

        except Exception as e:
            print(f"Erreur lors de l'amélioration du rempart : {e}")

    def formTroop(self):
        """
        Forme des troupes en appuyant sur la cabane et en naviguant dans le
        menu.
        """
        x, y = self.generateRandomCoord(maxH=450, minH=440, maxW=1040, minW=1030)
        pyautogui.click(x, y)  # Clic sur la cabane
        time.sleep(random.uniform(0.3, 0.5))

        x, y = self.generateRandomCoord(maxH=620, minH=540, maxW=850, minW=750)
        pyautogui.click(x, y)  # Clic sur l'onglet "former"
        time.sleep(random.uniform(0.3, 0.5))

        x, y = self.generateRandomCoord(maxH=100, minH=70, maxW=1100, minW=950)
        pyautogui.click(x, y)  # Clic sur "formation rapide"

        time.sleep(random.uniform(0.3, 0.5))
        x, y = self.generateRandomCoord(maxH=380, minH=350, maxW=1150, minW=1060)
        pyautogui.click(x, y)  # Clic sur "former"

        time.sleep(random.uniform(0.3, 0.5))
        x, y = self.generateRandomCoord(maxH=90, minH=70, maxW=1180, minW=1150)
        pyautogui.click(x, y)  # Clic sur "la croix rouge"
        time.sleep(random.uniform(0.3, 0.5))
        print("Troupes formées avec succès je declare pas mes impots MOUAHAHAHAHAHAHAAHHAHAHAHAHAHHAHAHAHAHAHAHAHAHAH.")

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
            # Maintenir la touche Ctrl pour dézoomer correctement

            pyautogui.click(45, 400)

            time.sleep(1)  # Pause avant de commencer le dézoom
            print("Maintien de la touche Ctrl...")
            pyautogui.keyDown('ctrl')
            time.sleep(1.5)  # Petite pause pour garantir que la touche Ctrl est bien enfoncée

            # Défilement pour dézoomer
            print("Défilement pour dézoomer...")
            pyautogui.scroll(-500)  # Scroll vers le bas pour dézoomer
            time.sleep(1.5)  # Attendre un peu avant de relâcher la touche Ctrl

            print("Relâchement de la touche Ctrl...")
            pyautogui.keyUp('ctrl')  # Relâcher la touche Ctrl

            # Vérification si le dézoom a eu lieu
            time.sleep(3)  # Pause pour voir si le dézoom a eu un effet

            # Drag and drop vers le bas
            start_x, start_y = 700, 150  # Point de départ
            end_x, end_y = 0, 700       # Point d'arrivée

            print("Début du drag-and-drop...")
            pyautogui.moveTo(start_x, start_y)  # Positionner la souris
            pyautogui.mouseDown()               # Maintenir le clic
            time.sleep(0.2)  # Attente avant de commencer le glisser
            pyautogui.dragTo(end_x, end_y, duration=0.5)  # Glisser
            pyautogui.mouseUp()                 # Relâcher le clic

            print("Opération de dézoom et drag-and-drop terminée.")

        except Exception as e:
            print(f"Erreur lors de l'exécution de la fonction dezoom : {e}")


    def deleteImage(self, image_path):
        """
        Supprime une image spécifiée par le chemin si elle existe.
        """
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Image supprimée : {image_path}")
            else:
                print(f"L'image n'existe pas : {image_path}")
        except Exception as e:
            print(f"Erreur lors de la suppression de l'image : {e}")
