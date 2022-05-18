from typing import List


class ResultInfo:
    def __init__(self):
        self.res = []


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        keyboard = {1: [""],
                    2: ["a", "b", "c"],
                    3: ["d", "e", "f"],
                    4: ["g", "h", "i"],
                    5: ["j", "k", "l"],
                    6: ["m", "n", "o"],
                    7: ["p", "q", "r", "s"],
                    8: ["t", "u", "v"],
                    9: ["w", "x", "y", "z"]}

        def solve(current_index, output, info):

            if current_index == len(digits):
                if output != "":
                    info.res.append(output)
                return

            ci = int(digits[current_index])
            for letter in keyboard[ci]:
                solve(current_index + 1, output + letter, info)

        info = ResultInfo()
        solve(0, "", info)
        return info.res
