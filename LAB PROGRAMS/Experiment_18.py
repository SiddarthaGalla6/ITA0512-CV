import cv2
image = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
image1 = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
roi = image1[50:150, 50:150]
image1[200:300, 200:300] = roi
cv2.imshow("Original Image", image)
cv2.imshow("ROI", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
