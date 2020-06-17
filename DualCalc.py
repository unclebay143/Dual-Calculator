# A Calculator Application Code
# BY :
        # 吴 敏
        # 伊衣
        # 远航
        # 乐成

# Importing Python module responsible for building the Calculator interfaces
import tkinter as tk
# Importing messagebox from python module tkinter for showing messages to users in a box
from tkinter import messagebox
# import math module for handling mathematical expressions
import math

# The small screen showing the math expression and answers
bay_small_screen = None

# The big screen displaying the user inputs and answer
bay_big_screen = None

# The operator signs
sign = None

# Variable to get what is on the screen
f_num = None

# The calculator Frame
frame = None

# numbers on the calculator
num = None


# Function for handling sin
def sin():
    global sign
    global num
    sign = "sin"
    num = float(bay_small_screen.get())
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "sin(" + str(num) + ")")
    bay_small_screen.insert(0, "sin(" + str(num) + ")")


# Function for handling cos
def cos():
    global sign
    global num
    sign = "cos"
    num = float(bay_small_screen.get())
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "cos(" + str(num) + ")")
    bay_small_screen.insert(0, "cos(" + str(num) + ")")


# Function for handling tan
def tan():
    global sign
    global num
    sign = "tan"
    num = float(bay_small_screen.get())
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.insert(0, "tan(" + str(num) + ")")
    bay_small_screen.insert(0, "tan(" + str(num) + ")")


# Function for handling tan_inverse
def tan_inv():
    global sign
    global num
    sign = "tan_inv"
    num = float(bay_small_screen.get())
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "tan^-1(" + str(num) + ")")
    bay_small_screen.insert(0, "tan^-1(" + str(num) + ")")


# Function for handling cos_inverse
def cos_inv():
    global sign
    global num
    sign = "cos_inv"
    num = float(bay_small_screen.get())
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "cos^-1(" + str(num) + ")")
    bay_small_screen.insert(0, "cos^-1(" + str(num) + ")")


# Function for handling sin_inverse
def sin_inv():
    global sign
    global num
    sign = "sin_inv"
    num = float(bay_small_screen.get())
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "sin^-1(" + str(num) + ")")
    bay_small_screen.insert(0, "sin^-1(" + str(num) + ")")


# Function for exp in math
def exp():
    global num
    num = bay_small_screen.get()
    global sign
    sign = "exp"
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "bay_small_screen" + num)
    bay_small_screen.insert(0, "bay_small_screen" + num)


# Function for factorial in math
def fact():
    global num
    global sign
    num = int(bay_small_screen.get())
    sign = "fact"
    bay_big_screen.insert(len(bay_small_screen.get()), "!")
    bay_small_screen.insert(len(bay_small_screen.get()), "!")


# Function for square root in math
def sqrt():
    global num
    num = float(bay_small_screen.get())
    global sign
    sign = "sqrt"
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(0, "sqrt(" + str(num) + ")")
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_small_screen.insert(0, "sqrt(" + str(num) + ")")


# Function for cube in math
def cube():
    global num
    num = float(bay_small_screen.get())
    global sign
    sign = "cube"
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_big_screen.insert(len(bay_small_screen.get()), str(num) + "^3")
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_small_screen.insert(len(bay_small_screen.get()), "^3")


# Function for power in math
def n_pow():
    global f_num
    f_num = bay_small_screen.get()
    global sign
    sign = "n_pow"
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.insert(0, str(f_num) + " ^ ")


# Function for inverse in math
def inv():
    global num
    global sign
    sign = "inv"
    num = float(bay_small_screen.get())
    bay_big_screen.insert(len(bay_big_screen.get()), "^(-1)")
    bay_small_screen.insert(len(bay_small_screen.get()), "^(-1)")


# Function for remainder in math
def rem():
    global f_num
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    f_num = float(bay_small_screen.get())
    global sign
    sign = "rem"
    bay_big_screen.insert(0, str(f_num) + " % ")
    bay_small_screen.delete(0, len(bay_small_screen.get()))


# Function to display keys been pressed on the big and small screen in math
def show(number):
    current = bay_small_screen.get()
    current1 = bay_big_screen.get()
    bay_big_screen.delete(0, len(current1))
    bay_small_screen.delete(0, len(current))
    bay_small_screen.insert(0, str(current) + str(number))
    bay_big_screen.insert(0, str(current1) + str(number))


# Function for addition in math
def addition():
    first_num = bay_small_screen.get()
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    global sign
    sign = "addition"
    global f_num
    f_num = float(first_num)
    bay_big_screen.insert(0, str(f_num) + " + ")
    bay_small_screen.delete(0, len(bay_small_screen.get()))


# Function for subtraction in math
def subtraction():
    first_num = bay_small_screen.get()
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    global sign
    sign = "subtraction"
    global f_num
    f_num = float(first_num)
    bay_big_screen.insert(0, str(f_num) + " - ")
    bay_small_screen.delete(0, len(bay_small_screen.get()))


# Function for multiplication in math
def multiplication():
    first_num = bay_small_screen.get()
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    global sign
    sign = "multiplication"
    global f_num
    f_num = float(first_num)
    bay_big_screen.insert(0, str(f_num) + " * ")
    bay_small_screen.delete(0, len(bay_small_screen.get()))

# Function for division in math
def division():
    first_num = bay_small_screen.get()
    bay_big_screen.delete(0, len(bay_big_screen.get()))
    global sign
    sign = "division"
    global f_num
    f_num = float(first_num)
    bay_big_screen.insert(0, str(f_num) + " / ")
    bay_small_screen.delete(0, len(bay_small_screen.get()))


# Function to handle math expression when the = button is pressed
# This Function contains the control flow of all the operations that can be used in the calculator
def equal():
    try:
        second_num = bay_small_screen.get()
        bay_small_screen.delete(0, len(second_num))
        # bay_big_screen.insert(len(bay_big_screen.get()), second_num)

        if sign == "addition":
            result = f_num + float(second_num)
            bay_small_screen.insert(0, result)
            bay_big_screen.insert(len(bay_big_screen.get()), " = " + str(result))

        if sign == "subtraction":
            result = f_num - float(second_num)
            bay_small_screen.insert(0, result)
            bay_big_screen.insert(len(bay_big_screen.get()), " = " + str(result))

        if sign == "multiplication":
            result = f_num * float(second_num)
            bay_small_screen.insert(0, result)
            bay_big_screen.insert(len(bay_big_screen.get()), " = " + str(result))

        if sign == "division":
            if int(second_num) == 0:
                bay_small_screen.insert(0, "NaN")
                bay_big_screen.insert(len(bay_big_screen.get()), " = NaN")
            else:
                result = f_num / int(second_num)
                bay_small_screen.insert(0, result)
                bay_big_screen.insert(len(bay_big_screen.get()), " = " + str(result))

        if sign == "sin":
            # print(math.sin(num))
            result = math.sin(math.radians(num))
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "sin(" + str(num) + ") = " + str(result))

        if sign == "cos":
            result = math.cos(math.radians(num))
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "cos(" + str(num) + ") = " + str(result))

        if sign == "tan":
            result = math.tan(math.radians(num))
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "tan(" + str(num) + ") = " + str(result))

        if sign == "n_pow":
            result = float(f_num) ** int(second_num)
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, str(f_num) + " ^ " + str(second_num) + " = " + str(result))

        if sign == "exp":
            result = math.exp(num)
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "bay_small_screen" + num + " = " + str(result))

        if sign == "fact":
            result = math.factorial(num)
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, str(num) + "! = " + str(result))

        if sign == "sqrt":
            result = math.sqrt(num)
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "sqrt(" + str(num) + ") = " + str(result))

        if sign == "inv":
            result = 1 / num
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, str(num) + "^(-1) = " + str(result))

        if sign == "rem":
            result = f_num % int(second_num)
            bay_small_screen.insert(0, result)
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, str(f_num) + " % " + str(second_num) + " = " + str(result))

        if sign == "sin_inv":
            result = math.degrees(math.asin(num))
            bay_small_screen.insert(0, str(result) + " (degree)")
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "sin^-1(" + str(num) + ") = " + str(result))

        if sign == "cos_inv":
            result = math.degrees(math.acos(num))
            bay_small_screen.insert(0, str(result) + " (degree)")
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "cos^-1(" + str(num) + ") = " + str(result))

        if sign == "tan_inv":
            result = math.degrees(math.atan(num))
            bay_small_screen.insert(0, str(result) + " (degree)")
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, "tan^-1(" + str(num) + ") = " + str(result))

        if sign == "cube":
            result = num ** 3
            bay_small_screen.insert(0, str(result))
            bay_big_screen.delete(0, len(bay_big_screen.get()))
            bay_big_screen.insert(0, str(num) + "^3 = " + str(result))

    except Exception as ValueError:
        messagebox.showerror("Value Error", "Math Error")


# Function that handles the delete on the screen
def delete():
    current = bay_small_screen.get()
    # bay_small_screen.insert(0, current)
    bay_small_screen.delete(len(current) - 1, len(current))


# Function that empty the screen for fresh operation
def clear():
    bay_small_screen.delete(0, len(bay_small_screen.get()))
    bay_big_screen.delete(0, len(bay_big_screen.get()))


# Function that handles the build up of the calculator
# Contains all the structural code of the interface
def create_frame(mode):
    global frame

    try:
        frame.destroy()
    except:
        pass

    frame = tk.Label(root, background="sky blue")
    frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    global bay_small_screen
    global bay_big_screen
    bay_big_screen = tk.Entry(frame, font=("Helvetica", 9), width=40, borderwidth=2)
    bay_big_screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=3)

    bay_small_screen = tk.Entry(frame, font=("Helvetica", 9, "bold"), width=40, borderwidth=5)
    bay_small_screen.grid(row=1, column=0, columnspan=3, padx=10, pady=10, ipady=8)

    # Makes the small screen gain the focus once the application is lunched
    bay_small_screen.focus()

    # Statements that handles user mode switch
    if mode == 'basic':

        button_1 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="1", padx=35, pady=5,
                             command=lambda: show(1))
        button_2 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="2", padx=35, pady=5,
                             command=lambda: show(2))
        button_3 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="3", padx=35, pady=5,
                             command=lambda: show(3))
        button_4 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="4", padx=35, pady=5,
                             command=lambda: show(4))
        button_5 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="5", padx=35, pady=5,
                             command=lambda: show(5))
        button_6 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="6", padx=35, pady=5,
                             command=lambda: show(6))
        button_7 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="7", padx=35, pady=5,
                             command=lambda: show(7))
        button_8 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="8", padx=35, pady=5,
                             command=lambda: show(8))
        button_9 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="9", padx=35, pady=5,
                             command=lambda: show(9))
        button_0 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="0", padx=35, pady=5,
                             command=lambda: show(0))
        button_del = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="Del", padx=31,
                               pady=5, command=delete)

        button_add = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="+", padx=35, pady=5,
                               command=addition)
        button_clear = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="Clear", padx=77,
                                 pady=5, command=clear)
        button_equal = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="=", padx=89,
                                 pady=5, command=equal)
        button_dot = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text=".", padx=37, pady=5,
                               command=lambda: show("."))

        button_sqrt = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="sqrt", padx=27,
                                pady=5, command=sqrt)
        button_sub = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="-", padx=37, pady=5,
                               command=subtraction)
        button_mul = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="*", padx=37, pady=5,
                               command=multiplication)
        button_div = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="/", padx=37, pady=5,
                               command=division)

        button_1.grid(row=2, column=0, pady=5)
        button_2.grid(row=2, column=1, pady=5)
        button_3.grid(row=2, column=2, pady=5)
        button_4.grid(row=3, column=0, pady=5)
        button_5.grid(row=3, column=1, pady=5)
        button_6.grid(row=3, column=2, pady=5)
        button_7.grid(row=4, column=0, pady=5)
        button_8.grid(row=4, column=1, pady=5)
        button_9.grid(row=4, column=2, pady=5)
        button_0.grid(row=5, column=0, pady=5)

        button_sqrt.grid(row=6, column=0, pady=5)
        button_clear.grid(row=6, column=1, columnspan=2, pady=5)
        button_equal.grid(row=8, column=1, columnspan=2, pady=5)
        button_del.grid(row=5, column=2)
        button_dot.grid(row=5, column=1)

        button_add.grid(row=8, column=0)
        button_sub.grid(row=7, column=0, pady=5)
        button_mul.grid(row=7, column=1, pady=5)
        button_div.grid(row=7, column=2, pady=5)

    else:

        button_1 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="1", padx=35, pady=5,
                             command=lambda: show(1))
        button_2 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="2", padx=36, pady=5,
                             command=lambda: show(2))
        button_3 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="3", padx=35, pady=5,
                             command=lambda: show(3))
        button_4 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="4", padx=35, pady=5,
                             command=lambda: show(4))
        button_5 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="5", padx=36, pady=5,
                             command=lambda: show(5))
        button_6 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="6", padx=35, pady=5,
                             command=lambda: show(6))
        button_7 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="7", padx=35, pady=5,
                             command=lambda: show(7))
        button_8 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="8", padx=36, pady=5,
                             command=lambda: show(8))
        button_9 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="9", padx=35, pady=5,
                             command=lambda: show(9))
        button_0 = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="0", padx=35, pady=5,
                             command=lambda: show(0))

        button_add = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="+", padx=35, pady=5,
                               command=addition)
        button_clear = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="Del", padx=31,
                                 pady=5, command=delete)
        button_dot = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text=".", padx=37, pady=5,
                               command=lambda: show("."))
        button_equal = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="=", padx=89,
                                 pady=5, command=equal)

        button_sin = tk.Button(frame, background="light gray", padx=29, pady=5, font=("Helvetica", 9, "bold"),
                               text="sin", command=sin)
        button_cos = tk.Button(frame, background="light gray", padx=30, pady=5, font=("Helvetica", 9, "bold"),
                               text="cos", command=cos)
        button_tan = tk.Button(frame, background="light gray", padx=31, pady=5, font=("Helvetica", 9, "bold"),
                               text="tan", command=tan)
        button_cot = tk.Button(frame, background="light gray", padx=20, pady=5, font=("Helvetica", 9, "bold"),
                               text="sin^-1", command=sin_inv)
        button_cosec = tk.Button(frame, background="light gray", padx=21, pady=5, font=("Helvetica", 9, "bold"),
                                 text="cos^-1", command=cos_inv)
        button_sec = tk.Button(frame, background="light gray", padx=22, pady=5, font=("Helvetica", 9, "bold"),
                               text="tan^-1", command=tan_inv)
        button_fact = tk.Button(frame, background="light gray", padx=35, pady=5, font=("Helvetica", 9, "bold"),
                                text="X!", command=fact)
        button_sqrt = tk.Button(frame, background="light gray", padx=26, pady=5, font=("Helvetica", 9, "bold"),
                                text="sqrt", command=sqrt)
        button_exp = tk.Button(frame, background="light gray", padx=30, pady=5, font=("Helvetica", 9, "bold"),
                               text="exp", command=exp)
        button_cube = tk.Button(frame, background="light gray", padx=27, pady=5, font=("Helvetica", 9, "bold"),
                                text="X^3", command=cube)
        button_n_pow = tk.Button(frame, background="light gray", padx=30, pady=5, font=("Helvetica", 9, "bold"),
                                 text="X^n", command=n_pow)
        button_inv = tk.Button(frame, background="light gray", padx=27, pady=5, font=("Helvetica", 9, "bold"),
                               text="X^-1", command=inv)
        button_rem = tk.Button(frame, background="light gray", padx=26, pady=5, font=("Helvetica", 9, "bold"),
                               text="X%n", command=rem)
        button_e = tk.Button(frame, background="light gray", padx=78, pady=5, font=("Helvetica", 9, "bold"),
                             text="Clear", command=clear)

        button_sub = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="-", padx=37, pady=5,
                               command=subtraction)
        button_mul = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="*", padx=37, pady=5,
                               command=multiplication)
        button_div = tk.Button(frame, background="light gray", font=("Helvetica", 9, "bold"), text="/", padx=37, pady=5,
                               command=division)

        button_1.grid(row=7, column=0, pady=5)
        button_2.grid(row=7, column=1, pady=5)
        button_3.grid(row=7, column=2, pady=5)
        button_4.grid(row=8, column=0, pady=5)
        button_5.grid(row=8, column=1, pady=5)
        button_6.grid(row=8, column=2, pady=5)
        button_7.grid(row=9, column=0, pady=5)
        button_8.grid(row=9, column=1, pady=5)
        button_9.grid(row=9, column=2, pady=5)
        button_0.grid(row=10, column=0, pady=5)

        button_add.grid(row=11, column=0, pady=5)
        button_clear.grid(row=10, column=1, pady=5)
        button_dot.grid(row=10, column=2, pady=5)
        button_equal.grid(row=11, column=1, columnspan=2, pady=5)

        button_sub.grid(row=12, column=0, pady=5)
        button_mul.grid(row=12, column=1, pady=5)
        button_div.grid(row=12, column=2, pady=5)

        button_sin.grid(row=2, column=0, pady=5)
        button_cos.grid(row=2, column=1, pady=5)
        button_tan.grid(row=2, column=2, pady=5)
        button_cot.grid(row=3, column=0, pady=5)
        button_cosec.grid(row=3, column=1, pady=5)
        button_sec.grid(row=3, column=2, pady=5)
        button_sqrt.grid(row=4, column=0, pady=5)
        button_fact.grid(row=4, column=1, pady=5)
        button_inv.grid(row=4, column=2, pady=5)
        button_rem.grid(row=5, column=0, pady=5)
        button_n_pow.grid(row=5, column=1, pady=5)
        button_exp.grid(row=5, column=2, pady=5)
        button_cube.grid(row=6, column=0, pady=5)
        button_e.grid(row=6, column=1, columnspan=2, pady=5)

# Run only if the application is been run directly from this source code
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.configure(background="sky blue")

    """
    global frame
    frame = tk.Label(root)
    frame.grid(row=1, column=0, columnspan=2)
    """

    mode = tk.StringVar()
    tk.Radiobutton(root, background="light gray", variable=mode, font=("Helvetica", 9, "bold"), text="Scientific",
                   value="scientific").grid(row=0, column=0, padx=5, pady=5, ipadx=10)
    tk.Radiobutton(root, background="light gray", variable=mode, font=("Helvetica", 9, "bold"), text="Basic",
                   value="basic").grid(row=0, column=1, padx=5, pady=5, ipadx=10)

    choose_btn = tk.Button(root, background="light gray", width=10, font=("Helvetica", 9, "bold"), text="Switch",
                           command=lambda: create_frame(mode.get()))
    choose_btn.grid(row=0, column=2, padx=5, pady=5)

    # Start Application when triggered
    root.mainloop()

# End Of Code
