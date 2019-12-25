#imports
from tkinter import *
import tempfile
import os
import math

#creating root
root = Tk()
root.title("Calc")
root.maxsize(318, 396)
root.minsize(318, 396)
dir_path = os.path.dirname(os.path.realpath(__file__)) #finding directory
ver = "1.10" #version
#images
photo = PhotoImage(file = dir_path + "/Calc.png")
root.iconphoto(True, photo)
img = PhotoImage(file = dir_path + "/rounded_button.png")
img_num = PhotoImage(file = dir_path + "/rounded_button_num.png")

#functions
def button_click(num): #writing numbers to entry box
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear(): #clearing entry box
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global func
    global f_num
    func = "add"
    f_num = float(first_number)
    e.delete(0, END)

def button_minus():
    first_number = e.get()
    global f_num
    global func
    func = "minus"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global func
    func = "divide"
    f_num = float(first_number)
    e.delete(0, END)

def button_times():
    first_number = e.get()
    global f_num
    global func
    func = "times"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal(): #finds the answer
    second_number = e.get()
    e.delete(0, END)

    if func == "add":
        e.insert(0, f_num + float(second_number))

    if func == "minus":
        e.insert(0, f_num - float(second_number))

    if func == "divide":
        if float(second_number) == 0:
            e.insert(0, "∞")

        else:
            e.insert(0, f_num / float(second_number))

    if func == "times":
        e.insert(0, f_num * float(second_number))

def square(): #squares number
    div = float(e.get())
    dived = div * div
    e.delete(0, END)
    e.insert(0, dived)

def rooting(): #square roots number
    div = math.sqrt(float(e.get()))
    e.delete(0, END)
    e.insert(0, div)

#creating widgets
frame = LabelFrame(root, text = "Version: " + str(ver))
e = Entry(frame, width = 35, borderwidth = 3)
button_1 = Button(frame, text = "1", padx = 0, pady = 0, command = lambda: button_click(1))
button_2 = Button(frame, text = "2", padx = 0, pady = 0, command = lambda: button_click(2))
button_3 = Button(frame, text = "3", padx = 0, pady = 0, command = lambda: button_click(3))
button_4 = Button(frame, text = "4", padx = 0, pady = 0, command = lambda: button_click(4))
button_5 = Button(frame, text = "5", padx = 0, pady = 0, command = lambda: button_click(5))
button_6 = Button(frame, text = "6", padx = 0, pady = 0, command = lambda: button_click(6))
button_7 = Button(frame, text = "7", padx = 0, pady = 0, command = lambda: button_click(7))
button_8 = Button(frame, text = "8", padx = 0, pady = 0, command = lambda: button_click(8))
button_9 = Button(frame, text = "9", padx = 0, pady = 0, command = lambda: button_click(9))
button_0 = Button(frame, text = "0", padx = 0, pady = 0, command = lambda: button_click(0))
button_equal = Button(frame, text = "=", padx = 0, pady = 0, command = button_equal)
button_clear = Button(frame, text = "C", padx = 0, pady = 0, command = button_clear)
button_add = Button(frame, text = "+", padx = 0, pady = 0, command = button_add)
button_minus = Button(frame, text = "-", padx = 0, pady = 0, command = button_minus)
button_divide = Button(frame, text = "/", padx = 0, pady = 0, command = button_divide)
button_times = Button(frame, text = "*", padx = 0, pady = 0, command = button_times)
button_square = Button(frame, text = "x²", padx = 0, pady = 0, command = square)
button_root = Button(frame, text = "√", padx = 0, pady = 0, command = rooting)

#coustom buttons
button_1.config(image = img_num, compound = CENTER, relief = FLAT)
button_2.config(image = img_num, compound = CENTER, relief = FLAT)
button_3.config(image = img_num, compound = CENTER, relief = FLAT)
button_4.config(image = img_num, compound = CENTER, relief = FLAT)
button_5.config(image = img_num, compound = CENTER, relief = FLAT)
button_6.config(image = img_num, compound = CENTER, relief = FLAT)
button_7.config(image = img_num, compound = CENTER, relief = FLAT)
button_8.config(image = img_num, compound = CENTER, relief = FLAT)
button_9.config(image = img_num, compound = CENTER, relief = FLAT)
button_0.config(image = img_num, compound = CENTER, relief = FLAT)
button_clear.config(image = img, compound = CENTER, relief = FLAT)
button_equal.config(image = img, compound = CENTER, relief = FLAT)
button_add.config(image = img, compound = CENTER, relief = FLAT)
button_minus.config(image = img, compound = CENTER, relief = FLAT)
button_divide.config(image = img, compound = CENTER, relief = FLAT)
button_times.config(image = img, compound = CENTER, relief = FLAT)
button_square.config(image = img, compound = CENTER, relief = FLAT)
button_root.config(image = img, compound = CENTER, relief = FLAT)

#puts widgets in window
frame.grid(row = 0, column = 0, padx = 2, pady = 2)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)
button_0.grid(row = 4,column = 0)
button_clear.grid(row = 6,column = 0)
button_equal.grid(row = 5,column = 2)
button_add.grid(row = 4,column = 1)
button_minus.grid(row = 4,column = 2)
button_divide.grid(row = 5,column = 1)
button_times.grid(row = 5,column = 0)
button_square.grid(row = 6,column = 1)
button_root.grid(row = 6,column = 2)

root.mainloop()
