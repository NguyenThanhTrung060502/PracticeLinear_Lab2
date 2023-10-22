import matplotlib.pyplot as plt


def Oxy():
    # Draw the coordinate system Oxy
    Ox = list(range(-20, 21, 2))
    Oy = list(range(-20, 21, 2))
    plt.xticks(Ox, color='white')
    plt.yticks(Oy, color='white')
    plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # Axis Ox
    plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # Axis Oy
    # This function is used to adjust so that the units of the Ox and Oy axes are equal 
    plt.axis('equal')

def Figure_settings():
	# Title and labels
	plt.title('Поворот плоскости на 90° против часовой стрелки', fontname='Times New Roman', fontsize=15, color='pink')
	plt.xlabel('x', color='white', fontname='Times New Roman', fontsize=15)
	plt.ylabel('y', color='white', fontname='Times New Roman', fontsize=15)
	plt.grid(color="silver", linestyle='--', linewidth=0.5)

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
    plt.plot(triangle_x,triangle_y, marker='o', color=f'{color}', ms=5, linestyle="")

    plt.text(triangle_x[0], triangle_y[0], f'{a}', ha='right', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=15)
    plt.text(triangle_x[1], triangle_y[1], f'{b}', ha='right', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=15)
    plt.text(triangle_x[2], triangle_y[2], f'{c}', ha='right', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=15)

# Set size and set background for figure
fig = plt.figure(figsize=(10,7))
fig.set_facecolor('black')

# Original triangle  
triangle_1_x = [5, 4, 10]
triangle_1_y = [-5, 3, 5]

# Triangle received  
triangle_2_x = [5, -3, -5]
triangle_2_y = [5, 4, 10]

# Draw related graphs
Oxy()
Figure_settings()
Draw_triangle(triangle_1_x, triangle_1_y, "A", "B", "C", 'Original triangle', 'red')
Draw_triangle(triangle_2_x, triangle_2_y, "A'", "B'", "C'", 'Triangle received', 'green')

# Show caption
plt.legend()

# Show graphs
plt.show()