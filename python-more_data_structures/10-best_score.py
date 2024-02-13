#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = list(a_dictionary.values())[0]
    name = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = a_dictionary[key]
            name = key
    return name
