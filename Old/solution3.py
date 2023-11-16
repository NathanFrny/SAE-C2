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

def richardson_lucy_deconvolution(image, kernel, mask, iterations):
    deconvolved_image = np.copy(image)
    for _ in range(iterations):
        estimated_blur = cv2.filter2D(deconvolved_image, -1, kernel)
        relative_blur = image / (estimated_blur + 1e-6)
        deconvolved_image *= cv2.filter2D(relative_blur, -1, kernel)
        deconvolved_image = deconvolved_image * (1 - mask / 255) + image * (mask / 255)
    return deconvolved_image

if __name__ == "__main__":
    input_image_path = "images/barnard_stacked_gradient.png"
    output_mask_path = "star_mask3.png"
    threshold_value = 200

    create_star_mask(input_image_path, output_mask_path, threshold_value)

    output_image_path = "images2/solution3.png"

    image = cv2.imread(input_image_path)
    mask = cv2.imread(output_mask_path, cv2.IMREAD_GRAYSCALE)

    kernel_size = 21
    kernel = cv2.getGaussianKernel(kernel_size, 0)
    kernel = kernel * kernel.T

    iterations = 10

    deconvolved_image = richardson_lucy_deconvolution(image, kernel, mask, iterations)

    # Convertissez l'image résultante en valeurs entières pour l'enregistrement
    deconvolved_image = (deconvolved_image * 255).astype(np.uint8)

    cv2.imwrite(output_image_path, deconvolved_image)
    print("Voile de pollution lumineuse réduit. Image enregistrée à", output_image_path)
