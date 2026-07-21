import cv2
import numpy as np
img = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(img, kernel)
cv2.imshow("Eroded", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
