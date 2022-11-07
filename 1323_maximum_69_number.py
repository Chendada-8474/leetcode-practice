class Solution:
    def maximum69Number(self, num: int) -> int:
        n = num
        for i in (1000, 100, 10, 1):
            d = n // i
            if d == 6:
                num = num + 3 * i
                break
            n -= d * i
        return num


num = 696
solution = Solution()
print(solution.maximum69Number(num))
