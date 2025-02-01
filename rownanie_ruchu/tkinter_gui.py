import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
from tkinter import ttk
import numpy
import math

def generate_animation(entries_a, entries_b, max_t_entry, ile_rownan):
    
    global lines, a_list, b_list
    
    a_list, b_list, max_t = read_user_input(entries_a, entries_b, max_t_entry)
    
    print(a_list, b_list)
    
    lines, fig = define_plot(max_t, a_list, b_list, ile_rownan)
    
    print(lines)
    
    plt.legend()
    plt.grid()

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = max_t*100, interval = max_t, blit = True)

    plt.show()

def read_user_input(entries_a, entries_b, max_t_entry):
    a_list = []
    b_list = []
    
    for entry_a in entries_a:
        if entry_a.get() != '': a_list.append(entry_a.get())
        else: a_list.append('0')
    
    for entry_b in entries_b:    
        if entry_b.get() != '': b_list.append(entry_b.get())
        else: b_list.append('0')

    try: max_t = int(max_t_entry.get())
    except: max_t = 4
    
    return a_list, b_list, max_t


def define_plot(max_t, a_list, b_list, ile_rownan):
    t = max_t

    x_skrajnosci = [0]
    y_skrajnosci = [0]

    for j in range(ile_rownan):
        x_skrajnosci.append(eval(a_list[j]))
        y_skrajnosci.append(eval(b_list[j]))

    x_min = min(x_skrajnosci)
    x_max = max(x_skrajnosci)

    y_min = min(y_skrajnosci)
    y_max = max(y_skrajnosci)


    fig = plt.figure()
    axis = plt.axes(xlim = (x_min, x_max), ylim = (y_min, y_max))
    
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")

    lines = []

    for j in range(ile_rownan):
        line, = axis.plot([], [], 'o', label = f'{a_list[j]} * i + {b_list[j]} * j')
        lines.append(line)
        
    return lines, fig
    
def init():
    
    for line in lines:
        line.set_data([], [])
        
    return lines

def animate(i):
    
    # t is a parameter which varies with the frame number 
    t = 0.01 * i

    # x, y values to be plotted 
    for j, line in enumerate(lines):
        x = eval(a_list[j])
        y = eval(b_list[j])
        
        line.set_data([x], [y])
    
    return lines


def len_gui():
    root = Tk()
    frm = ttk.Frame(root, padding=30)
    
    frm.grid()
    
    Label(frm, text='Ile rownan ruchu?', font=25).grid(row=0, column=0)
    ile_rownan_entry = Entry(frm, font=25, width=10)
    confirm_button = Button(frm, font=25, text='CONFIRM', command=lambda: main_gui(ile_rownan_entry.get()))
    
    ile_rownan_entry.grid(row=0, column=1)
    confirm_button.grid(row=0, column=2)
    
    root.mainloop()

def main_gui(ile_rownan_str):
    
    try: ile_rownan = int(ile_rownan_str)
    except: ile_rownan = 1
    
    root = Tk()
    frm = ttk.Frame(root, padding = 30)
    frm2 = ttk.Frame(root, padding = 30)

    frm.grid(row=0)
    frm2.grid(row=1)

    for i in range(ile_rownan): ttk.Label(frm, text=f'r{i+1}: ', font=25).grid(row=i, column=0)

    entries_a = [Entry(frm, font = 25) for _ in range(ile_rownan)]
    for i in range(ile_rownan): Label(frm,text = '* i + ', font = 25).grid(row = i, column = 2)

    entries_b = [Entry(frm, font = 25) for _ in range(ile_rownan)]
    for i in range(ile_rownan): Label(frm, text = '* j', font = 25).grid(row = i, column = 4)
    
    for i, entry in enumerate(entries_a):
        entry.grid(row=i, column=1)

    for i, entry in enumerate(entries_b):
        entry.grid(row=i, column=3)
    
    
    Label(frm2, text='Max t[s]: ', font = 25).grid(row=0,column=0)
    max_t_entry = Entry(frm2, font=25, width=5)
    max_t_entry.grid(row=0, column=1)
    
    button_generate = Button(frm2, font=25, text='generate', height = 2, width=50, bg='lightblue', command=lambda: generate_animation(entries_a, entries_b, max_t_entry, ile_rownan))
    button_generate.grid(row=2, rowspan=2, sticky=EW)
    
    root.mainloop()

len_gui()