import numpy as np

# 创建一个二维数组
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

# 创建一个一维数组
array_1d = np.array([7, 8, 9])

# 使用 vstack 垂直堆叠将一维数组添加到二维数组中
result = np.vstack((array_2d, array_1d))

print(result)