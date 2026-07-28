import cv2
img = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original", img)
cv2.imshow("270 Degree Rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
