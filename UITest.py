from tkinter import *
import tkinter as tk
import os

win = Tk()
win.geometry("400x200")

radio = IntVar()
time_var = tk.StringVar()

choises = [("Seconds", 1),
           ("Minutes", 2),
           ("Hours", 3),]

def countdownSys():
    time = time_var.get()
    X = str(radio.get())

    if X == "1":
        os.system("shutdown /s /t "+time)
        print("PC will shutdown in", time, "Seconds")
    
    elif X == "2":
        time = int(time)*int(60)
        os.system("shutdown /s /t "+time)
        print("PC will shutdown in", time/60, "Minutes")

    elif X == "3":
        time = int(time)*int(3600)
        os.system("shutdown /s /t "+time)
        print("PC will shutdown in", time/3600, "Hours")

    else:
        print("Sum Ting Wong")

def abort():
    os.system("shutdown /a")
    print("Pc shutdown aborted")
    
    
label1 = tk.Label(win,
                  text="Shutdown pc in...",
                  font="montserrat 12 bold").pack()

time_ent = tk.Entry(win,
                    textvariable = time_var).pack()

r1 = Radiobutton(win,
                 text = "Seconds",
                 variable=radio,
                 font="montserrat 12 bold",
                 justify=tk.LEFT,
                 value=1).pack()

r2 = Radiobutton(win,
                 text = "Minutes",
                 variable=radio,
                 font="montserrat 12 bold",
                 justify=tk.LEFT,
                 value=2).pack()


r3 = Radiobutton(win,
                 text = "Hours",
                 variable=radio,
                 font="montserrat 12 bold",
                 justify=tk.LEFT,
                 value=3).pack()

sub_btn = tk.Button(win,
                    text="Submit",
                    font="montserrat 12 bold",
                    command = countdownSys).pack()

stp_btn = tk.Button(win,
                    text = 'Stop Shutdown',
                    background="red",
                    foreground="white",
                    font="montserrat 12 bold",
                    command = abort).pack()
mainloop()