def minMutation(start: str, end: str, bank: list) -> int:
    tasks = [start]
    ans = 0
    seen_bank = {}
    while len(tasks) != 0:
        new_tasks = []
        for t in tasks:
            if t == end:
                return ans
            for b in bank:
                if b in seen_bank:
                    continue
                if sum(1 for st, sb in zip(t,b) if st != sb) == 1:
                    new_tasks.append(b)
                    seen_bank[b] = True
        ans += 1
        tasks = new_tasks
    return -1



start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

print(minMutation(start, end, bank))



