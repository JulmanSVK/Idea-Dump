from tkinter import *
import tkinter as tk
import os
from sys import platform

print(platform)

win = Tk()
win.geometry("300x175")

radio = IntVar()
time_var = tk.StringVar()

def abort():
    if platform == "win32":
        os.system("shutdown /a")
    elif platform == "linux" or platform == "linux2":
        os.system("sudo shutdown -c")
    elif platform == "darwin":
        os.system()
    print("Pc shutdown aborted")

def main():
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
        print("Niečo sa podrbalo")

nadpis = tk.Label(win,text="Vypnutie PC",font="bold").pack()
time_ent = tk.Entry(win,textvariable = time_var).pack()

if platform != "linux" or platform != "linux2":
    r1 = Radiobutton(win, text = "Seconds", variable=radio, value=1).pack()
r2 = Radiobutton(win, text = "Minutes", variable=radio, value=2).pack()
r3 = Radiobutton(win, text = "Hours", variable=radio, value=3).pack()
sep = tk.Separator(win)
sub_btn = tk.Button(win,text = 'Submit', command = main).pack(side=RIGHT,padx=20)
stp_btn = tk.Button(win,text = 'Stop Shutdown', command = abort, fg="white",bg="red").pack(side=LEFT,padx=20)
mainloop()