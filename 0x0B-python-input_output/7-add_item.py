#!/usr/bin/python3
import os
import sys
import json


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_\
        json_file.py').load_from_json_file


filename = add_item.json
args = len(sys.argv)

if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as j_file:
        j_file.write('[]')


if args > 1:
    py_list = load_from_json_file(filename)
    for i in range(1, args):
        py_list.append(sys.argv[i])
    save_to_json_file(py_list, filename)
