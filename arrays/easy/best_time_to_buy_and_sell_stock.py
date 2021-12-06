from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        min_price = float("inf")
        max_profit = 0

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


p1 = 0
p2 = 1
arr = [2, 3, 3, 3, 6, 9, 9]
next_non_duplicate = 1

i = 1
while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1