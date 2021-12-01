from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
            return 0

        right = [0] * n
        left = [0] * n
        right[0] = height[0]
        for i in range(1, n):
            right[i] = max(right[i - 1], height[i])

        left[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            left[i] = max(left[i + 1], height[i])

        units = 0
        for i in range(n):
            units += min(right[i], left[i]) - height[i]
        return units
