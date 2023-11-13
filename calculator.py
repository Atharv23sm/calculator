
from tkinter import *

exp = "" 

def press(num): 
    
	global exp
 
	exp += str(num) 

	equation.set(exp) 

def equal(): 

	try: 
		global exp 

		total = str(eval(exp)) 
  
		equation.set(total) 
  
		exp = "" 
  
	except: 

		equation.set("Error") 
  
		exp = "" 

def clear(): 
    
	global exp 
 
	exp = "" 
 
	equation.set("") 
 
def backspace():
    
    global exp
    
    exp=exp[:-1]
    
    equation.set(exp)

if __name__ == "__main__": 

	gui = Tk() 

	gui.configure(background="grey") 
	gui.title("Calculator") 
	gui.geometry("300x350") 

	equation = StringVar() 

	field = Entry(gui, textvariable=equation, width="14", font=('Arial 30')) 

	field.grid(columnspan=5)

	button1 = Button(gui, text=' 1 ', fg='black', bg='#ddd', 
					command=lambda: press(1), height=3, width=7) 
	button1.grid(row=4, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='#ddd', 
					command=lambda: press(2), height=3, width=7) 
	button2.grid(row=4, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='#ddd', 
					command=lambda: press(3), height=3, width=7) 
	button3.grid(row=4, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='#ddd', 
					command=lambda: press(4), height=3, width=7) 
	button4.grid(row=5, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='#ddd', 
					command=lambda: press(5), height=3, width=7) 
	button5.grid(row=5, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='#ddd', 
					command=lambda: press(6), height=3, width=7) 
	button6.grid(row=5, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='#ddd', 
					command=lambda: press(7), height=3, width=7) 
	button7.grid(row=6, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='#ddd', 
					command=lambda: press(8), height=3, width=7) 
	button8.grid(row=6, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='#ddd', 
					command=lambda: press(9), height=3, width=7) 
	button9.grid(row=6, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='#ddd', 
					command=lambda: press(0), height=3, width=7) 
	button0.grid(row=7, column=1) 

	plus = Button(gui, text=' + ', fg='black', bg='#ddd', 
				command=lambda: press("+"), height=3, width=7) 
	plus.grid(row=4, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='#ddd', 
				command=lambda: press("-"), height=3, width=7) 
	minus.grid(row=5, column=3) 

	mult = Button(gui, text=' * ', fg='black', bg='#ddd', 
					command=lambda: press("*"), height=3, width=7) 
	mult.grid(row=6, column=3) 

	div = Button(gui, text=' / ', fg='black', bg='#ddd', 
					command=lambda: press("/"), height=3, width=7) 
	div.grid(row=7, column=3) 

	eql = Button(gui, text=' = ', fg='white', bg='green', 
				command=equal, height=3, width=18) 
	eql.grid(row=8, column=0, columnspan=2) 

	clr = Button(gui, text='Clear', fg='white', bg='red', 
				command=clear, height=3, width=18) 
	clr.grid(row=8, column=2, columnspan=2) 

	deci= Button(gui, text='.', fg='black', bg='#ddd', 
					command=lambda: press('.'), height=3, width=7) 
	deci.grid(row=7, column=0) 
	
	back = Button(gui, text='<=', fg='red', bg='#eee', 
				command=backspace, height=3, width=7) 
	back.grid(row=7, column=2) 
 
	gui.mainloop() 
