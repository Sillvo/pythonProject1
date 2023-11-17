import csv
import numpy as np

# Function to solve the maze
# x, y is the starting point
def solve_maze(maze, x, y, path):
    # If x, y is goal, return True
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        path.append((x, y))
        maze[x][y] = 3  # Mark the goal with 3
        return True

    # Check if maze[x][y] is valid
    if x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 0:
        # Mark x, y as part of solution path
        path.append((x, y))
        maze[x][y] = 3  # Mark the path with 3

        # Move forward in x direction
        if solve_maze(maze, x + 1, y, path):
            return True

        # If moving in x direction doesn't give solution, move down in y direction
        if solve_maze(maze, x, y + 1, path):
            return True

        # If none of the above movements work, then backtrack: remove (x, y) from path list and unmark x, y
        path.remove((x, y))
        maze[x][y] = 0
        return False

    return False
# Read the maze from a CSV file
with open('maze-1.csv') as csvfile:
    data = list(csv.reader(csvfile, delimiter=';'))
    maze = [[int(cell) for cell in row] for row in data]

# Solve the maze
path = []
solve_maze(maze, 1, 1, path)

# Print the maze with the path
for row in maze:
    print(' '.join(str(cell) for cell in row))