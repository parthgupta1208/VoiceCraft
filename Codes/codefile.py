
import tkinter as tk

def click_button(button):
    global expression
    expression += str(button)
    equation.set(expression)
    
def clear():
    global expression
    expression = ""
    equation.set("")
    
def evaluate():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

expression = ""

root = tk.Tk()
root.title("Calculator")

equation = tk.StringVar()

label = tk.Label(root, textvariable=equation, font=('arial', 28), justify='right')
label.grid(columnspan=4)

button1 = tk.Button(root, text='1', font=('arial', 24), command=lambda: click_button(1))
button1.grid(row=1, column=0)

button2 = tk.Button(root, text='2', font=('arial', 24), command=lambda: click_button(2))
button2.grid(row=1, column=1)

button3 = tk.Button(root, text='3', font=('arial', 24), command=lambda: click_button(3))
button3.grid(row=1, column=2)

button_div = tk.Button(root, text='/', font=('arial', 24), command=lambda: click_button('/'))
button_div.grid(row=1, column=3)

button4 = tk.Button(root, text='4', font=('arial', 24), command=lambda: click_button(4))
button4.grid(row=2, column=0)

button5 = tk.Button(root, text='5', font=('arial', 24), command=lambda: click_button(5))
button5.grid(row=2, column=1)

button6 = tk.Button(root, text='6', font=('arial', 24), command=lambda: click_button(6))
button6.grid(row=2, column=2)

button_mult = tk.Button(root, text='*', font=('arial', 24), command=lambda: click_button('*'))
button_mult.grid(row=2, column=3)

button7 = tk.Button(root, text='7', font=('arial', 24), command=lambda: click_button(7))
button7.grid(row=3, column=0)

button8 = tk.Button(root, text='8', font=('arial', 24), command=lambda: click_button(8))
button8.grid(row=3, column=1)

button9 = tk.Button(root, text='9', font=('arial', 24), command=lambda: click_button(9))
button9.grid(row=3, column=2)

button_sub = tk.Button(root, text='-', font=('arial', 24), command=lambda: click_button('-'))
button_sub.grid(row=3, column=3)

button_dot = tk.Button(root, text='.', font=('arial', 24), command=lambda: click_button('.'))
button_dot.grid(row=4, column=0)

button0 = tk.Button(root, text='0', font=('arial', 24), command=lambda: click_button(0))
button0.grid(row=4, column=1)

button_equal = tk.Button(root, text='=', font=('arial', 24), command=evaluate)
button_equal.grid(row=4, column=2)

button_plus = tk.Button(root, text='+', font=('arial', 24), command=lambda: click_button('+'))
button_plus.grid(row=4, column=3)

button_clear = tk.Button(root, text='C', font=('arial', 24), command=clear)
button_clear.grid(row=5, column=2)

root.mainloop()
