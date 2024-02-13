#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = dict(sorted(a_dictionary.items()))
    for k, v in new.items():
        print("{}: {}".format(k, v))
