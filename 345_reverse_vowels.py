class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s = list(s)

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in v and s[r] in v:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in v and s[r] not in v:
                r -= 1
            elif s[r] in v and s[l] not in v:
                l += 1
            else:
                l += 1
                r -= 1
        s = "".join(s)
        return s


s = "hello"
solution = Solution()

print(solution.reverseVowels(s))
