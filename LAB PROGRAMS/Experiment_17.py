import cv2
image = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
image1 = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
cv2.putText(image1, "Watermark", (30,20), cv2.FONT_HERSHEY_DUPLEX, 1, (225,225,225), 2)
cv2.imshow("Original Image", image)
cv2.imshow("WaterMark Image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
