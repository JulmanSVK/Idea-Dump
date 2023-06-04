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
        print("Sum Ting Wong")
        
def abort():
    os.system("shutdown /a")
    print("Pc shutdown aborted")
          
label1 = tk.Label(win,
                  text="Shutdown pc in...",
                  font="montserrat 12 bold").pack()

time_ent = tk.Entry(win,
                    font="montserrat 12",
                    textvariable = time_var).pack()

midframe = tk.Frame(win).pack()
botframe = tk.Frame(win).pack(side=BOTTOM)

r1 = Radiobutton(midframe,
                 text = "Seconds",
                 variable=radio,
                 font="montserrat 12 bold",
                 value=1).pack(side=LEFT)

r2 = Radiobutton(midframe,
                 text = "Minutes",
                 variable=radio,
                 font="montserrat 12 bold",
                 value=2).pack(side=LEFT)


r3 = Radiobutton(midframe,
                 text = "Hours",
                 variable=radio,
                 font="montserrat 12 bold",
                 value=3).pack(side=LEFT)

sub_btn = tk.Button(botframe,
                    text="Shutdown PC",
                    font="montserrat 12 bold",
                    command = countdownSys).pack(side=BOTTOM)

stp_btn = tk.Button(botframe,
                    text = 'Stop Shutdown',
                    background="red",
                    foreground="white",
                    font="montserrat 12 bold",
                    command = abort).pack(side=BOTTOM)
mainloop()