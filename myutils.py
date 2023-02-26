from tkinter import *


def add_win(n, win1, win2, txt):
    n.add(win1, text=txt)
    n.hide(win2)


def display_label(win, txt, color, font_size, x, y):
    Label(win, text=txt, font=("Times 18", font_size, "bold"), bg="light blue", fg=color).place(x=x, y=y)


def clear(event, entry):
    entry.delete(0, END)
