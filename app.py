import tkinter as tk

def button_click(number):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current + str(number))

def button_clear():
    screen.delete(0, tk.END)

def button_equal():
    try:
        current = screen.get()
        result = eval(current)
        screen.delete(0, tk.END)
        screen.insert(0, str(result))
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

screen = tk.Entry(root, width=20, font=("Arial", 20))
screen.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 20), bg="gray",
                       command=lambda t=text: button_click(t) if t != "=" else button_equal())
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 20), bg="gray", command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
