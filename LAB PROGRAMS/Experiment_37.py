import cv2
img=cv2.imread("input.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,(0,50,50),(179,255,255))
foreground=cv2.bitwise_not(mask)
result=cv2.bitwise_and(img,img,mask=foreground)
cv2.imwrite("foreground.jpg",result)
