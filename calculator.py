#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from tkinter import *

# the expression to compute is globally declared 
to_compute = "" 
# StringVar() is the variable class 
# we create an instance of this class 
  
# Update expression in the text field
def click(key, equation): 
    # point out the global expression variable 
	global to_compute 
  
    # concatenation of string 
	to_compute = to_compute + str(key) 
  
    # update the expression by using set method 
	equation.set(to_compute) 
  
  
# Function to evaluate the final expression 
def click_equals(equation): 
	try: 
		global to_compute 
  
        # Evaluate the expression and  convert the result into a string 
		total = str(eval(to_compute)) 
  
		equation.set(total) 
  
        # initialze again the expression variable 
		to_compute = "" 
  
    # handle error (division by zero...)
	except: 
  
		equation.set(" error ") 
		to_compute = "" 
  
  
# Function to clear the content of the text field
def clear(equation): 
	global to_compute 
	to_compute = "" 
	equation.set("") 

