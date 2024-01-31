#!/usr/bin/python3
for i in range(1, 90):
    if (i % 11 != 0 and i % 10 != 0 and i / 10 < i % 10 and i != 89):
        print("{:0=2d}".format(i), end=", ")
    elif i == 89:
        print(i)
