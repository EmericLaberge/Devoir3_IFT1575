import numpy as np

q = np.array([[10, 7, 0, 11], [2, 1, 8, 4], [4, 9, 6, 0], [3, 5, 2, 7]])
d = np.array([[50, 50, 95, 45], [30, 30, 55, 65], [70, 50, 25, 55], [100, 60, 55, 25]])
c = np.zeros((4, 4))

for k in range(4):
    for i in range(4):
        for j in range(4):
            c[i][k] += q[i][j] * d[j][k]
print(c)
# Hungarian algorithm
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(c)

c_hungarian = c[row_ind, col_ind]
print(c_hungarian)
