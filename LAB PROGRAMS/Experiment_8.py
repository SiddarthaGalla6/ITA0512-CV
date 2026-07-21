import cv2
import numpy as np
image = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
kernal = np.ones((5,5), np.uint8)
dilated = cv2.dilate(image, kernal, iterations=1)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
