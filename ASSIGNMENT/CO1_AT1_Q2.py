import cv2
image = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
high = cv2.resize(image, None, fx = 1, fy = 1)
low = cv2.resize(image, None, fx = 0.25, fy = 0.25)
cv2.imshow("High Sampling", high)
cv2.imshow("Low Sampling", low)
cv2.waitKey(0)
cv2.destroyAllWindows()
