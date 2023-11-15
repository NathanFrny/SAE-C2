import cv2
import numpy as np

# Charger l'image astronomique
image_astronomique = cv2.imread('images/barnard_stacked_gradient.png', cv2.IMREAD_GRAYSCALE)

# Appliquer la détection de Sobel pour calculer le gradient
gradient_x = cv2.Sobel(image_astronomique, cv2.CV_64F, 1, 0, ksize=5)
gradient_y = cv2.Sobel(image_astronomique, cv2.CV_64F, 0, 1, ksize=5)

# Calculer la magnitude du gradient
magnitude_gradient = np.sqrt(gradient_x**2 + gradient_y**2)

# Afficher l'image résultante du gradient (pour vérification)
cv2.imshow('Gradient Image', magnitude_gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()