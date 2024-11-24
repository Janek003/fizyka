import matplotlib.pyplot as plt
from matplotlib.widgets import *
import matplotlib.animation as animation
from numpy import *
from math import ceil
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

g = 9.81
cel_h = 30
gun_h = 30
gun_v0 = 2

s = sqrt(100 / g)
fps = 100

frames = ceil(fps*s)
multiplier = 1/fps
interval = 1/fps*1000


fig = plt.figure()
axis = plt.axes(xlim = (0, 120), ylim = (0, 100))
plt.xlabel("x[m]")
plt.ylabel("y[m]")


plt.subplots_adjust(left=0.15, bottom=0.45)

slider_ax1 = plt.axes([0.1, 0.3, 0.3, 0.03])
v0_slider = Slider(slider_ax1, 'v0', 0, 70,valstep=1, valinit=30)

slider_ax2 = plt.axes([0.1, 0.2, 0.3, 0.03])
gun_h_slider = Slider(slider_ax2, 'gun_h', 0, 50,valstep=1, valinit=15)

slider_ax3 = plt.axes([0.1, 0.1, 0.3, 0.03])
cel_h_slider = Slider(slider_ax3, 'cel_h', 0, 50,valstep=1, valinit=45)

slider_ax4 = plt.axes([0.5, 0.3, 0.3, 0.03])
kat_slider = Slider(slider_ax4, 'kat', 0, 90,valstep=1, valinit=70)

button_ax = plt.axes([0.8, 0.05, 0.05, 0.04])
launch_button = Button(button_ax, 'Odswierz')

lines = []
for i in range(2):
    line, = axis.plot([], [], 'o')
    lines.append(line)

def check_collison(x,y,bx,by):
    odleglosc = sqrt((x - bx)**2 + (y - by)**2)
    if x > 0 and y > 0 and bx > 0 and by > 0:
        if odleglosc < 3: return True

def init():
    lines[0].set_data([], [])
    lines[1].set_data([], [])
    return lines

def animate(i):
	
    t = i*multiplier

    x = v0x*t
    y = gun_h + v0y*t - (g/2)*(t**2)

    bx = 100
    by = cel_h - (g/2)*(t**2)

    if check_collison(x,y,bx,by):
        messagebox.showinfo("Zwyciestwo", "trafiles spadajacy obiekt i wygrales!")
        root.quit()
        

    lines[0].set_data([x], [y])
    lines[1].set_data([bx], [by])

    return lines

def start_an(event=None):
    global gun_v0, gun_h, cel_h, v0y, v0x
    gun_v0 = v0_slider.val
    gun_h = gun_h_slider.val
    cel_h = cel_h_slider.val
    kat = kat_slider.val
    v0x = gun_v0*cos(radians(kat))
    v0y = gun_v0*sin(radians(kat))

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = frames, interval = interval, blit = True, repeat_delay = 0)
    
    plt.grid()
    plt.show()

launch_button.on_clicked(start_an)

start_an()