import numpy as np
rows = np.random.randint(15, 101)
cols = np.random.randint(15, 101)
array = np.random.randint(1, 1001, size=(rows, cols))
print("Массив:")
print(array)
row = array[0]
min_element = np.min(row)
print("\nМинимальный элемент в строке варианта:", min_element)
product = array * min_element
print("\nПроизведение матрицы на минимальный элемент:")
print(product)
