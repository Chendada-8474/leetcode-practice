class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for j in s:
            if ans and j.swapcase() == ans[-1]:
                ans.pop()
            else:
                ans.append(j)
        return "".join(ans)


s = "leEeetcode"
solution = Solution()
print(solution.makeGood(s))
