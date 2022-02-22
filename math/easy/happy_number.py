class Solution:
    def isHappy(self, n: int) -> bool:

        def find_square_sum(num):
            sq_sum = 0
            while num > 0:
                digit = num % 10
                sq_sum += digit * digit
                num = num // 10
            return sq_sum

        # define fast and slow pointer to initial value
        fast, slow = n, n
        while True:
            # slow pointer is square sum of slow
            slow = find_square_sum(slow)
            # fast pointer is square sum of next next of fast
            fast = find_square_sum(find_square_sum(fast))
            # if cycle is with number 1,which means happy number
            # otherwise it will stuck with a cycle with a different number
            if slow == fast:
                break
        return slow == 1
