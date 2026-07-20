import cv2
image = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
lines = cv2.HoughLinesP(edges, 1, 3.14/180, 50, minLineLength=50, maxLineGap=50)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line.flatten()
        cv2.line(image, (x1,y1), (x2,y2), (0,255,0),3)
cv2.imshow("Lane Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
