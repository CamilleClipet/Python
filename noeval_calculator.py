#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import math

operator = ""
nb_left = ""
nb_right = ""
result = ""
left_is_filled = False

def click(key, output):
	global nb_left
	global nb_right
	global left_is_filled

	if left_is_filled == False:
		nb_left = nb_left + str(key)
		output.set(nb_left)
	else:
		nb_right = nb_right + str(key)
		output.set(nb_right)


def click_operator(key, output):
	global operator
	global result
	global nb_left
	global nb_right
	global left_is_filled

	if nb_left != "" and nb_right != "" and operator != "":
		_result = click_equals(output)
		result = _result
		operator = key
		nb_left = _result
		left_is_filled = True

	else:
		left_is_filled = True
		nb_right = ""
		operator = key



def click_equals(output):
	global operator
	global result
	global nb_left
	global nb_right
	global left_is_filled

	if nb_left != "" and nb_right != "" and operator != "":
		if operator == "+":
			_result = int(nb_left) + int(nb_right)
		elif operator == "-":
			_result = int(nb_left) - int(nb_right)
		elif operator == "*":
			_result = int(nb_left) * int(nb_right)
		elif operator == "/":
			_result = int(nb_left) / int(nb_right)
		elif operator == "%":
			_result = int(nb_left) % int(nb_right)
	elif nb_left != "" and nb_right == "":
		_result = nb_left

	output.set(str(_result))
	operator = ""
	nb_left = ""
	nb_right = ""
	result = ""
	left_is_filled = False

	return _result
	

def clear(output):
	global operator
	global result
	global nb_left
	global nb_right
	global left_is_filled

	operator = ""
	nb_left = ""
	nb_right = ""
	result = ""
	left_is_filled = False

	output.set("0")


