#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from tkinter import *
import calculator

gui = Tk() 

# set the title of the GUI window
#gui.configure(background="gray30") 
gui.title('Calculator') 

# StringVar() is the variable class 
# we create an instance of this class 
equation = StringVar() 

field = Entry(gui, textvariable=equation) 
field.grid(row=0, column=1, columnspan=4)

equation.set('Type your calculation')  

#row 1
button = Button(gui, text='AC', width=5, command=lambda: calculator.clear(equation))
button.grid(row=1, column=1)  

button = Button(gui, text='(', width=5, command=lambda: calculator.click("(", equation))
button.grid(row=1, column=2)  

button = Button(gui, text=')', width=5, command=lambda: calculator.click(")", equation)) 
button.grid(row=1, column=3)  

button = Button(gui, text='/', width=5, command=lambda: calculator.click("/", equation)) 
button.grid(row=1, column=4) 

#row2
button = Button(gui, text='7', width=5, command=lambda: calculator.click(7, equation))
button.grid(row=2, column=1)  

button = Button(gui, text='8', width=5, command=lambda: calculator.click(8, equation))
button.grid(row=2, column=2)  

button = Button(gui, text='9', width=5, command=lambda: calculator.click(9, equation)) 
button.grid(row=2, column=3)  

button = Button(gui, text='*', width=5, command=lambda: calculator.click("*", equation)) 
button.grid(row=2, column=4) 


#row3
button = Button(gui, text='4', width=5, command=lambda: calculator.click(4, equation))
button.grid(row=3, column=1)  

button = Button(gui, text='5', width=5, command=lambda: calculator.click(5, equation))
button.grid(row=3, column=2)  

button = Button(gui, text='6', width=5, command=lambda: calculator.click(6, equation)) 
button.grid(row=3, column=3)  

button = Button(gui, text='-', width=5, command=lambda: calculator.click("-", equation)) 
button.grid(row=3, column=4) 

#row4
button = Button(gui, text='1', width=5, command=lambda: calculator.click(1, equation))
button.grid(row=4, column=1)  

button = Button(gui, text='2', width=5, command=lambda: calculator.click(2, equation))
button.grid(row=4, column=2)  

button = Button(gui, text='3', width=5, command=lambda: calculator.click(3, equation)) 
button.grid(row=4, column=3)  

button = Button(gui, text='+', width=5, command=lambda: calculator.click("+", equation)) 
button.grid(row=4, column=4) 

#row5
button = Button(gui, text='0', width=11, command=lambda: calculator.click(0, equation))
button.grid(row=5, column=1, columnspan=2)  

button = Button(gui, text=',', width=5, command=lambda: calculator.click(".", equation))
button.grid(row=5, column=3)  

button = Button(gui, text='=', width=5, command=lambda: calculator.click_equals(equation))
button.grid(row=5, column=4) 


#exit
button = Button(gui, text='Exit', width=5, command=gui.destroy) 
button.grid(row=6, column=4)  


gui.mainloop() 