#!/usr/bin/python35
def fizzbuzz():
    for i in range(1, 101):
        if (i % 15 == 0):
            print("FizzBuzz ", end="")
        elif (i % 5 == 0):
            if (i != 100):
                print("Buzz ", end="")
            else:
                print("Buzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end="")
        else:
            print("{} ".format(i), end="")
