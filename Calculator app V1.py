import tkinter as tk
from math import *

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "modulo"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_sin():
    first_number = e.get()
    global f_num
    global math
    math = "sin"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_cos():
    first_number = e.get()
    global f_num
    global math
    math = "cos"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_tan():
    first_number = e.get()
    global f_num
    global math
    math = "tan"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_modulo():
    first_number = e.get()
    if first_number == "":
        e.insert(0, "Error, enter a number first")
    else:
        global f_num
        global math
        math = "modulo"
        f_num = float(first_number)
        e.delete(0, tk.END)



def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

    if math == "power":
        e.insert(0, f_num ** float(second_number))

    if math == "modulo":
        e.insert(0, f_num % float(second_number))

    if math == "square_root":
        e.insert(0, sqrt(f_num))

    if math == "sin":
        e.insert(0, sin(f_num))

    if math == "cos":
        e.insert(0, cos(f_num))

    if math == "tan":
        e.insert(0, tan(f_num))

root = tk.Tk()
root.title("Scientific Calculator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)
button_power = tk.Button(root, text="x^y", padx=41, pady=20, command=button_power)
button_power.grid(row=5, column=3)
button_modulo = tk.Button(root, text="%", padx=41, pady=20, command=button_modulo)
button_modulo.grid(row=6, column=3)
button_square_root = tk.Button(root, text="sqrt", padx=31, pady=20, command=button_square_root)
button_square_root.grid(row=6, column=2)
button_sin = tk.Button(root, text="sin", padx=35, pady=20, command=button_sin)
button_sin.grid(row=6, column=0)
button_cos = tk.Button(root, text="cos", padx=35, pady=20, command=button_cos)
button_cos.grid(row=6, column=1)
button_tan = tk.Button(root, text="tan", padx=35, pady=20, command=button_tan)
button_tan.grid(row=5, column=1)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)

root.mainloop()




