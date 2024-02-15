#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            new = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            new = 0
        except IndexError:
            print("out of range")
            new = 0
        except ZeroDivisionError:
            print("division by 0")
            new = 0
        finally:
            res.append(new)
    return res
