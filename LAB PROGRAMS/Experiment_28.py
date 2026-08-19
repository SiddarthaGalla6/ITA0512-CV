import cv2
cap=cv2.VideoCapture("input.mp4")
while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.rectangle(frame,(170,120),(360,260),(0,255,0),2)
    cv2.imwrite("vehicle_output.jpg",frame)
    break
cap.release()
