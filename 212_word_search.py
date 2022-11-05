class Solution:
    def _backtrack(self, b, S, trie):
        self.route.add(b)
        w = self.board[b[0]][b[1]]
        if w not in trie:
            self.route.remove(b)
            return
        trie = trie[w]
        if "E" in trie:
            self.ans.add(trie["E"])
            del trie["E"]

            if len(trie) == 2 and "U" in trie:
                while len(trie) == 2 and "U" in trie:
                    del trie["U"][trie["C"]]
                    trie = trie["U"]
                self.route.remove(b)
                return

        for x, y in S:
            x += b[0]
            y += b[1]
            if (
                (x, y) not in self.route
                and x > -1
                and y > -1
                and x < len(self.board)
                and y < len(self.board[0])
            ):
                self._backtrack((x, y), S, trie)
        self.route.remove(b)

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        self.board = board
        self.S = ((1, 0), (0, 1), (0, -1), (-1, 0))
        self.route = set()
        self.ans = set()

        # make a trie
        for i in words:
            n = trie
            for j in i:
                if j not in n:
                    n[j] = {"U": n, "C": j}
                n = n[j]
            n["E"] = i

        for ixb, xb in enumerate(board):
            for iyb, yb in enumerate(xb):
                if yb in trie:
                    self._backtrack((ixb, iyb), self.S, trie)

        return list(self.ans)


if __name__ == "__main__":

    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    solution = Solution()
    print(solution.findWords(board, words))
