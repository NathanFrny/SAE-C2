import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

class app_gradient_12_points():
    def __init__(self) -> None:
        self.image = None
    def remove_light_pollution(image_color, image_gray, num_columns, threshold):
        height, width, _ = image_color.shape

        def find_left_point(x_range, y_range):
            for x in x_range:
                for y in y_range:
                    if np.any(image_gray[y, x] <= threshold):
                        return x
            return None

        def find_right_point(x_range, y_range):
            for x in x_range[::-1]:
                for y in y_range:
                    if np.any(image_gray[y, x] <= threshold):
                        return x
            return None

        left_x1 = find_left_point(range(num_columns), range(height))
        right_x1 = find_right_point(range(width - num_columns), range(height))
        one_third_x1 = width // 3
        two_thirds_x1 = 2 * (width // 3)

        left_x2 = find_left_point(range(one_third_x1 - 1, one_third_x1 + 2), range(height))
        right_x2 = find_right_point(range(width - num_columns), range(height))
        one_third_x2 = one_third_x1
        two_thirds_x2 = two_thirds_x1

        left_x3 = find_left_point(range(one_third_x2 - 1, one_third_x2 + 2), range(height))
        right_x3 = find_right_point(range(width - num_columns), range(height))
        one_third_x3 = one_third_x2
        two_thirds_x3 = two_thirds_x2

        left_x4 = find_left_point(range(one_third_x3 - 1, one_third_x3 + 2), range(height))
        right_x4 = find_right_point(range(width - num_columns), range(height))
        one_third_x4 = one_third_x3
        two_thirds_x4 = two_thirds_x3

        if (left_x1 is not None and right_x1 is not None and
            left_x2 is not None and right_x2 is not None and
            left_x3 is not None and right_x3 is not None and
            left_x4 is not None and right_x4 is not None):
            # Get the colors of the left, 1/3, 2/3, and right pixels in the color image
            color_pixel_left1 = image_color[0, left_x1]
            color_pixel_one_third1 = image_color[0, one_third_x1]
            color_pixel_two_thirds1 = image_color[0, two_thirds_x1]
            color_pixel_right1 = image_color[0, right_x1]

            color_pixel_left2 = image_color[0, left_x2]
            color_pixel_one_third2 = image_color[0, one_third_x2]
            color_pixel_two_thirds2 = image_color[0, two_thirds_x2]
            color_pixel_right2 = image_color[0, right_x2]

            color_pixel_left3 = image_color[0, left_x3]
            color_pixel_one_third3 = image_color[0, one_third_x3]
            color_pixel_two_thirds3 = image_color[0, two_thirds_x3]
            color_pixel_right3 = image_color[0, right_x3]

            color_pixel_left4 = image_color[0, left_x4]
            color_pixel_one_third4 = image_color[0, one_third_x4]
            color_pixel_two_thirds4 = image_color[0, two_thirds_x4]
            color_pixel_right4 = image_color[0, right_x4]

            # Generate a horizontal linear gradient using the twelve color points
            gradient_linear = np.zeros((height, width, 3), dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    ratio1 = (x - left_x1) / (right_x1 - left_x1)
                    ratio2 = (x - left_x2) / (right_x2 - left_x2)
                    ratio3 = (x - left_x3) / (right_x3 - left_x3)
                    ratio4 = (x - left_x4) / (right_x4 - left_x4)
                    
                    interpolated_color1 = (1 - ratio1) * color_pixel_left1 + ratio1 * color_pixel_one_third1
                    interpolated_color2 = (1 - ratio2) * color_pixel_left2 + ratio2 * color_pixel_one_third2
                    interpolated_color3 = (1 - ratio3) * color_pixel_left3 + ratio3 * color_pixel_one_third3
                    interpolated_color4 = (1 - ratio4) * color_pixel_left4 + ratio4 * color_pixel_one_third4
                    
                    interpolated_color5 = (1 - ratio1) * color_pixel_one_third1 + ratio1 * color_pixel_two_thirds1
                    interpolated_color6 = (1 - ratio2) * color_pixel_one_third2 + ratio2 * color_pixel_two_thirds2
                    interpolated_color7 = (1 - ratio3) * color_pixel_one_third3 + ratio3 * color_pixel_two_thirds3
                    interpolated_color8 = (1 - ratio4) * color_pixel_one_third4 + ratio4 * color_pixel_two_thirds4
                    
                    interpolated_color9 = (1 - ratio1) * color_pixel_two_thirds1 + ratio1 * color_pixel_right1
                    interpolated_color10 = (1 - ratio2) * color_pixel_two_thirds2 + ratio2 * color_pixel_right2
                    interpolated_color11 = (1 - ratio3) * color_pixel_two_thirds3 + ratio3 * color_pixel_right3
                    interpolated_color12 = (1 - ratio4) * color_pixel_two_thirds4 + ratio4 * color_pixel_right4
                    

                    interpolated_color = (interpolated_color1 + interpolated_color2 + interpolated_color3 + interpolated_color4 + interpolated_color5 + interpolated_color6 + interpolated_color7 + interpolated_color8 + interpolated_color9 + interpolated_color10 + interpolated_color11 + interpolated_color12) / 12
                    gradient_linear[y, x] = interpolated_color

            cv2.imwrite('images/gradient_12_points.jpg', gradient_linear)

            # Subtract the linear gradient from the color image
            image_depolluted = cv2.subtract(image_color, gradient_linear)

            return image_depolluted
        else:
            print("No point without stars found.")
            return image_color  # Return the original image


    # Load the grayscale image
    image_gray = cv2.imread('images/barnard_stacked_gradient.png', cv2.IMREAD_GRAYSCALE)

    # Load the color image
    image_color = cv2.imread('images/barnard_stacked_gradient.png')

    # Check if the images were loaded successfully
    if image_gray is None or image_color is None:
        print("Failed to load one or more images.")
    else:
        num_columns_to_check = 1
        threshold_value = 128

        depolluted_image = remove_light_pollution(image_color, image_gray, num_columns_to_check, threshold_value)

        # Display the depolluted image
        cv2.imshow('Depolluted Image', depolluted_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imwrite('images/depolluted_image_12_gradient.jpg', depolluted_image)
