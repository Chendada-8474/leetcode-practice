class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = list(s)
        return "".join(
            min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else sorted(s)
        )


if __name__ == "__main__":
    s = "enbczfjtvxerzbrvigpl"
    k = 1

    solution = Solution()
    print(solution.orderlyQueue(s, k))
