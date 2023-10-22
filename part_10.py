import matplotlib.pyplot as plt
import numpy as np 

def Oxy():
	# Draw the coordinate system Oxy
	Ox = list(range(-4, 5, 1))
	Oy = list(range(-4, 5, 1))
	plt.xticks(Ox, color='white')
	plt.yticks(Oy, color='white')
	plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # Axis Ox
	plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # Axis Oy	
	plt.axis('equal')

def Figure_settings():
	# Title and labels 
	plt.xlabel('x', fontname='Times New Roman', fontsize=15, color='white')
	plt.ylabel('y', fontname='Times New Roman', fontsize=15, color='white')
	plt.title('Отображение, которое переводит круг единичной площади с центром в начале координат в круг площади 6.', fontname='Times New Roman', fontsize=12, color='pink')
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
    ax.quiver(0, 0, vecto[0], vecto[1], angles='xy', scale_units='xy', scale=1, color=f'{color}', label=f'{vecto_name}', width=0.004, headwidth=2, headaxislength=3, headlength=4)

    # Customize the limits of the x and y axis
    ax.set_xlim([0, max(vecto[0], 1)])  # Sets the x-axis limit from 0 to the x-value of the vector, or 1 if vector[0] <= 1
    ax.set_ylim([0, max(vecto[1], 1)])  # Sets the y-axis limit from 0 to the y-value of the vector, or 1 if vector[0] <= 1

    # Name the x and y axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

def Draw_a_circle(radius, color, Circle_Name, a, b, c, points_circle_x, points_circle_y):
    # Create data for the circle
    theta = np.linspace(0, 2*np.pi, 100)         # Create an array of angle values from 0 to 2*pi
    x = radius*np.cos(theta)                     # Calculate the x value corresponding to each angle value
    y = radius*np.sin(theta)                     # Calculate the y value corresponding to each angle value
    # Draw a circle
    plt.plot(x, y, color=f'{color}', linewidth=1.5, label=f'{Circle_Name}')
    
    plt.text(points_circle_x[0], points_circle_y[0], f'{a}', ha='right' , va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=12)
    plt.text(points_circle_x[1], points_circle_y[1], f'{b}', ha='right' , va='top'   , color=f'{color}', fontname='Times New Roman', fontsize=12)
    plt.text(points_circle_x[2], points_circle_y[2], f'{c}', ha='center', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=12)
    
def Draw_triangle(triangle_x, triangle_y, a, b, c, Triangle_name, color, color_vertex):
	plt.fill(triangle_x, triangle_y, color=f'{color}', alpha=0.5, label=f'{Triangle_name}')
	plt.plot(triangle_x, triangle_y, marker='o', ms=3, color=f'{color}', linestyle="")
	
	plt.text(triangle_x[0], triangle_y[0], f'{a}', ha='right' , va='bottom', color=f'{color_vertex}', fontname='Times New Roman', fontsize=15)
	plt.text(triangle_x[1], triangle_y[1], f'{b}', ha='right' , va='top'   , color=f'{color_vertex}', fontname='Times New Roman', fontsize=15)
	plt.text(triangle_x[2], triangle_y[2], f'{c}', ha='center', va='bottom', color=f'{color_vertex}', fontname='Times New Roman', fontsize=15)


# Creates a drawing object and set size, background for figure 
fig, ax = plt.subplots(figsize=(10,7))
fig.set_facecolor('black')

# Define vector
vector_radius_1 = [0, np.sqrt(1/np.pi)]    # Vector OA
vector_radius_2 = [0, -np.sqrt(1/np.pi)]   # Vector OB
vector_radius_3 = [np.sqrt(1/np.pi), 0]    # Vector OC

vector_1 = [0, np.sqrt(2*np.sqrt(3))]       # Vector OA' 
vector_2 = [0, -np.sqrt(2*np.sqrt(3))]      # Vector OB' 
vector_3 = [np.sqrt((11*np.sqrt(3))/2), 0]  # Vector OC' 


# Coordinates of any 3 vertices of the circle
points_circle_x = [0, 0, np.sqrt(1/np.pi)]
points_circle_y = [np.sqrt(1/np.pi), -np.sqrt(1/np.pi), 0]

# Coordinates of 3 points on the circle after transformation
received_points_x = [0, 0, np.sqrt((11*np.sqrt(3))/2)]
received_points_y = [np.sqrt(2*np.sqrt(3)), -np.sqrt(2*np.sqrt(3)), 0]

# Draw vectors
Draw_vecto(vector_1, 'green', "Vecto OA'")
Draw_vecto(vector_2, 'green', "Vecto OB'")
Draw_vecto(vector_3, 'green', "Vecto OC'")
Draw_vecto(vector_radius_1, 'tomato', 'Vecto OA')
Draw_vecto(vector_radius_2, 'tomato', 'Vecto OB')
Draw_vecto(vector_radius_3, 'tomato', 'Vecto OC')

# Draw related graphs
Oxy()
Figure_settings()
Draw_a_circle(np.sqrt(1/np.pi), 'red', 'Unit Circle', 'A', 'B', 'C', points_circle_x, points_circle_y)
Draw_triangle(received_points_x, received_points_y, "A'", "B'", "C'", 'Triangle received', 'lightgreen', 'green')

# Show caption
plt.legend()

# Show graphs
plt.show()