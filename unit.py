import cv2
import pytesseract

# Spécifie le chemin de tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\D\tesseract\tesseract.exe'

# Charger l'image
img = cv2.imread('C:/Users/drysf/Bureau/cocfarmer/build/elixir_amount_screen.png')

# Vérifier si l'image est correctement chargée
if img is None:
    print("Erreur : Impossible de charger l'image.")
    exit()

# 1. Redimensionner l'image pour augmenter la résolution
img_resized = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# 2. Convertir en niveaux de gris
gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

# Afficher l'image en niveaux de gris
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)

# 3. Augmenter le contraste avec l'égalisation de l'histogramme
gray = cv2.equalizeHist(gray)

# Afficher l'image après égalisation
cv2.imshow("Equalized Image", gray)
cv2.waitKey(0)

# 4. Appliquer un seuillage adaptatif pour binariser l'image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY, 11, 2)

# Afficher l'image binarisée
cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)

# 5. Appliquer un filtre de flou pour réduire le bruit
thresh = cv2.GaussianBlur(thresh, (5, 5), 0)

# Afficher l'image après flou
cv2.imshow("Blurred Image", thresh)
cv2.waitKey(0)

# 6. Utiliser pytesseract pour extraire uniquement les chiffres
custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

# Extraire le texte
text = pytesseract.image_to_string(thresh, config=custom_config)

# Afficher le texte extrait
print("Texte extrait :")
print(text)

# Fermer les fenêtres d'image
cv2.destroyAllWindows()
