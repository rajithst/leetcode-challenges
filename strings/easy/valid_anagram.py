class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check if the lengths are the same, if not, return False
        if len(s) != len(t):
            return False
        # Create a dictionary to store the characters and their counts
        char_frequency = {}
        for char in t:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

        matched = 0
        # check if the characters in s are in char_frequency
        for we in range(len(s)):
            char = s[we]
            # if the character is in char_frequency, decrease the frequency
            if char in char_frequency:
                char_frequency[char] -= 1
                # if the frequency is 0, we found a matching set, increase the matched counter
                if char_frequency[char] == 0:
                    matched += 1
                # if matched count is equal to the length of s, we found a anagram,return True,otherwise return False
                if matched == len(char_frequency):
                    return True

        return False
