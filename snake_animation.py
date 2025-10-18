# snake_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Canvas size
width, height = 10, 10

fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')
ax.axis('off')  # hide axes

# Snake initial position
snake = [[5, 5]]  # starting point
line, = ax.plot([], [], 'gs', markersize=20)  # 'gs' = green square

def update(frame):
    global snake
    x, y = snake[-1]
    # Random move: up, down, left, right
    move = np.random.choice(['UP','DOWN','LEFT','RIGHT'])
    if move == 'UP': y += 1
    if move == 'DOWN': y -= 1
    if move == 'LEFT': x -= 1
    if move == 'RIGHT': x += 1
    # Keep inside bounds
    x = max(0, min(width-1, x))
    y = max(0, min(height-1, y))
    snake.append([x, y])
    if len(snake) > 5:  # snake length
        snake.pop(0)
    # Update line
    line.set_data([p[0] for p in snake], [p[1] for p in snake])
    return line,

ani = animation.FuncAnimation(fig, update, frames=50, interval=200)
ani.save("snake.gif", writer='pillow')
