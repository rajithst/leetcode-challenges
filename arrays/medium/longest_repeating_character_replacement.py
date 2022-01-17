class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_start = 0
        mem = {}
        max_freq = 0
        max_length = 0
        for window_end in range(len(s)):
            char = s[window_end]
            if char not in mem:
                mem[char] = 0
            mem[char] += 1
            # always keep calculate the max_frequency in the window,remaining characters should be replace
            max_freq = max(max_freq, mem[char])

            # if replacable characters are greater than the k,we need to shrink window till posible
            while (window_end - window_start + 1) - max_freq > k:
                remove_char = s[window_start]
                mem[remove_char] -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length



