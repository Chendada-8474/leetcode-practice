class Solution:
    def maximum69Number(self, num: int) -> int:
        ans = num
        n = num
        for i in (1000, 100, 10, 1):
            d = int(n / i)
            if d == 6:
                ans = num + 3 * i if ans < num + 3 * i else ans
            n = n - d * i
        return ans


num = 9996
solution = Solution()
print(solution.maximum69Number(num))
