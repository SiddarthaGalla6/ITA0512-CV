import cv2
img = cv2.imread("C:/Users/sidda/Downloads/download (1).jpg")
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Original", img)
cv2.imshow("90 Degree Rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
