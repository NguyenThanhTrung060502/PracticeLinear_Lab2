import matplotlib.pyplot as plt
import numpy as np 

def Oxy():
	# Draw the coordinate system Oxy
	Ox = list(range(-3, 4, 1))
	Oy = list(range(-3, 4, 1))
	plt.xticks(Ox, color='white')
	plt.yticks(Oy, color='white')
	plt.plot(Ox, [0] * len(Ox), color='black', linewidth=1)  # Axis Ox
	plt.plot([0] * len(Oy), Oy, color='black', linewidth=1)  # Axis Oy	
	plt.axis('equal')

def Figure_settings():
	# Title and labels 
	plt.xlabel('x', fontname='Times New Roman', fontsize=15, color='white')
	plt.ylabel('y', fontname='Times New Roman', fontsize=15, color='white')
	plt.title('Отображение, которое переводит круг единичной площади с центром в начале координат в круг площади 9.', fontname='Times New Roman', fontsize=12, color='pink')
	plt.grid(color = 'silver', linestyle = '--', linewidth = 0.5)

	# Set color for plt the outlines
	ax = plt.gca()

	# Set borders for the outlines (top, bottom, left, right)
	ax.spines['top'].set_visible(True)
	ax.spines['bottom'].set_visible(True)
	ax.spines['left'].set_visible(True)
	ax.spines['right'].set_visible(True)

	# Set color and thickness for the outlines
	ax.spines['top'].set_color('crimson')
	ax.spines['bottom'].set_color('crimson')
	ax.spines['left'].set_color('crimson')
	ax.spines['right'].set_color('crimson')

	# Set size for the outline
	ax.spines['top'].set_linewidth(2)
	ax.spines['bottom'].set_linewidth(2)
	ax.spines['left'].set_linewidth(2)
	ax.spines['right'].set_linewidth(2)

def Draw_vecto(vecto, color, vecto_name):
    ax.quiver(0, 0, vecto[0], vecto[1], angles='xy', scale_units='xy', scale=1, color=f'{color}', label=f'{vecto_name}')

    # Customize the limits of the x and y axis
    ax.set_xlim([0, max(vecto[0], 1)])  # Sets the x-axis limit from 0 to the x-value of the vector, or 1 if vector[0] <= 1
    ax.set_ylim([0, max(vecto[1], 1)])  # Sets the y-axis limit from 0 to the y-value of the vector, or 1 if vector[0] <= 1

    # Name the x and y axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
 
def Draw_a_circle(radius, color, Circle_Name):
    # Create data for the circle
    theta = np.linspace(0, 2*np.pi, 100)         # Create an array of angle values from 0 to 2*pi
    x = radius*np.cos(theta)                     # Calculate the x value corresponding to each angle value
    y = radius*np.sin(theta)                     # Calculate the y value corresponding to each angle value
    # Draw a circle
    plt.plot(x, y, color=f'{color}', linewidth=2, label=f'{Circle_Name}')

# Creates a drawing object and set size, background for figure 
fig, ax = plt.subplots(figsize=(10,7))
fig.set_facecolor('black')

# Define vector
vector_1 = [0, np.sqrt(1/(np.pi))]    # Radius vector of the unit circle
vector_2 = [0, 3*np.sqrt(1/(np.pi))]  # Radius vector of the received circle

# Draw related graphs
Draw_vecto(vector_2, 'lightgreen', 'Vecto_2')
Draw_vecto(vector_1, 'red', 'Vecto_1')
Oxy()
Figure_settings()
Draw_a_circle( np.sqrt(1/(np.pi)), 'red', 'Unit Circle')
Draw_a_circle(3*np.sqrt(1/(np.pi)), 'lightgreen', 'Received Circle')

# Show caption
plt.legend()

# Show graphs
plt.show()