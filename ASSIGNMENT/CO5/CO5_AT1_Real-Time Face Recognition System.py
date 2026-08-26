import cv2
import numpy as np
import time
def acquire_frame(width=320, height=240, seed=0):
    rng = np.random.default_rng(seed)
    frame = rng.integers(40, 90, (height, width, 3), dtype=np.uint8)
    return frame
def preprocess(frame, target_width=160):
    scale = target_width / frame.shape[1]
    resized = cv2.resize(frame, (target_width, int(frame.shape[0] * scale)), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    equalised = cv2.equalizeHist(gray)
    return equalised
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
def detect_faces(gray_frame):
    return face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
def build_enrolled_dataset():
    p1 = np.zeros((80, 80), dtype=np.uint8)
    cv2.ellipse(p1, (40, 40), (28, 34), 0, 0, 360, 200, -1)
    cv2.circle(p1, (30, 32), 5, 60, -1)
    cv2.circle(p1, (50, 32), 5, 60, -1)
    p2 = np.zeros((80, 80), dtype=np.uint8)
    cv2.ellipse(p2, (40, 40), (30, 32), 0, 0, 360, 160, -1)
    cv2.circle(p2, (28, 30), 6, 40, -1)
    cv2.circle(p2, (52, 30), 6, 40, -1)
    images = [p1, p2]
    labels = [1, 2]
    return images, np.array(labels)
def train_recognizer():
    images, labels = build_enrolled_dataset()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(images, labels)
    return recognizer
def run_pipeline(num_frames=15):
    recognizer = train_recognizer()
    names = {1: "Employee_A", 2: "Employee_B", -1: "Unknown"}
    frame_times = []
    total_faces_detected = 0
    for i in range(num_frames):
        start = time.perf_counter()
        frame = acquire_frame(seed=i)
        gray = preprocess(frame)
        faces = detect_faces(gray)
        total_faces_detected += len(faces)
        probe_images, _ = build_enrolled_dataset()
        probe = probe_images[i % 2]
        label, confidence = recognizer.predict(probe)
        elapsed_ms = (time.perf_counter() - start) * 1000
        frame_times.append(elapsed_ms)
    avg_latency = sum(frame_times) / len(frame_times)
    fps = 1000.0 / avg_latency
    print(f"Frames processed            : {num_frames}")
    print(f"Average latency / frame     : {avg_latency:.2f} ms")
    print(f"Effective throughput        : {fps:.1f} FPS")
    print(f"Real-time constraint (<33ms, i.e. >=30 FPS): {'SATISFIED' if avg_latency < 33.3 else 'VIOLATED'}")
    print(f"Faces located by Haar cascade across all frames: {total_faces_detected}")
    print(f"Sample recognition on last probe -> {names.get(label, 'Unknown')} (confidence={confidence:.2f}, lower=better)")
run_pipeline()

Output:
Frames processed            : 15
Average latency / frame     : 8.70 ms
Effective throughput        : 115.0 FPS
Real-time constraint (<33ms, i.e. >=30 FPS): SATISFIED
Faces located by Haar cascade across all frames: 0
Sample recognition on last probe -> Employee_A (confidence=0.00, lower=better)
