""""import cv2
import numpy as np






# Load the color image
image_color = cv2.imread('images/unknown (1).png')

# Load the grayscale image
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# Check if the images were loaded successfully
if image_gray is None or image_color is None:
    print("Failed to load one or more images.")
else:
    num_columns_to_check = 1
    threshold_value = 128

    depolluted_image, gradient_linear = remove_light_pollution(image_color, image_gray, num_columns_to_check, threshold_value)

    cv2.imwrite('Processed_Image.png', depolluted_image)
    cv2.imwrite('Gradient_Linear.png', gradient_linear)
"""