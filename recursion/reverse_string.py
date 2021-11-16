from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def swap(start, end, given_string):
            if start >= end:
                return
            given_string[start], given_string[end] = given_string[end], given_string[start]
            return swap(start + 1, end - 1, given_string)

        swap(0, len(s) - 1, s)