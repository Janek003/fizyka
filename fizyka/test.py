import matplotlib.pyplot as plt

# Define the point (x, y)
x, y = 3, 7

# Plot the point
plt.plot(x, y, 'o', label=f'Point ({x}, {y})')

# Draw a vertical line from (x, y) to the x-axis
plt.vlines(x=x, ymin=0, ymax=y, colors='blue', linestyles='dashed', label='Vertical line to x-axis')

# Draw a horizontal line from (x, y) to the y-axis
plt.hlines(y=y, xmin=0, xmax=x, colors='red', linestyles='dashed', label='Horizontal line to y-axis')

# Label the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show plot
plt.grid(True)
plt.show()