from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation  
   
# initializing a figure in  
# which the graph will be plotted 
fig = plt.figure()  
   
# marking the x-axis and y-axis 
axis = plt.axes(xlim =(0, 16),  
                ylim =(0, 8))  
  
# initializing a line variable 
line, = axis.plot([], [], lw = 3)  
   
# data which the line will  
# contain (x, y) 
def init():  
    line.set_data([], []) 
    return line, 
   
def animate(i): 
    x = np.linspace(0, 4, 1000)
   
    # plots a sine graph 
    y = 2 * x
    line.set_data(x, y) 
      
    return line, 
   
anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 200, blit = True) 
  
plt.show()


# anim.save('continuousSineWave.mp4',  
#           writer = 'ffmpeg', fps = 30) 