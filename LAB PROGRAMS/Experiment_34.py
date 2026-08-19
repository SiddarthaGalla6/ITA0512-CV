import cv2
import numpy as np
img=np.ones((400,600,3),np.uint8)*255
cv2.circle(img,(300,200),100,(0,255,0),3)
cv2.imwrite("circle.jpg",img)
