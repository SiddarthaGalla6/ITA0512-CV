import cv2
import numpy as np
h,w=400,600
img=np.ones((h,w,3),np.uint8)*255
s=min(h,w)//10
img[:s,:s]=(0,0,0)
img[:s,-s:]=(255,0,0)
img[-s:,:s]=(0,255,0)
img[-s:,-s:]=(0,0,255)
cv2.imwrite("boxes.jpg",img)
