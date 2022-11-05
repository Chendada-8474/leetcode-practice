from collections import Counter


class Solution:
    def _backtrack(self, x, y, index):
        if (
            self.board[x][y] != self.word[index]
            or self.route
            or x < 0
            or y < 0
            or x >= len(self.board)
            or y >= len(self.board[0])
        ):
            return
        index += 1
        self.route.add((x, y))
        if len(self.word) == index or any(
            self._backtrack(x + i, y + j, index) for i, j in self.S
        ):
            return True
        self.route.remove((x, y))

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.word = list(word)
        self.board = board
        self.S = ((1, 0), (0, 1), (0, -1), (-1, 0))
        self.route = set()
        self.index = 0

        wc = Counter(word)
        bc = sum((Counter(b) for b in board), start=Counter())
        if wc - bc:
            return False

        for ixb, xb in enumerate(board):
            for iyb, yb in enumerate(xb):
                if self._backtrack(ixb, iyb, self.index):
                    return True

        return False


if __name__ == "__main__":
    board = [
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A", "A"],
    ]

    word = "AAAAAAAAAAAABAA"
    solution = Solution()
    print(solution.exist(board, word))
