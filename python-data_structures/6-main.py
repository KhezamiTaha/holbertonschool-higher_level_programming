#!/usr/bin/python3
print_m = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_m(matrix)
print("--")
print_m()
