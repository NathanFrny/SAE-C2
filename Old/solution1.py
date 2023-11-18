import cv2
import numpy as np

def create_star_mask(image_path, output_path, threshold=200):
    # Charger l'image astronomique en niveaux de gris
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Impossible de charger l'image astronomique.")
        return

    # Appliquer un seuillage pour détecter les étoiles
    _, binary_mask = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    # Inverser le masque pour que les étoiles soient en blanc
    binary_mask = cv2.bitwise_not(binary_mask)

    # Enregistrer le masque des étoiles
    cv2.imwrite(output_path, binary_mask)

    print("Masque d'étoiles créé. Masque enregistré à", output_path)

def deconvolve_image_with_stars(image_path, mask_path, output_path, kernel_size=21, iterations=10):
    # Charger l'image astronomique
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    if image is None or mask is None:
        print("Impossible de charger les images.")
        return

    # Créer un noyau de déconvolution (vous pouvez ajuster la taille)
    kernel = cv2.getGaussianKernel(kernel_size, 0)
    kernel = kernel * kernel.T

    # Appliquer la déconvolution uniquement aux pixels masqués
    deconvolved_image = cv2.filter2D(image, -1, kernel)

    # Dupliquer le masque pour qu'il ait la même forme que l'image en couleur
    mask = np.tile(mask[:, :, np.newaxis], (1, 1, 3))

    # Appliquer le masque aux étoiles pour les conserver
    deconvolved_image = deconvolved_image * (1 - mask / 255) + image * (mask / 255)

    # Appliquer plusieurs itérations de la déconvolution pour améliorer la qualité
    for _ in range(iterations):
        deconvolved_image = cv2.filter2D(deconvolved_image, -1, kernel)
        deconvolved_image = deconvolved_image * (1 - mask / 255) + image * (mask / 255)

    # Enregistrer l'image résultante
    cv2.imwrite(output_path, deconvolved_image)

    print("Voile de pollution lumineuse réduit. Image enregistrée à", output_path)

if __name__ == "__main__":
    input_image_path = "images/barnard_stacked_gradient.png"
    output_mask_path = "star_mask.png"  # Nom du masque d'étoiles de sortie
    threshold_value = 200  # Ajustez ce seuil en fonction de votre image

    create_star_mask(input_image_path, output_mask_path, threshold_value)

    output_image_path = "image_sans_pollution_lumineuse.jpg"

    deconvolve_image_with_stars(input_image_path, output_mask_path, output_image_path)
