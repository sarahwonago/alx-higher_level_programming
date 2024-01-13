#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_key = list(a_dictionary)
    for i in dict_key:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return dict_key         
