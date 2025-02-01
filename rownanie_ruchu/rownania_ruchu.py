import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

print('jedyna dopuszczalna zmienna to "t", zapisz w postaci:\nA * i + B * j')

a = input('A: ')
b = input('B: ')

xpoints = []
ypoints = []

t = 0

while t <= 4:
    xpoints.append(eval(a))
    ypoints.append(eval(b))
    t+=0.1

plt.plot(xpoints, ypoints,'o')
plt.show()