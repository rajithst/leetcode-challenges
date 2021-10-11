from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        price = [float("inf")] * n
        price[src] = 0
        for i in range(k + 1):
            tmp_prices = price.copy()
            for flight in flights:
                from_node, to_node, f_price = flight
                if price[from_node] != float("inf") and price[from_node] + f_price < tmp_prices[to_node]:
                    tmp_prices[to_node] = price[from_node] + f_price
            price = tmp_prices
        ans = -1 if price[dst] == float("inf") else price[dst]
        return ans