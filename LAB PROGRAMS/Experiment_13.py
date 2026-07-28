import cv2
import numpy as np
img = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
rows, cols = img.shape[:2]
p1 = np.float32([[0,0], [cols-1,0], [0,rows-1]])
p2 = np.float32([[0,0], [cols-1,50], [50,rows-1]])
M = cv2.getAffineTransform(p1, p2)
result = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Original", img)
cv2.imshow("Affine", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
