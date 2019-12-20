import tkinter as tk
from tkinter import ttk as tkk
import TM

def get_tape():

    tape = []
    while True:
        str = in_tape.get()
        if str != "":
            break
        else:
            return ["B"]
    #str = input("Tape: ")
    for i in str:
        tape.append(i)

    return tape

def choose_tm():

    t = combo.get()[0]
    path = "rules/TM_" + t + ".txt"
    r = TM.read_rules(path)

    return r

def runTM():

    r = choose_tm()
    t = get_tape()
    machine = TM.TM(rules = r, input_tape = t, algorithm = combo.get()[1:])
    temp = machine.run()

    if temp != "":
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.geometry("250x150")

        if temp == "ExcInvMov":
            error_lb = tk.Label(error_window, text = "Invalid Movement", font = ("Arial", 15))
        elif temp == "ExcNonSta":
            error_lb = tk.Label(error_window, text = "No Final State Reached", font = ("Arial", 15))

        error_lb.grid(column = 3, row = 5)
        return False

    return True


def clicked_run():

    temp = runTM()
    if temp == False:
        return

    f=open("tape.txt", "r")
    contents =f.read()

    run = tk.Tk()
    run.title("Result")
    run.geometry("600x400")
    T = tk.Text(run, height=100, width=200)
    T.pack()
    T.insert(tk.END, "{}".format(contents))
    S = tk.Scrollbar(run)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    #tk.lbl.configure(text="Button was clicked !!")
    return

# Window Properties
window = tk.Tk()
window.title("Turing Machine")
title = tk.Label(window, text = "Turing Machine", font = ("Arial", 25))
title.grid(column = 1, row = 1)

# Run Button
btn_start = tk.Button(window, text = "Run TM", command = clicked_run)
btn_start.grid(column = 1, row = 6)

# Tape Input
lb1 = tk.Label(window, text = "Tape: ", font = ("Arial", 15))
lb1.grid(column = 0, row = 5)
in_tape = tk.Entry(window,width=20)
in_tape.grid(column = 1, row = 5)

# Algorithm Selection
lb2 = tk.Label(window, text = "Select TM: ", font = ("Arial", 15))
lb2.grid(column = 0, row = 4)
combo = tkk.Combobox(window)
combo['values']= ("Select TM...",
                  "1 (a+b)(b)(a+b)*",
                  "2 (a^n)(c^n)",
                  "3 Palindrome",
                  "4 Even-Even",
                  "5 All strings with 'aa' somewhere",
                  "6 (a^n)(b^n)(a^n)",
                  "7 Insert",
                  "8 Delete")
combo.current(0) #set the selected item
combo.grid(column = 1, row = 4)

# Window Properties
window.geometry('400x200')
window.mainloop()
