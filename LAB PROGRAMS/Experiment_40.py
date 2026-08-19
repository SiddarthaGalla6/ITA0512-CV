import cv2
import pytesseract
cap=cv2.VideoCapture("input.mp4")
while True:
    ret,frame=cap.read()
    if not ret:
        break
    text=pytesseract.image_to_string(frame).strip()
    if text:
        print(text)
cap.release()
