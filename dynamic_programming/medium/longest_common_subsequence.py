class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def solve(string1, string2, index1, index2):
            if index1 == len(string1) or index2 == len(string2):
                return 0
            if (index1, index2) in memo:
                return memo[(index1, index2)]

            # if current letter for given index1 and index2 is equal,
            # that letter is part of the subsequence and solve sub problem for starting from next index for both strings
            if string1[index1] == string2[index2]:
                memo[(index1, index2)] = solve(string1, string2, index1 + 1, index2 + 1) + 1
                return memo[(index1, index2)]

            # if current letter for given index1 and index2 not equal,
            # we have two options,
            #  1 -> ignore current letter from string1 and solve the sub problem
            #  2 -> ignore current letter from string2 and solve the sub problem
            # return max from both options
            option_1 = solve(string1, string2, index1 + 1, index2)
            option_2 = solve(string1, string2, index1, index2 + 1)
            memo[(index1, index2)] = max(option_1, option_2)
            return memo[(index1, index2)]

        return solve(text1, text2, 0, 0)
