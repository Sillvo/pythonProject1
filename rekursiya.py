import csv

maze = []
DIRS=((1, 0), (0, 1), (-1, 0), (0, -1))
with open('maze-1.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        maze.append([int(char) for cell in row for char in cell])
#jkenfkjsdf
def find_path(maze_new, v, d):
    if v == len(maze_new)-2 and d == len(maze_new[0])-2:
        maze_new[v][d] = 'f'
        return maze_new, True
    else:
        if maze_new[v][d] == 0:
            maze_new[v][d] = 2
        for i in DIRS:
            if maze_new[v+i[0]][d+i[1]] == 0:
                maze_new, res = find_path(maze_new, v=v+i[0], d=d+i[1])
                if res:
                    return maze_new, True
        maze_new[v][d]=3
        return maze_new, False

maze, res = find_path(maze, 1, 1)
for row in maze:
    print('  '.join(str(cell) for cell in row).replace('2', '#').replace('3','.'))

