import cv2
image = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg", 0)
sx = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sy = cv2.Sobel(image, cv2.CV_64F, 1, 0)
cv2.imshow("Original Image ", image)
cv2.imshow("Sobel X", sx)
cv2.imshow("Sobel Y", sy)
cv2.waitKey(0)
cv2.destroyAllWindows()
