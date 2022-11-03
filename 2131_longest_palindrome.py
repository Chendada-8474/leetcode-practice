# class Solution:
#     def longestPalindrome(self, words: list[str]) -> int:
#         ans = 0
#         redup = False
#         while len(words) != 0:
#             w = words[0]
#             along = True
#             for i, j in enumerate(words[1:]):
#                 if w == j[1] + j[0]:
#                     ans += 4
#                     words.pop(i + 1)
#                     along = False
#                     break
#             if not redup and along and w[0] == w[1]:
#                 ans += 2
#                 redup = True
#             words.pop(0)
#         return ans
from typing import Counter


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
        for i in h:
            if i[1] == i[0] and h[i] > 0:
                ans += 2
                break
        return ans


words = ["gg", "gg"]

words = ["ab", "ty", "yt", "lc", "cl", "ab"]


answer = Solution()
print(answer.longestPalindrome(words))
