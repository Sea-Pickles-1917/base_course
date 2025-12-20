import numpy as np

n = 10
array1 = np.random.randint(0, 100, n)
array2 = np.random.randint(0, 100, n)
array3 = np.random.randint(0, 100, n)

max_number = np.max([array1, array2, array3])
array_sum = np.sum([array1, array2, array3])

print(f "максимальное значение: {max_number}, сумма элементов: {array_sum}")
