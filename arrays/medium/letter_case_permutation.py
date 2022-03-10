from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        permutations = [s]
        # try to swap every letter and make a new permutation
        for char in range(len(s)):
            # check if character is a letter
            if s[char].isalpha():

                # if a letter,swap the case of every available permutation
                # and create a new permutation
                cpm = len(permutations)
                for i in range(cpm):
                    cp = list(permutations[i])
                    cp[char] = cp[char].swapcase()
                    permutations.append("".join(cp))
        return permutations
