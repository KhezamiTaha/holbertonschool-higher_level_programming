#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))

def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))