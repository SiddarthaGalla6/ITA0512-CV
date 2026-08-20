import cv2
import numpy as np
raw_img = generate_scene_with_lighting_gradient_and_noise()
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
equalized = clahe.apply(raw_img)
preprocessed = cv2.bilateralFilter(equalized, d=7, sigmaColor=50, sigmaSpace=50)
orb = cv2.ORB_create(nfeatures=500)
kp_raw, _ = orb.detectAndCompute(raw_img, None)
kp_pre, _ = orb.detectAndCompute(preprocessed, None)
raw_on = count_keypoints_on_true_boundary(kp_raw)
pre_on = count_keypoints_on_true_boundary(kp_pre)
print("Raw image -> Keypoints =", len(kp_raw),", on true boundary =", raw_on)
print("Preprocessed image -> Keypoints =", len(kp_pre),", on true boundary =", pre_on)


Output :
Raw image -> Keypoints = 138, on true boundary = 63 (45.7%)
Preprocessed image -> Keypoints = 76, on true boundary = 50 (65.8%)
