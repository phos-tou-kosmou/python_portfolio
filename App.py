#!/bin/python3

import tkinter as tk
import uuid

master = tk.Tk()

a = {}

def scroll_out(x, y):
    for i in range(0, x):
        tk.Label(master).grid(row=i)
        key = uuid.uuid1()
        value = tk.Entry(master)
        a[i] = value     

    for i, val in enumerate(a):
        print(a[i].grid(row=i, column=1))
        if i == len(a): break

we = tk.Entry(master)
le = tk.Entry(master)
w = int(we.get())
l = int(le.get())
w.set(0)
l.set(0)

matrix_button = tk.Button(master, text = "Submit", command = scroll_out(w, l))
matrix_button.grid(row = 2, column = 1)

master.mainloop()
