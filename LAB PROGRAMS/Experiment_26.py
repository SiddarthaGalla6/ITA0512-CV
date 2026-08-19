import cv2
cap=cv2.VideoCapture("input.mp4")
frames=[]
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
frames.reverse()
if frames:
    cv2.imwrite("reverse_frame.jpg",frames[0])
