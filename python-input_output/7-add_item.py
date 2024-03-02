#!/usr/bin/python3
import sys
from os.path import exists


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
listy = []
for arg in sys.argv[1: ]:
    listy.append(arg)
if exists("add_item.json"):
    list2= load_from_json_file("add_item.json")
    list_final = list2 + listy
else:
    list_final = listy
save_to_json_file(list_final, "add_item.json")
