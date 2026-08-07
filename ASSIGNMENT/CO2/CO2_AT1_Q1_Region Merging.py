import numpy as np
region1 = np.array([45, 50])
region2 = np.array([52, 55])
threshold = 5
mean1 = np.mean(region1)
mean2 = np.mean(region2)
difference = abs(mean1 - mean2)
print("Region 1 Mean =", mean1)
print("Region 2 Mean =", mean2)
print("Difference =", difference)
if difference <= threshold:
    merged = np.concatenate((region1, region2))
    print("Merged Region =", merged)
else:
    print("Regions are NOT merged")


Output:
Region 1 Mean = 47.5
Region 2 Mean = 53.5
Difference = 6.0
Regions are NOT merged
