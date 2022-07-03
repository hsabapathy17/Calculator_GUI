from tkinter import *
from tkinter import font as tkFont

screen_width = 640
screen_height = 265

def clear_screen():
    display.set("")

def print_data(key):
    if display.get() == "ERROR":
        display.set("")
    word = display.get() + key
    display.set(word)

def answer():
    try:
        answer = eval(display.get())
        display.set(answer)
    except:
        answer = "ERROR"
        display.set(answer)

window = Tk()
window.geometry("{}x{}".format(screen_width, screen_height))
window.title("Calculator")
window.resizable(0, 0) 

text_font = tkFont.Font(family='Times New Roman', size=23, weight=tkFont.BOLD)
display = StringVar()
display_area = Entry(window, width=46, bd=20, textvariable=display, justify="right", font=text_font, bg="grey")
display_area.grid(row=0, column=0, columnspan=4)

# Clear
clear = Button(window, text="CLEAR", width=50, font=text_font, bg="white", command=clear_screen)
clear.grid(row=1, column=0, padx=2, sticky=W, columnspan=4)

# Seven 
seven = Button(window, text="7", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("7"))
seven.grid(row=2, column=0)

# Eight 
eight = Button(window, text="8", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("8"))
eight.grid(row=2, column=1)

# Nine 
nine_btn = Button(window, text="9", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("9"))
nine_btn.grid(row=2, column=2)

# Divide 
divide = Button(window, text="/", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("/"))
divide.grid(row=2, column=3)

# Four 
four = Button(window, text="4", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("4"))
four.grid(row=3, column=0)

# Five 
five = Button(window, text="5", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("5"))
five.grid(row=3, column=1)

# Six 
six_btn = Button(window, text="6", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("6"))
six_btn.grid(row=3, column=2)

# Multiplication
mult = Button(window, text="*", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("*"))
mult.grid(row=3, column=3)

# One 
one_btn = Button(window, text="1", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("1"))
one_btn.grid(row=4, column=0)

# Two 
two = Button(window, text="2", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("2"))
two.grid(row=4, column=1)

# Three
three = Button(window, text="3", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("3"))
three.grid(row=4, column=2)

# Minus
minus = Button(window, text="-", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("-"))
minus.grid(row=4, column=3)

# Decimal Point
decimalPoint = Button(window, text=".", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("."))
decimalPoint.grid(row=5, column=0)

# Zero
zero = Button(window, text="0", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("0"))
zero.grid(row=5, column=1)

# Equal
equal = Button(window, text="=", width=10, bg="white", fg="black", font=text_font, command=answer)
equal.grid(row=5, column=2)

# Addition
plus = Button(window, text="+", width=10, font=text_font, bg="white", fg="black", command=lambda: print_data("+"))
plus.grid(row=5, column=3)

window.mainloop()
