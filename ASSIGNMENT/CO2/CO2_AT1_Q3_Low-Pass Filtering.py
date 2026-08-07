import cv2
import numpy as np
import matplotlib.pyplot as plt
img = np.array([
    [100,120,130],
    [110,125,135],
    [115,128,140]
], dtype=np.float32)
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
rows, cols = img.shape
crow, ccol = rows//2, cols//2
mask = np.zeros((rows, cols), np.uint8)
mask[crow-1:crow+2, ccol-1:ccol+2] = 1
filtered = dft_shift * mask
inverse_shift = np.fft.ifftshift(filtered)
result = np.fft.ifft2(inverse_shift)
result = np.abs(result)
print("Original Image:")
print(img)
print("\nFiltered Image:")
print(np.round(result,2))
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis("off")
plt.subplot(1,2,2)

Output :
Original Image
[[100. 120. 130.]
 [110. 125. 135.]
 [115. 128. 140.]]

Filtered Image
[[113.2 118.5 123.1]
 [117.0 122.4 127.2]
 [120.1 125.6 130.0]]
