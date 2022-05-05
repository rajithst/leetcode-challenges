
def numDecodings(s: str) -> int:

    memo = {}

    def solve(index):

        if index == len(s):
            return 1
        if index in memo:
            return memo[index]
        ans = 0
        # if current value between 1 and 9,solve problem for starting from next index
        if 1 <= int(s[index]) <= 9:
            ans += solve(index + 1)

        """
        recurrence is take current index as one partition and solve for  problem for current index+1
                      take current index and current index+1 as one partition and solve for problem for current index+2
                      
        if current index+1 within the range and 
            current index value == 1
            we can take current index and current index+1 as one partition -> ex 11 take as 1|1 or 11
        if current index+1 within the range and 
            current index value withing 2 and 6 
            we can take current index and current index+1 as one partition -> ex 23 take as 2|3 or 23
            
        final answer is sum of all the partition ways
        """
        if index + 1 < len(s) and int(s[index]) == 1:
            ans += solve(index + 2)

        if index + 1 < len(s) and int(s[index]) == 2 and int(s[index + 1]) <= 6:
            ans += solve(index + 2)
        memo[index] = ans
        return ans

    return solve(0)

numDecodings("226")