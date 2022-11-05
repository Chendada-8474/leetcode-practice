from collections import Counter


class Solution:
    def _backtrack(self, b, index):
        if self.board[b[0]][b[1]] != self.word[index]:
            return
        index += 1
        self.route.add(b)
        if len(self.word) == index:
            return True
        for x, y in self.S:
            x += b[0]
            y += b[1]
            if (
                (x, y) not in self.route
                and x > -1
                and y > -1
                and x < len(self.board)
                and y < len(self.board[0])
            ):
                if self._backtrack((x, y), index):
                    return True
        self.route.remove(b)

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.word = list(word)
        self.board = board
        self.S = ((1, 0), (0, 1), (0, -1), (-1, 0))
        self.route = set()
        self.index = 0

        bc = sum((Counter(b) for b in board), start=Counter())
        bc.subtract(word)
        if any(b < 0 for b in bc.values()):
            return False

        for ixb, xb in enumerate(board):
            for iyb, yb in enumerate(xb):
                if yb == self.word[0]:
                    if self._backtrack((ixb, iyb), self.index):
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
