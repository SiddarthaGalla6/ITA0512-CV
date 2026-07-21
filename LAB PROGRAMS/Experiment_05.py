import cv2
import matplotlib.pyplot as plt
img = cv2.imread("C:/Users/sidda/Downloads/loki wallpaper.jpg")
for i, c in enumerate(['b', 'g', 'r']):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=c)
plt.show()
