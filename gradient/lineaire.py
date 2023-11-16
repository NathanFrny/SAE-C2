import cv2
import numpy as np

# Charger l'image
image_path = 'gradient/barnard_stacked_gradient.png'  # Mettez le chemin de votre image ici
image = cv2.imread(image_path)

# Calculer l'image en nuances de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sélectionner les points sans étoiles sur les bords médians de l'image
top_point = (image.shape[0] // 2, 0)  # Milieu haut
bottom_point = (image.shape[0] // 2, image.shape[1] - 1)  # Milieu bas
left_point = (0, image.shape[1] // 2)  # Milieu gauche
right_point = (image.shape[0] - 1, image.shape[1] // 2)  # Milieu droit

selected_points = [top_point, bottom_point, left_point, right_point]

# Ajuster un modèle de gradient linéaire avec ces points
gradient_linear_model = np.polyfit([p[1] for p in selected_points], [p[0] for p in selected_points], 1)

# Créer un gradient linéaire basé sur le modèle ajusté
linear_gradient = np.zeros_like(gray_image)
for x in range(gray_image.shape[1]):
    linear_gradient[:, x] = gradient_linear_model[0] * x + gradient_linear_model[1]

# Créer une version en couleur de l'image de gradient linéaire
color_linear_gradient = cv2.cvtColor(linear_gradient.astype(np.uint8), cv2.COLOR_GRAY2BGR)

# Soustraire le gradient linéaire de l'image originale canal par canal
processed_image = cv2.subtract(image, color_linear_gradient)

# Afficher l'image originale et l'image traitée
cv2.imwrite('Processed_Image.png', color_linear_gradient)
cv2.destroyAllWindows()
