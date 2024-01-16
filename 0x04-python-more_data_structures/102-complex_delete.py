#!/usr/bin/python3

def complex_delete(a_dictionary, value):
   ky_del = [k for k, v in a_dictionary.items() if v == value]

   for ky in ky_del:
      del a_dictionary[ky]
   return a_dictionary
