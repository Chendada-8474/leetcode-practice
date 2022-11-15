class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        x = {}
        y = {}
        for sx, sy in stones:
            if sx in x:
                x[sx].append((sx, sy))
            else:
                x[sx] = [(sx, sy)]
            if sy in y:
                y[sy].append((sx, sy))
            else:
                y[sy] = [(sx, sy)]
        v = set()
        c = 0
        for sx, sy in stones:
            s = (sx, sy)
            if s in v:
                continue
            v.add(s)
            t = [s]
            nt = []
            while len(t) != 0:
                for tx, ty in t:
                    for n in x[tx]:
                        if n not in v:
                            nt.append(n)
                            v.add(n)
                    for n in y[ty]:
                        if n not in v:
                            nt.append(n)
                            v.add(n)
                t = nt
                nt = []
            c += 1
        return len(stones) - c

    def _find_boss(self, t: int) -> int:
        p = []
        while t != jsf[t]:
            p.append(t)
            t = jsf[t]
        for i in p:
            jsf[i] = t
        return t

    def disjoint_set_version(self, stones: list[list[int]]) -> int:
        global jsf
        jsf = list(range(len(stones)))

        x = {}
        y = {}
        for i, (sx, sy) in enumerate(stones):
            if sx in x:
                jsf[self._find_boss(i)] = self._find_boss(x[sx])
            else:
                x[sx] = i
            if sy in y:
                jsf[self._find_boss(i)] = self._find_boss(y[sy])
            else:
                y[sy] = i

        boss = set()
        for b in jsf:
            boss.add(self._find_boss(b))
        return len(stones) - len(boss)


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]

solution = Solution()
print(solution.disjoint_set_version(stones))
# print(solution._find_boss(3, [0, 0, 2, 2, 1]))
