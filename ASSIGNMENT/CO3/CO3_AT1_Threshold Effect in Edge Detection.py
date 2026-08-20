import cv2
import numpy as np
import matplotlib.pyplot as plt
img = np.full((300, 300), 200, dtype=np.uint8)
cv2.rectangle(img, (40, 40), (140, 140), 80, -1)
cv2.circle(img, (210, 90), 55, 130, -1)
pts = np.array([[60, 260], [140, 180], [220, 260]], np.int32)
cv2.fillPoly(img, [pts], 60)
noise = np.random.normal(0, 15, img.shape).astype(np.int16)
noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8) cv2.imwrite("input.png", noisy_img)thresholds = [(10, 50), (50, 150), (150, 250)]
labels = ["Low", "Medium", "High"]
for (low, high), label in zip(thresholds, labels):
edges = cv2.Canny(noisy_img, low, high)
count = np.count_nonzero(edges)
print(f"{label} Threshold ({low},{high}) -> Edge pixel count = {count}")


Output :
Low Threshold (10,50) -> Edge pixel count = 33002
Medium Threshold (50,150) -> Edge pixel count = 27603
High Threshold (150,250) -> Edge pixel count = 1715
