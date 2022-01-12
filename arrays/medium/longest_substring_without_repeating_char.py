class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window_start = 0
        substring_length = 0
        max_length = 0
        lookup = {}
        for window_end in range(len(s)):
            char = s[window_end]

            # if character in map and character within the current window
            if char in lookup and lookup[char] >= window_start:
                # start new window at next position
                window_start = lookup[char] + 1
                # shrink substring length
                substring_length = window_end - window_start

            lookup[char] = window_end
            substring_length += 1
            max_length = max(max_length, substring_length)
        return max_length
