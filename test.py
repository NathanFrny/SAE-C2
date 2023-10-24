import cv2
import numpy as np

# Charger l'image en niveaux de gris
image = cv2.imread('images/barnard_stacked_gradient.png', cv2.IMREAD_GRAYSCALE)
# Charger l'image en niveaux de gris
image_couleur = cv2.imread('images/barnard_stacked_gradient.png', cv2.IMREAD_COLOR)

# Vérifier si l'image a été correctement chargée
if image is None:
    print("Impossible de charger l'image.")
else:
    hauteur, largeur, _ = image_couleur.shape  # Utilisez l'image en couleur
    hauteur_gris, largeur_gris = image.shape

    left_x = None
    right_x = None

    # Trouver le point sans étoile à gauche
    ###TODO - Faire en sorte de récupérer les pixels de l'image de couleur tout en gardant les conditions des images en gris
    for x in range(largeur // 4):
        for y in range(hauteur):
            if any(image[y, x] <= 128):
                left_x = x
                break
        if left_x is not None:
            break

    # Trouver le point sans étoile à droite
    for x in range(largeur - 1, largeur - 10 - 1, -1):
        for y in range(hauteur):
            if any(image[y, x] <= 128):
                right_x = x
                break
        if right_x is not None:
            break

    if left_x is not None and right_x is not None:
        # Générer un gradient linéaire horizontal de gauche à droite
        gradient_lineaire = np.zeros((hauteur, largeur), dtype=np.uint8)

        for x in range(largeur):
            for y in range(hauteur):
                # Utilisez la pente pour générer le gradient horizontal
                gradient_lineaire[y, x] = int(255 * (x - left_x) / (right_x - left_x))

        # Afficher l'image du gradient linéaire
        cv2.imshow('Gradient Linéaire', gradient_lineaire)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imwrite('images/gradient_de_lenfer.jpg', gradient_lineaire)
    else:
        print("Aucun pixel sans étoile trouvé.")
