import cv2
import numpy as np
image = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Original Image", image)
cv2.imshow("Black Hat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
