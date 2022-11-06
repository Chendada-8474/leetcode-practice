class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        if n == 2:
            return n
        n1 = 1
        n2 = 2
        ans = 0
        for i in range(3, n + 1):
            ans = n1 + n2
            n1 = n2
            n2 = ans
        return ans
