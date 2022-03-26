class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        If a string with an even length is a palindrome,
        every character in the string must always occur an even number of times.
        If the string with an odd length is a palindrome,
        every character except one of the characters must always occur an even number of times.
        Thus, in case of a palindrome,
        the number of characters with odd number of occurrences can't exceed 1
        (1 in case of odd length and 0 in case of even length).
        """
        char_frequency = {}
        for char in s:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1

        odd_count = 0
        for k, v in char_frequency.items():
            if v % 2 == 1:
                odd_count += 1

        return odd_count < 2
