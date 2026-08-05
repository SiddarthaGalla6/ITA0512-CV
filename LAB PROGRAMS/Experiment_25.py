import cv2
image = cv2.imread("C:/Users/sidda/Downloads/Thor.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
watch = cv2.CascadeClassifier("watch.xml")
objects = watch.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
cv2.imshow("Original Image", image)
cv2.imshow("Watch Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
