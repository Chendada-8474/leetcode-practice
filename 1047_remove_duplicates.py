class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for j in s:
            if ans and j == ans[-1]:
                ans.pop()
            else:
                ans.append(j)
        return "".join(ans)


s = "abbaca"
solution = Solution()
print(solution.removeDuplicates(s))
