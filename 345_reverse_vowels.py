class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in v and s[r] in v:
                s = s[:l] + s[r] + s[l + 1 : r] + s[l] + s[r + 1 :]
                l += 1
                r -= 1
            elif s[l] in v and s[r] not in v:
                r -= 1
            elif s[r] in v and s[l] not in v:
                l += 1
            else:
                l += 1
                r -= 1
        return s


s = "hello"
solution = Solution()
print(s[:1])
print(solution.reverseVowels(s))
