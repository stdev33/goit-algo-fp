import matplotlib.pyplot as plt
import numpy as np


def draw_pythagoras_tree(ax, x, y, angle, size, level):
    if level == 0:
        return

    # Calculate new coordinates for the next branch
    x_new = x + size * np.cos(angle)
    y_new = y + size * np.sin(angle)

    # Draw the current branch (line segment)
    ax.plot([x, x_new], [y, y_new], color="brown", lw=2)

    # Parameters for the left branch
    new_size = size * np.sqrt(2) / 2
    new_angle_left = angle + np.pi / 4
    draw_pythagoras_tree(ax, x_new, y_new, new_angle_left, new_size, level - 1)

    # Parameters for the right branch
    new_angle_right = angle - np.pi / 4
    draw_pythagoras_tree(ax, x_new, y_new, new_angle_right, new_size, level - 1)


def main():
    recursion_level = int(input("Enter the level of recursion (e.g., 5): "))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Initial coordinates and parameters
    x = 0
    y = 0
    angle = np.pi / 2  # Initial angle (90 degrees)
    size = 1  # Initial size
    draw_pythagoras_tree(ax, x, y, angle, size, recursion_level)

    plt.show()


if __name__ == "__main__":
    main()
