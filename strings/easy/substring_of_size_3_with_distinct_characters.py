class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        window_start = 0
        mem = {}
        count = 0
        for window_end in range(len(s)):
            char = s[window_end]
            if char not in mem:
                mem[char] = 0
            mem[char] += 1

            if window_end >= 3:
                remove = s[window_start]
                mem[remove] -= 1
                if mem[remove] == 0:
                    del mem[remove]
                window_start += 1
            if len(mem) == 3:
                count += 1
        return count
