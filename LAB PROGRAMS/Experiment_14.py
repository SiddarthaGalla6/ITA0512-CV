import cv2
import numpy as np
img = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
p1 = np.float32([[0,0], [300,0], [0,300], [300,300]])
p2 = np.float32([[0,0], [250,50], [50,250], [300,300]])
M = cv2.getPerspectiveTransform(p1, p2)
result = cv2.warpPerspective(img, M, (300,300))
cv2.imshow("Original", img)
cv2.imshow("Perspective", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
