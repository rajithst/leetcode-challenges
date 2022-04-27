from typing import List


class TreeInfo:
    def __init__(self):
        self.results = []


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # if n == 3,we can fill 6 positions
        # we have two conditions
        # 1) if opened parenthesis count is less than N
        #       if true -> we can add another open parenthesis
        # 2) if closed parenthesis less than open parenthesis
        #       if true -> we can add close parenthesis
        # if total open+closed parenthesis == 2*n means we hit the base case
        # we found a balanced parenthesis set,add to result
        def generate(output, n, open_c, close_c, current, ti):
            if current == n * 2:
                ti.results.append(output)
                return

            if open_c < n:
                generate(output + "(", n, open_c + 1, close_c, current + 1, ti)

            if close_c < open_c:
                generate(output + ")", n, open_c, close_c + 1, current + 1, ti)

        ti = TreeInfo()
        generate("", n, 0, 0, 0, ti)
        return ti.results
