import cv2
img = cv2.imread("image.jpg")
rotated = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("Original", img)
cv2.imshow("180 Degree Rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
