import cv2
img = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
bigger = cv2.resize(img, None, fx=2, fy=2)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow("Bigger", bigger)
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
