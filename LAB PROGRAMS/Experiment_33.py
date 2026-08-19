import cv2
import numpy as np
img=np.ones((400,600,3),np.uint8)*255
cv2.rectangle(img,(150,100),(450,300),(0,0,255),3)
cv2.imwrite("rectangle.jpg",img)
