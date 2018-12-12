#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from tkinter import *
import noeval_calculator as calc

gui = Tk() 

# set the title of the GUI window
#gui.configure(background="gray30") 
gui.title('Calculator') 

# StringVar() is the variable class 
# we create an instance of this class 
output = StringVar() 

field = Entry(gui, textvariable=output) 
field.grid(row=0, column=1, columnspan=4)

output.set('0')  

#row 1
button = Button(gui, text='1', width=5, command=lambda: calc.click(1, output))
button.grid(row=1, column=1)  

button = Button(gui, text='2', width=5, command=lambda: calc.click(2, output))
button.grid(row=1, column=2)  

button = Button(gui, text='3', width=5, command=lambda: calc.click(3, output)) 
button.grid(row=1, column=3)  

button = Button(gui, text='+', width=5, command=lambda: calc.click_operator("+", output)) 
button.grid(row=1, column=4) 

#row2
button = Button(gui, text='4', width=5, command=lambda: calc.click(4, output))
button.grid(row=2, column=1)  

button = Button(gui, text='5', width=5, command=lambda: calc.click(5, output))
button.grid(row=2, column=2)  

button = Button(gui, text='6', width=5, command=lambda: calc.click(6, output)) 
button.grid(row=2, column=3)  

button = Button(gui, text='-', width=5, command=lambda: calc.click_operator("-", output)) 
button.grid(row=2, column=4) 


#row3
button = Button(gui, text='7', width=5, command=lambda: calc.click(7, output))
button.grid(row=3, column=1)  

button = Button(gui, text='8', width=5, command=lambda: calc.click(8, output))
button.grid(row=3, column=2)  

button = Button(gui, text='9', width=5, command=lambda: calc.click(9, output)) 
button.grid(row=3, column=3)  

button = Button(gui, text='*', width=5, command=lambda: calc.click_operator("*", output)) 
button.grid(row=3, column=4) 

#row4
button = Button(gui, text='AC', width=5, command=lambda: calc.clear(output))
button.grid(row=4, column=1)  

button = Button(gui, text='0', width=5, command=lambda: calc.click(0, output))
button.grid(row=4, column=2)  

button = Button(gui, text='=', width=5, command=lambda: calc.click_equals(output))
button.grid(row=4, column=3)  

button = Button(gui, text='/', width=5, command=lambda: calc.click_operator("/", output)) 
button.grid(row=4, column=4) 


#exit
button = Button(gui, text='Exit', width=5, command=gui.destroy) 
button.grid(row=5, column=4)  


gui.mainloop() 