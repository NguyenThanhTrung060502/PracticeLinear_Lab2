import matplotlib.pyplot as plt
import numpy as np

def Oxy():
	# Draw the coordinate system Oxy
	Ox = list(range(-20, 21, 1))
	Oy = list(range(-20, 21, 1))
	plt.xticks(Ox, color='white')
	plt.yticks(Oy, color='white')
	plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # Axis Ox
	plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # Axis Oy	
	# This function is used to adjust so that the units of the Ox and Oy axes are equal 
	plt.axis('equal')

def Figure_settings():
	# Title and labels 
	plt.xlabel('x', fontname='Times New Roman', fontsize=15, color='white')
	plt.ylabel('y', fontname='Times New Roman', fontsize=15, color='white')
	plt.title('Отражение (симметрию) плоскости относительно прямой y = 2x', fontname='Times New Roman', fontsize=15, color='pink')
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
 
def Draw_triangle(triangle_x, triangle_y, a, b, c, Triangle_name, color):
	plt.fill(triangle_x, triangle_y, color=f'{color}', alpha=0.5, label=f'{Triangle_name}')
	plt.plot(triangle_x, triangle_y, marker='o', color=f'{color}', linestyle="")
	
	plt.text(triangle_x[0], triangle_y[0], f'{a}', ha='right', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=15)
	plt.text(triangle_x[1], triangle_y[1], f'{b}', ha='right', va='top', color=f'{color}', fontname='Times New Roman', fontsize=15)
	plt.text(triangle_x[2], triangle_y[2], f'{c}', ha='center', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=15)
	
def Draw_Eigenvector(vecto, color, vecto_name):
    ax.quiver(0, 0, vecto[0], vecto[1], angles='xy', scale_units='xy', scale=1, color=f'{color}', label=f'{vecto_name}', width=0.004, headwidth=2, headaxislength=3, headlength=4)
    
    # Customize the limits of the x and y axis
    ax.set_xlim([0, max(vecto[0], 1)])
    ax.set_ylim([0, max(vecto[0], 1)])
    
    # Name the x and y axesa
    ax.set_xlabel('X')
    ax.set_ylabel('Y')


# Set size and set background for figure
fig, ax = plt.subplots(figsize=(10,7))
fig.set_facecolor('black')

# Original triangle 
triangle_1_x = [5, 4, 10]
triangle_1_y = [-5, 3, 5]

# Triangle received
triangle_2_x = [-7, 0, -2]
triangle_2_y = [1, 5, 11]

# Draw the graph y = 2x
x = np.arange(-5, 6, 1)
y = 2*x
plt.plot(x, y, color='yellow', label='Line: y = 2x', linewidth=1)

# Eigenvectors 
eigenvector_1 = [1, 2]
eigenvector_2 = [-4, 2]

# Draw related graphs
Draw_Eigenvector(eigenvector_1, 'darkviolet', 'Eigenvector 1')
Draw_Eigenvector(eigenvector_2, 'mediumaquamarine', 'Eigenvector 2')
Oxy()
Figure_settings()
Draw_triangle(triangle_1_x, triangle_1_y, "A", "B", "C", 'Original triangle', 'red')
Draw_triangle(triangle_2_x, triangle_2_y, "A'", "B'", "C'", 'Triangle received', 'green')

# Show caption
plt.legend()

# Show graphs
plt.show()

