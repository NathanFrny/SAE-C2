import cv2
import numpy as np

def remove_light_pollution(image_color, image_gray, num_columns, threshold):
    height, width, _ = image_color.shape

    # Find the point without stars on the left side of the grayscale image
    for x in range(num_columns):
        for y in range(height):
            if np.any(image_gray[y, x] <= threshold):
                left_x = x
                break
        if left_x is not None:
            break

    # Find the point without stars on the right side of the grayscale image
    for x in range(width - 1, width - num_columns - 1, -1):
        for y in range(height):
            if np.any(image_gray[y, x] <= threshold):
                right_x = x
                break
        if right_x is not None:
            break

    if left_x is not None and right_x is not None:
        # Get the colors of the left and right pixels in the color image
        color_pixel_left = image_color[0, left_x]
        color_pixel_right = image_color[0, right_x]

        # Generate a horizontal linear gradient between the colors of the left and right pixels
        gradient_linear = np.zeros((height, width, 3), dtype=np.uint8)

        for x in range(width):
            for y in range(height):
                ratio = (x - left_x) / (right_x - left_x)
                interpolated_color = (1 - ratio) * color_pixel_left + ratio * color_pixel_right
                gradient_linear[y, x] = interpolated_color

        # Subtract the linear gradient from the color image
        image_depolluted = cv2.subtract(image_color, gradient_linear)

        return image_depolluted
    else:
        print("No point without stars found.")
        return image_color  # Return the original image

# Load the grayscale image
image_gray = cv2.imread('images/niveau_de_gris.jpg', cv2.IMREAD_GRAYSCALE)

# Load the color image
image_color = cv2.imread('images/barnard_stacked_gradient.png')

# Check if the images were loaded successfully
if image_gray is None or image_color is None:
    print("Failed to load one or more images.")
else:
    num_columns_to_check = 1
    threshold_value = 10

    depolluted_image = remove_light_pollution(image_color, image_gray, num_columns_to_check, threshold_value)

    # Display the depolluted image
    cv2.imshow('Depolluted Image', depolluted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('images/depolluted_image.jpg', depolluted_image)
