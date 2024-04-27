#!/usr/bin/python3

def roman_to_int(roman_string):
	roman_int_map = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 100,
		'D': 500,
		'M': 1000
	}

	prev_va = roman_int_map[roman_string[1]]
	curr_va = roman_int_map[roman_string[1]]

	print(prev_va, curr_va)

roman_to_int('II')
