from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        visited = []
        for i in range(rows):
            visited.append([0] * cols)

        def flood_fill(x, y, new_color, start_color):
            visited[x][y] = 1
            image[x][y] = new_color
            coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in coordinates:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if image[new_x][new_y] == start_color and visited[new_x][new_y] == 0:
                        flood_fill(new_x, new_y, new_color, start_color)

        x, y = sr, sc
        start_color = image[x][y]
        flood_fill(x, y, newColor, start_color)
        return image