def find_max_element(matrix):
    max_element = matrix[0][0]
    max_row = 0
    max_col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_row = i
                max_col = j
    return max_row, max_col


def swap_max_elements(matrix_a, matrix_b):
    max_element_a_pos = find_max_element(matrix_a)
    max_element_b_pos = find_max_element(matrix_b)

    max_element_a = matrix_a[max_element_a_pos[0]][max_element_a_pos[1]]
    max_element_b = matrix_b[max_element_b_pos[0]][max_element_b_pos[1]]

    matrix_a[max_element_a_pos[0]][max_element_a_pos[1]] = max_element_b
    matrix_b[max_element_b_pos[0]][max_element_b_pos[1]] = max_element_a


# Пример использования
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Before swapping:")
print("Matrix A:")
for row in matrix_a:
    print(row)
print("Matrix B:")
for row in matrix_b:
    print(row)

swap_max_elements(matrix_a, matrix_b)

print("After swapping:")
print("Matrix A:")
for row in matrix_a:
    print(row)
print("Matrix B:")
for row in matrix_b:
    print(row)
