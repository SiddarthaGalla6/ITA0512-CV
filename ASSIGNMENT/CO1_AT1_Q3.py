import cv2
img = cv2.imread = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
h, w = img.shape[:2]
small = cv2.resize(img, (w//5,h//5))
jagged = cv2.resize(small,(w, h), interpolation = cv2.INTER_NEAREST)
cv2.imshow("Low Sampling", jagged)
cv2.waitKey(0)
cv2.destroyAllWindows()
