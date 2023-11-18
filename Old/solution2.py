import cv2
import numpy as np

def generate_color_gradient(mask, image):
    # Trouver les coordonnées des pixels noirs dans le masque
    black_pixels = np.argwhere(mask == 0)

    # Initialiser le gradient avec une image noire
    gradient = np.zeros_like(image, dtype=np.uint8)

    # Remplir le gradient avec les couleurs de l'image d'origine aux coordonnées des pixels noirs dans le masque
    for coord in black_pixels:
        gradient[coord[0], coord[1]] = image[coord[0], coord[1]]

    return gradient

def remove_light_pollution(image, pollution_color, star_mask):
    # Créer un masque négatif pour le voile de pollution lumineuse
    pollution_mask = cv2.inRange(image, pollution_color, pollution_color)

    # Générer le gradient en couleur en utilisant le masque de pollution
    color_gradient = generate_color_gradient(pollution_mask, image)

    # Soustraire le gradient de l'image d'origine
    result_image = cv2.subtract(image, color_gradient)

    # Appliquer le masque des étoiles pour ne pas supprimer les étoiles
    result_image[star_mask > 0] = image[star_mask > 0]

    return result_image

# Charger l'image astronomique
image = cv2.imread('images/barnard_stacked_gradient.png')

# Définir la couleur du voile de pollution lumineuse (à ajuster)
pollution_color = (0, 255, 0)  # Exemple en vert, ajustez selon la couleur du voile

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer une opération de seuillage pour détecter les étoiles
_, star_mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

# Appliquer la fonction de suppression de pollution lumineuse
result_image = remove_light_pollution(image, pollution_color, star_mask)

# Sauvegarder l'image résultante
cv2.imwrite('result_image.jpg', result_image)
