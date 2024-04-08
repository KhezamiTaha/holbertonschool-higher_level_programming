#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return   # this will print None
    for roww in matrix:
        for i in range(len(roww)):
            print("{:d}".format(roww[i]), end="")
            if i != len(roww) - 1:
                print(" ", end="")
        print()
