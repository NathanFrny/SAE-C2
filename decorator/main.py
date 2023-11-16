from Blur import Blur
from Image import Image
from Saturation import Saturation
from Gamma import Gamma
import cv2

image = Image('decorator/barnard_stacked_gradient.png')

# MODIFIER LE GAMMA ICI
gamma_processor = Gamma(1.5)
# MODIFIER LE FLOU ICI
blur_processor = Blur(5)
# MODIFIER LA SATURATION ICI
saturation_processor = Saturation(1)

image.apply(gamma_processor)
image.apply(blur_processor)
image.apply(saturation_processor)

cv2.imshow('Modified Image', image.image)
cv2.waitKey(0)
cv2.destroyAllWindows()