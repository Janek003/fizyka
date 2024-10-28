import matplotlib.pyplot as plt
import matplotlib.animation as animation


a_list = []
b_list = []

line_num = int(input("Ile rownan ruchu? [max 5]: "))
while line_num > 5:
    line_num = int(input("Podales za duza ilosc rownan, Ile rownan ruchu? [max 5]: "))
      
print('--------------------\njedyna dopuszczalna zmienna to "t", rownanie w postaci:\nA * i + B * j\n')
for j in range(line_num):
    
    a = input(f'A{j}: ')
    a_list.append(a)

    b = input(f'B{j}: ')
    b_list.append(b)

    print()


# creating a blank window for the animation 
fig = plt.figure() 
axis = plt.axes(xlim =(0,16), ylim =(0, 8)) 

lines = [] 
colors = ['blue', 'red', 'green', 'purple', 'black']

for j in range(line_num):
    line, = axis.plot([], [], 'o', color = colors[j])
    lines.append(line)

# what will our line dataset 
# contain? 
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
        line.set_data(x, y)

    return lines

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 400, interval = 4, blit = True) 

plt.show()