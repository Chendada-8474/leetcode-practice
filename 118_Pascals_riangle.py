class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        for i in range(1, numRows + 1):
            n = 1
            l = []
            for j in range(1, i + 1):
                l.append(n)
                n = n * (i - j) // j
            ans.append(l)
        return ans


solution = Solution()
print(solution.generate(10))
