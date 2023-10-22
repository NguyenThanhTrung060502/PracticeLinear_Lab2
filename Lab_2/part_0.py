import numpy as np 
import matplotlib.pyplot as plt 

# Set size and set background for figure
fig = plt.figure(figsize=(10,7))
fig.set_facecolor('black')

# Draw the coordinate system Oxy
Ox = list(range(-20, 21, 1))
Oy = list(range(-20, 21, 1))

# Set the color for the values of the Ox axis and Oy axis
plt.xticks(Ox, color='white')
plt.yticks(Oy, color='white')

plt.plot(Ox, [0] * len(Ox), color='black', linewidth=0.5)  # Axis Ox
plt.plot([0] * len(Oy), Oy, color='black', linewidth=0.5)  # Axis Oy

# Draw original triangle
triangle_x = np.array([5, 4, 10]) 
triangle_y = np.array([-5, 3, 5])
plt.plot(triangle_x, triangle_y, marker='o', linestyle="", color="red")
plt.text(triangle_x[0], triangle_y[0], 'A', ha='right', va='bottom', color='red', fontname='Times New Roman', fontsize=15)
plt.text(triangle_x[1], triangle_y[1], 'B', ha='right', va='top',    color='red', fontname='Times New Roman', fontsize=15)
plt.text(triangle_x[2], triangle_y[2], 'C', ha='center',va='bottom', color='red', fontname='Times New Roman', fontsize=15)


# Set title and labels
plt.xlabel('x', color='white', fontname='Times New Roman', fontsize=15)
plt.ylabel('y', color='white', fontname='Times New Roman', fontsize=15)
plt.title('Original triangle', fontname='Times New Roman', fontsize=20, color='pink')
plt.grid(linestyle="--", color="silver", linewidth=0.5)

# Draw triangle
plt.fill(triangle_x, triangle_y,"red", alpha=0.5, label="Original triangle")

plt.legend()

# Show graph
plt.show()

