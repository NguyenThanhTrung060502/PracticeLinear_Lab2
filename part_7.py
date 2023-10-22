import matplotlib.pyplot as plt
import numpy as np 

def Oxy():
	# Draw the coordinate system Oxy
	Ox = list(range(-20, 21, 1))
	Oy = list(range(-20, 21, 1))
	plt.xticks(Ox, color='white')
	plt.yticks(Oy, color='white')
	plt.plot(Ox, [0] * len(Ox), color='red', linewidth=1, label='Ox')  # Axis Ox
	plt.plot([0] * len(Oy), Oy, color='orange', linewidth=1, label='Oy')  # Axis Oy	
	plt.legend()
	plt.axis('equal')

def Figure_settings():
	# Title and labels 
	plt.xlabel('x', fontname='Times New Roman', fontsize=15, color='white')
	plt.ylabel('y', fontname='Times New Roman', fontsize=15, color='white')
	plt.title('Отображение, которое переводит прямую y = 2x в y = 0 и прямую y = -2x в x = 0.', fontname='Times New Roman', fontsize=12, color='pink')
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
	
	plt.text(triangle_x[0], triangle_y[0], f'{a}', ha='right', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=12)
	plt.text(triangle_x[1], triangle_y[1], f'{b}', ha='right', va='top', color=f'{color}', fontname='Times New Roman', fontsize=12)
	plt.text(triangle_x[2], triangle_y[2], f'{c}', ha='center', va='bottom', color=f'{color}', fontname='Times New Roman', fontsize=12)

# Set size and set background for figure
fig = plt.figure(figsize=(10,7))
fig.set_facecolor('black')

# Draw graphs y = 2x and y = -2x 
x_1 = np.arange(-5,6,1)
y_1 = 2*x_1
y_2 = -2*x_1

plt.plot(x_1, y_1, color='lightgreen', label="Line: y = 2x")
plt.plot(x_1, y_2, color='lightskyblue', label="Line: y = -2x")

# Original Triangle 
triangle_x = [5, 4, 10]
triangle_y = [-5, 3, 5]

# Triangle Received
triangle_2_x = [-5, 3, 5]
triangle_2_y = [-5,-4,-10]



# Draw related graphs
Oxy()
Figure_settings()
Draw_triangle(triangle_x, triangle_y, 'A', 'B', 'C', "Original triangle", "red")
Draw_triangle(triangle_2_x, triangle_2_y, "A'", "B'", "C'", "Received Triangle", "green")

# Show caption
plt.legend()

# Show graphs
plt.show()