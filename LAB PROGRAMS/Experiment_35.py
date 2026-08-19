import cv2
img=cv2.imread("input.jpg")
cv2.putText(img,"Hello OpenCV",(120,340),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imwrite("text_output.jpg",img)
