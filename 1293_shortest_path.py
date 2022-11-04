class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        S = ((0, 1), (1, 0), (0, -1), (-1, 0))
        tasks = [(0, 0, k)]
        steps = 1
        while len(tasks) != 0:

            new_tasks = []
            for tx, ty, kn in tasks:
                print(tx, ty, kn, steps)
                for x, y in S:
                    x += tx
                    y += ty
                    if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]):
                        continue
                    if not grid[x][y]:
                        if x == len(grid) - 1 and y == len(grid[0]) - 1:
                            return steps
                        else:
                            grid[x][y] += 1
                            new_tasks.append((x, y, kn))
                    elif kn and grid[x][y]:
                        if x == len(grid) - 1 and y == len(grid[0]) - 1:
                            return steps
                        elif (x, y) != (0, 0):
                            new_tasks.append((x, y, kn - 1))
            tasks = new_tasks
            steps += 1
        return -1


grid1 = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 1],
]
grid2 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 1],
]
k = 1
solution = Solution()
print(solution.shortestPath(grid1, k))
print("-" * 10)
print(solution.shortestPath(grid2, k))
