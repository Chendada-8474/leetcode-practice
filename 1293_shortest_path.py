class Solution:
    def shortestPath1(self, grid: list[list[int]], k: int) -> int:
        w = len(grid)
        h = len(grid[0])
        if w == 1 and h == 1:
            return 0
        S = ((0, 1), (1, 0), (0, -1), (-1, 0))
        tasks = {(0, 0): {"k": k, "track": {(0, 0): None}}}
        steps = 1
        while len(tasks) != 0:
            print(tasks, steps)
            new_tasks = {}
            for xy, info in tasks.items():
                for x, y in S:
                    x += xy[0]
                    y += xy[1]
                    p = (x, y)
                    if x < 0 or x == w or y < 0 or y == h:
                        continue
                    g = grid[x][y]
                    if p in info["track"]:
                        continue
                    if not g:
                        if p == (w - 1, h - 1):
                            return steps
                        elif (
                            p in new_tasks
                            and new_tasks[p]["k"] < info["k"]
                            or p not in new_tasks
                        ):
                            info["track"][p] = None
                            new_tasks[p] = info
                    else:
                        if p == (w - 1, h - 1) and info["k"]:
                            return steps
                        elif info["k"] and (
                            (p in new_tasks and new_tasks[p]["k"] < info["k"] - 1)
                            or (p not in new_tasks)
                        ):
                            new_tasks[p] = {"k": info["k"] - 1, "track": {}}
                            new_tasks[p]["track"][p] = None
            tasks = new_tasks
            steps += 1
        return -1

    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        pass


grid = [[0] + [1] * 2] + [[1] * 3] * 1 + [[1] * 2 + [0]]

k = 3

solution = Solution()
print(solution.shortestPath1(grid, k))

# print([1600] * 5)
