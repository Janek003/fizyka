import matplotlib.animation as animation 
import matplotlib.pyplot as plt 


# creating a blank window for the animation 
fig = plt.figure() 
axis = plt.axes(xlim =(0,16), ylim =(0, 8)) 

line, = axis.plot([], [], 'o')

# what will our line dataset 
# contain? 
def init(): 
	line.set_data([], []) 
	return line, 

def animate(i):
	
    # t is a parameter which varies with the frame number 
	t = 0.01 * i
	
	# x, y values to be plotted 
	x = t**2
	y = 2 * t
	
	line.set_data(x, y) 
	
	return line,

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 400, interval = 4, blit = True) 

plt.show()