import numpy as np
edges = np.array([1, 0, 1, 0, 1])
linked = edges.copy()
for i in range(1, len(edges)-1):
    if edges[i] == 0 and edges[i-1] == 1 and edges[i+1] == 1:
        linked[i] = 1
print("Original Edge :", edges)
print("Linked Edge   :", linked)

Output:
Original Edge : [1 0 1 0 1]
Linked Edge   : [1 1 1 1 1]
