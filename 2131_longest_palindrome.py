class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        h = {}
        ans = 0
        for i in words:
            if i in h:
                if h[i] > 0:
                    ans += 4
                    h[i] -= 1
                    continue
            r = i[::-1]
            h[r] = h[r] + 1 if r in h else 1
        if any(i[1] == i[0] and h[i] > 0 for i in h):
            ans += 2
        return ans


words = ["ab", "ty", "yt", "lc", "cl", "ab"]
answer = Solution()
print(answer.longestPalindrome(words))
