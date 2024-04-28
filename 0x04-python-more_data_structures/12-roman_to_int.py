#!/usr/bin/python3

def roman_to_int(roman_string):
	roman_int_map = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}

	total = 0
	prev_value = 0

	if not isinstance(roman_string, str) or roman_string is None:
		return 0

	for chars in roman_string:
		int_val = roman_int_map[chars]

		if int_val > prev_value:
			total += int_val - 2 * prev_value
		else:
			total += int_val

		prev_value = int_val

	return total
