#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = ()
tuple_b = (88, 11)
a = tuple_a + (0, 0)
print(() + (1, 7, 4))
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
