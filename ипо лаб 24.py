import numpy as np
def negative(arr):
    # Находим первый отрицательный элемент
    negative_indices = np.where(arr < 0)
    if negative_indices[0].size == 0:
        end = len(arr)
    else:
        end = negative_indices[0][0]
    # Проверяем, образуют ли элементы до первого отрицательного элемента возрастающую последовательность
    return np.all(arr[:end - 1] < arr[1:end])
# Пример использования функции
arr = np.array([1, 2, 3, -1, 5])
print(negative(arr))  # Выводит: True
