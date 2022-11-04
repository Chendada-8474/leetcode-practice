def nearestExit(maze, entrance) -> int:
    S = ((0, 1), (1, 0), (0, -1), (-1, 0))
    maze[entrance[0]][entrance[1]] = "+"
    tasks = [entrance]
    steps = 1
    while len(tasks) != 0:
        new_tasks = []
        for tx, ty in tasks:
            for x, y in S:
                x += tx
                y += ty
                if x < 0 or x == len(maze) or y < 0 or y == len(maze[0]):
                    continue
                if maze[x][y] == ".":
                    if x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1:
                        return steps
                    else:
                        maze[x][y] = "+"
                        new_tasks.append((x, y))
        tasks = new_tasks
        steps += 1
    return -1


maze = [
    ["+", ".", "+", "+", "+", "+", "+"],
    ["+", ".", "+", ".", ".", ".", "+"],
    ["+", ".", "+", ".", "+", ".", "+"],
    ["+", ".", ".", ".", "+", ".", "+"],
    ["+", "+", "+", "+", "+", ".", "+"],
]
entrance = [0, 1]


print(nearestExit(maze, entrance))
