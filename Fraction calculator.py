import tkinter as tk
from tkinter import messagebox
from fractions import Fraction


def convert_to_fraction(value):
    value = value.strip()
    if value == "":
        raise ValueError("Please enter a fraction.")

    try:
        return Fraction(value)
    except ZeroDivisionError:
        raise ValueError("Denominator cannot be zero.")
    except:
        raise ValueError("Invalid format! Use something like 3/4 or 2.")


def perform_operation(op):
    try:
        f1 = convert_to_fraction(fraction_input1.get())
        f2 = convert_to_fraction(fraction_input2.get())

        if op == "+":
            res = f1 + f2
        elif op == "-":
            res = f1 - f2
        elif op == "*":
            res = f1 * f2
        elif op == "/":
            if f2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            res = f1 / f2
        else:
            res = "?"

        result_box.config(text=f"{f1}  {op}  {f2}  =  {res}")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        result_box.config(text="")
def simplify_both():
    try:
        f1 = convert_to_fraction(fraction_input1.get())
        f2 = convert_to_fraction(fraction_input2.get())

        
        result_box.config(text=f"Simplified:   {f1}   and   {f2}")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        result_box.config(text="")



root = tk.Tk()
root.title("Fraction Calculator")
root.geometry("340x400")

main_area = tk.Frame(root, bd=2, relief="ridge", padx=10, pady=10)
main_area.pack(pady=15)

label1 = tk.Label(main_area, text="First Fraction", font=("Arial", 11))
label1.pack()
fraction_input1 = tk.Entry(main_area, width=22, font=("Arial", 12))
fraction_input1.pack(pady=5)

label2 = tk.Label(main_area, text="Second Fraction", font=("Arial", 11))
label2.pack()
fraction_input2 = tk.Entry(main_area, width=22, font=("Arial", 12))
fraction_input2.pack(pady=5)


btn_plus = tk.Button(main_area, text="+", width=12, command=lambda: perform_operation("+"))
btn_minus = tk.Button(main_area, text="-", width=12, command=lambda: perform_operation("-"))
btn_mul = tk.Button(main_area, text="×", width=12, command=lambda: perform_operation("*"))
btn_div = tk.Button(main_area, text="÷", width=12, command=lambda: perform_operation("/"))

btn_plus.pack(pady=3)
btn_minus.pack(pady=3)
btn_mul.pack(pady=3)
btn_div.pack(pady=3)


btn_simplify = tk.Button(main_area, text="Simplify Fractions", width=18, command=simplify_both)
btn_simplify.pack(pady=7)


result_box = tk.Label(root, text="", font=("Arial", 14))
result_box.pack(pady=10)

root.mainloop()