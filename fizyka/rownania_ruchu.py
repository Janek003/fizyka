import matplotlib.pyplot as plt
import matplotlib.animation as animation

print('jedyna dopuszczalna zmienna to "t", w postaci:\nA * i + B * j')

a = input('A: ')
b = input('B: ')

xpoints = []
ypoints = []

t = 0

while t <= 4:
    xpoints.append(eval(a))
    ypoints.append(eval(b))
    t+=0.1

plt.plot(xpoints, ypoints)
plt.show()