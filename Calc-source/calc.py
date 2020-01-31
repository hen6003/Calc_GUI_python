# imports
from tkinter import * # tkinter
import tempfile
import os
import math # for math operations

# creating root
root = Tk()
root.title("Calc")
root.minsize(306, 390)
root.maxsize(306, 390)
dir_path = os.path.dirname(os.path.realpath(__file__)) # finding directory
ver = "2.0" # version
root.option_add('*font', ('comforta', 9, 'bold'))
# images
photo = PhotoImage(file = dir_path + "/Calc.png")
settingicon = PhotoImage(file = dir_path + "/settings.png")
root.iconphoto(True, photo)
img = PhotoImage(file = dir_path + "/rounded_button.png")
img_num = PhotoImage(file = dir_path + "/rounded_button_num.png")

setting = Frame(root)

# functions
def button_click(num): # writing numbers to entry box
    current = e.cget("text")
    e.config(text = str(current) + str(num))

def button_clear(): # clearing entry box
    e.config(text = "")

def button_add():
    first_number = e.cget("text")
    global func
    global f_num
    func = "add"
    f_num = float(first_number)
    e.config(text = "")

def button_minus():
    first_number = e.cget("text")
    global f_num
    global func
    func = "minus"
    f_num = float(first_number)
    e.config(text = "")

def button_divide():
    first_number = e.cget("text")
    global f_num
    global func
    func = "divide"
    f_num = float(first_number)
    e.config(text = "")

def button_times():
    first_number = e.cget("text")
    global f_num
    global func
    func = "times"
    f_num = float(first_number)
    e.config(text = "")

def button_equal(): # finds the answer
    second_number = e.cget("text")
    e.config(text = "")

    if func == "add":
        e.config(text = f"{f_num + float(second_number):g}")

    if func == "minus":
        e.config(text = f"{f_num - float(second_number):g}")

    if func == "divide":
        if float(second_number) == 0:
            e.config(text = "inf")

        else:
            e.config(text = f"{f_num / float(second_number):g}")

    if func == "times":
        e.config(text = f"{f_num * float(second_number):g}")

def square(): # squares number
    div = float(e.cget("text"))
    dived = div * div
    e.config(text = "")
    e.config(text = f"{dived:g}")

def rooting(): # square roots number
    div = math.sqrt(float(e.cget("text")))
    e.config(text = "")
    e.config(text = f"{div:g}")

def settings():
    def save(): # saving fuction
        if optionVar.get() == "Left     ":
            e.config(anchor = W)

        else:
            e.config(anchor = N)

    # creating Settings menu
    set = Toplevel(root)
    set.title("Settings")
    set.minsize(180, 122)
    set.maxsize(180, 122)
    set.title("Settings")
    set.iconphoto(True, settingicon)

    # creating widgets
    descanch = Label(set, relief = FLAT, text = "Text Anchor")
    version = Label(set, text = "Version: " + str(ver))
    setting = Button(set, image = settingicon, relief = FLAT, text = "\n\nSave", compound = CENTER, pady = 0, anchor = N, command = save)
    maker = Label(set, text = "Made By Henry Smith")
    optionVar = StringVar()

    if e.cget("anchor") == W:
        optionVar.set("Left     ")

    else:
        optionVar.set("Middle")

    option = OptionMenu(set, optionVar, "Middle", "Left     ")

    # puts widgets in window
    maker.grid(row = 0, column = 0, columnspan = 2)
    version.grid(row = 1, column = 0, columnspan = 2)
    option.grid(row = 2, column = 1)
    descanch.grid(row = 2, column = 0)
    setting.grid(row = 3, column = 0, columnspan = 2)

# creating widgets
e = Label(root, relief = GROOVE, width = 35, bg = "grey")
setting = Button(root, image = settingicon, relief = FLAT, command = settings)
button_1 = Button(root, text = "1", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 0, pady = 0, image = img_num, compound = CENTER, relief = FLAT, command = lambda: button_click(0))
button_equal = Button(root, text = "=", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = button_equal)
button_clear = Button(root, text = "C", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = button_clear)
button_add = Button(root, text = "+", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = button_add)
button_minus = Button(root, text = "-", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = button_minus)
button_divide = Button(root, text = "÷", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = button_divide)
button_times = Button(root, text = "X", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = button_times)
button_square = Button(root, text = "a²", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = square)
button_root = Button(root, text = "√", padx = 0, pady = 0, image = img, compound = CENTER, relief = FLAT, command = rooting)

# puts widgets in window
setting.grid(row = 7, column = 0, columnspan = 3)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
button_1.grid(row = 1,column = 0)
button_2.grid(row = 1,column = 1)
button_3.grid(row = 1,column = 2)
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_7.grid(row = 3,column = 0)
button_8.grid(row = 3,column = 1)
button_9.grid(row = 3,column = 2)
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
