class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        ws = 0
        points = 0
        range_count = 0
        for we in range(len(calories)):
            range_count += calories[we]

            if we >= k - 1:
                if range_count < lower:
                    points -= 1
                elif range_count > upper:
                    points += 1

                remove = calories[ws]
                range_count -= remove
                ws += 1

        return points
