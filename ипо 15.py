import random
import time


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def test_sorting_time():
    num_elements = [10, 100, 1000, 10000, 100000]

    table = []

    for n in num_elements:
        arr = [random.randint(1, 1000) for _ in range(n)]

        start_time = time.time()
        sorted_arr = bubble_sort(arr)
        end_time = time.time()

        execution_time = end_time - start_time

        table.append([n, execution_time])

    return table
results = test_sorting_time()

for result in results:
    print(result)

