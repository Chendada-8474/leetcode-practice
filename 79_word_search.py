from collections import Counter


class Solution:
    def _backtrack(self, x, y, index):
        if (
            (x, y) in self.route
            or x < 0
            or y < 0
            or x >= len(self.board)
            or y >= len(self.board[0])
            or self.board[x][y] != self.word[index]
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
        if Counter(word) - sum((Counter(b) for b in board), start=Counter()):
            return False
        return any(
            any(self._backtrack(x, y, self.index) for y in range(len(board[0])))
            for x in range(len(board))
        )


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    solution = Solution()
    print(solution.exist(board, word))
