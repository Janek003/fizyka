import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Create a figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)  # Make space for buttons below the plot

# Add grid for clarity
plt.grid()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Example with Multiple Buttons")

# Define button positions
button1_ax = plt.axes([0.1, 0.3, 0.2, 0.05])  # Button 1 at (x=0.1, y=0.3)
button2_ax = plt.axes([0.1, 0.2, 0.2, 0.05])  # Button 2 below Button 1
button3_ax = plt.axes([0.1, 0.1, 0.2, 0.05])  # Button 3 below Button 2

# Create buttons
button1 = Button(button1_ax, "Button 1")
button2 = Button(button2_ax, "Button 2")
button3 = Button(button3_ax, "Button 3")

# Define button actions
def on_button1_click(event):
    print("Button 1 clicked!")

def on_button2_click(event):
    print("Button 2 clicked!")

def on_button3_click(event):
    print("Button 3 clicked!")

# Attach actions to buttons
button1.on_clicked(on_button1_click)
button2.on_clicked(on_button2_click)
button3.on_clicked(on_button3_click)

# Show the plot
plt.show()
