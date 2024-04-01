import numpy as np

# 0부터 9까지
range_vec = np.arange(10)
print(range_vec)
print("\t")

# 1부터 9까지 +2씩 적용되는 범위
n = 2
range_n_step_vec = np.arange(1, 10, n)
print(range_n_step_vec)
print("\t")

reshape_mat = np.array(np.arange(30)).reshape((5,6))
print(reshape_mat)