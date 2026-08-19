import cv2
img=cv2.imread("input.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
smile=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
smiles=smile.detectMultiScale(gray,1.5,20)
for x,y,w,h in smiles:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imwrite("smile_output.jpg",img)
