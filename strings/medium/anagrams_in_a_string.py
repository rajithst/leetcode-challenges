from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        window_start = 0
        char_frequency = {}
        for char in p:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

        result = []
        matched = 0
        for window_end in range(len(s)):
            current_char = s[window_end]
            if current_char in char_frequency:

                char_frequency[current_char] -= 1

                if char_frequency[current_char] == 0:
                    matched += 1
            if matched == len(char_frequency):
                result.append(window_start)

            if window_end >= len(p) - 1:
                remove_char = s[window_start]
                if remove_char in char_frequency:
                    if char_frequency[remove_char] == 0:
                        matched -= 1
                    char_frequency[remove_char] += 1
                window_start += 1
        return result
