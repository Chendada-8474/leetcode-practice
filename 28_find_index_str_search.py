class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = len(needle)
        b = [-1] + [0] + [-1] * (s - 2)
        i = 0
        j = 2

        while j < s:
            if needle[j - 1] == needle[i]:
                i += 1
                b[j] = i
                j += 1
            elif i > 0:
                i = b[i]
            else:
                b[j] = 0
                j += 1

        ni = 0
        hi = 0
        while hi < len(haystack):
            if haystack[hi] == needle[ni]:
                ni += 1
                hi += 1
            elif ni == 0:
                hi += 1
            else:
                ni = b[ni]
            if ni == s:
                return hi - ni
        return -1


if __name__ == "__main__":
    haystack = "leetcode"

    needle = "leeto"
    solution = Solution()
    print(solution.strStr(haystack, needle))
