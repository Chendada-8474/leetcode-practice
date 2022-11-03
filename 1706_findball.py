def findBall(grid):
    ans = list(range(len(grid[0])))
    for m, a in enumerate(ans):
        for g in grid:
            g.append(-1)
            g.append(1)
            if g[m] != g[m + g[m]]:
                m = -1
                break
            m += g[m]
        ans[a] = m
    return ans


grid = [
    [1,1,1,-1,-1],
    [1,1,1,-1,-1],
    [-1,-1,-1,1,1],
    [1,1,1,1,-1],
    [-1,-1,-1,-1,-1]
    ]

print(findBall(grid))
