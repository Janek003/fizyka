import matplotlib.pyplot as plt
import matplotlib.animation as animation


a_list = []
b_list = []

line_num = int(input("Ile rownan ruchu? [max 5]: "))
while line_num > 5:
    line_num = int(input("Podales za duza ilosc rownan, Ile rownan ruchu? [max 5]: "))

max_t = int(input("Max t: "))

print('--------------------\njedyna dopuszczalna zmienna to "t", rownanie w postaci:\nA * i + B * j\n')
for j in range(line_num):
    
    a = input(f'A{j}: ')
    a_list.append(a)

    b = input(f'B{j}: ')
    b_list.append(b)

    print()

t = max_t

x_skrajnosci = [0]
y_skrajnosci = [0]

for j in range(line_num):
    x_skrajnosci.append(eval(a_list[j]))
    y_skrajnosci.append(eval(b_list[j]))

x_min = min(x_skrajnosci)
x_max = max(x_skrajnosci)

y_min = min(y_skrajnosci)
y_max = max(y_skrajnosci)


fig = plt.figure()
axis = plt.axes(xlim = (x_min, x_max), ylim = (y_min, y_max)) 

lines = [] 
colors = ['blue', 'red', 'green', 'purple', 'black']

for j in range(line_num):
    line, = axis.plot([], [], 'o', color = colors[j])
    lines.append(line)

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

anim = animation.FuncAnimation(fig, animate, init_func = init, frames = max_t*100, interval = max_t, blit = True) 

plt.show()