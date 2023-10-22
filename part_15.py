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
	plt.axis('equal')

def Figure_settings():
	# Title and labels 
	plt.xlabel('x', fontname='Times New Roman', fontsize=15, color='white')
	plt.ylabel('y', fontname='Times New Roman', fontsize=15, color='white')
	plt.title('Пару отображений, последовательное применение которых даёт различные результаты в зависимости от порядка: AB ̸= BA.', fontname='Times New Roman', fontsize=12, color='pink')
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

def Draw_Eigenvector(vecto, color, vecto_name):
    ax.quiver(0, 0, vecto[0], vecto[1], angles='xy', scale_units='xy', scale=1, color=f'{color}', label=f'{vecto_name}', width=0.004, headwidth=2, headaxislength=3, headlength=4)

    # Customize the limits of the x and y axis
    ax.set_xlim([0, max(vecto[0], 1)])  # Sets the x-axis limit from 0 to the x-value of the vector, or 1 if vector[0] <= 1
    ax.set_ylim([0, max(vecto[1], 1)])  # Sets the y-axis limit from 0 to the y-value of the vector, or 1 if vector[0] <= 1

    # Name the x and y axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

def Draw_triangle(triangle_x, triangle_y, a, b, c, Triangle_name, color):
	plt.fill(triangle_x, triangle_y, color=f'{color}', alpha=0.5, label=f'{Triangle_name}')
	plt.plot(triangle_x, triangle_y, marker='o', color=f'{color}', linestyle="")
	
	plt.text(triangle_x[0], triangle_y[0], f'{a}', ha='right', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=10)
	plt.text(triangle_x[1], triangle_y[1], f'{b}', ha='right', va='top', color=f'{color}', fontname='Times New Roman', fontsize=10)
	plt.text(triangle_x[2], triangle_y[2], f'{c}', ha='center', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=10)

# Creates a drawing object and set size, background for figure 
fig, ax = plt.subplots(figsize=(10,7))
fig.set_facecolor('black')

# Draw line y = 2x
x = np.arange(-6, 7, 1)
y = 2*x
plt.plot(x, y, color='black', linewidth=1.5, label="Line: y = 2x")

# Original triangle 
triangle_x = [5, 4, 10]
triangle_y = [-5, 3, 5]

# Отображение (симметрию) плоскости относительно прямой y = 2x.
triangle_A_x = [-7, 0, -2]
triangle_A_y = [1, 5, 11]

# Отображение вращения с углом phi против часовой стрелки.
triangle_B_x = [7, 0, 2]
triangle_B_y = [1, 5, 11]

# Парa отображений P = B.A
triangle_BA_x = [-17/5, 4, 38/5]
triangle_BA_y = [31/5, 3, 41/5]

# Парa отображений P = A.B
triangle_AB_x = [-5, -4, -10]
triangle_AB_y = [-5, 3, 5]

# Eigenvectors 
eigenvector_1 = [12, 9]
eigenvector_2 = [-9, 12]

# Draw Eigenvectors
Draw_Eigenvector(eigenvector_1, 'firebrick', 'Eigenvector 1')
Draw_Eigenvector(eigenvector_2, 'mediumaquamarine', 'Eigenvector 2')

# Draw graphs
Oxy()
Figure_settings()
Draw_triangle(triangle_x, triangle_y, "a", "b", "c", 'Original triangle', 'red')
Draw_triangle(triangle_A_x, triangle_A_y, "a2", "a2", "a2", 'Triangle A', 'black')
Draw_triangle(triangle_B_x, triangle_B_y, "a3", "b3", "c3", 'Triangle B', 'darkcyan')
Draw_triangle(triangle_BA_x, triangle_BA_y, "a23", "b23", "c23", 'Triangle received BA', 'green')
Draw_triangle(triangle_AB_x, triangle_AB_y, "a32", "b32", "c32", 'Triangle received AB', 'hotpink')

# Show caption
plt.legend()

# Show graphs
plt.show()