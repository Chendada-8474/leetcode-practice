class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return (
            min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else "".join(sorted(s))
        )

    def orderly_queue_kmp(self, s: str, k: int) -> str:
        if k == 1:
            return "".join(sorted(s))
        else:

            pass


if __name__ == "__main__":
    s = "enbczfjtvxerzbrvigpl"
    k = 1

    solution = Solution()
    print(solution.orderly_queue_kmp(s, k))
