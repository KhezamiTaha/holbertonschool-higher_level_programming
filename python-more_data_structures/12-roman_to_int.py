#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    rom = roman_string
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(rom) == 1:
        return dic[rom[0]]
    number = 0
    i = 0
    while i < (len(rom) - 1):
        if dic[rom[i]] >= dic[rom[i + 1]]:
            number = number + dic[rom[i]]
            i = i + 1
        else:
            number = number + dic[rom[i + 1]] - dic[rom[i]]
            i = i + 2
    if dic[rom[len(rom) - 1]] <= dic[rom[len(rom) - 2]]:
        number = number + dic[rom[len(rom) - 1]]
    return number
