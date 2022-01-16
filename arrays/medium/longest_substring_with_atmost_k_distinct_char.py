class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        ws = 0
        lg = 0
        mem = {}
        for we in range(len(s)):
            char = s[we]
            if char not in mem:
                mem[char] = 0
            mem[char] += 1

            while len(mem) > k:
                ch2 = s[ws]
                mem[ch2] -= 1
                if mem[ch2] == 0:
                    del mem[ch2]
                ws += 1

            lg = max(lg, we - ws + 1)
        return lg