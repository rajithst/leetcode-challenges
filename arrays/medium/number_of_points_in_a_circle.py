from typing import List


def count_points(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    return [sum([(x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2 for x, y in points]) \
            for center_x, center_y, radius in queries]
