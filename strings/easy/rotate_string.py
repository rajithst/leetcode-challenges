class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # if abcde
        # shift by 1 -> eabcd
        # shift by 2 -> deabc
        # shift by 3 -> cdeab
        # shift by 4 -> bcdea
        # shift by 5 -> abcde ---> this is full cycle
        # ---> abcde+abcde should have all the combinations of shifts
        # if given goal string is substring of s+s,can create goal from some number of shifts

        return len(s) == len(goal) and goal in s + s
