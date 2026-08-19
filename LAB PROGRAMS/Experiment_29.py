import cv2
img=cv2.imread("input.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eye=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
eyes=eye.detectMultiScale(gray,1.1,5)
for x,y,w,h in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imwrite("eye_output.jpg",img)
