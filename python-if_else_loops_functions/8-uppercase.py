#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            upper = upper + chr(ord(str[i]) - 32)
        else:
            upper = upper + str[i]
    print("{}".format(upper))
