class Solution:
    def maximum69Number(self, num: int) -> int:
        n = num
        for i in (1000, 100, 10, 1):
            d = int(n / i)
            if d == 6:
                num = num + 3 * i
                break
            n = n - d * i
        return num


num = 9996
solution = Solution()
print(solution.maximum69Number(num))
