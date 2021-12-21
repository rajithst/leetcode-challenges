from collections import deque
from typing import List

#
# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
n = len(board)
cells = n * n

myboard = []
side = 1
for i in range(n - 1, -1, -1):
    if side == 1:
        myboard = myboard + board[i]
    else:
        myboard = myboard + list(reversed(board[i]))
    side = 3 - side

myboard = [0] + myboard

adj_list = {i: [] for i in range(1, cells)}
for u in range(1, cells):
    for dice in range(1, 7):
        v = myboard[min(cells, u + dice)]
        if v == -1:
            v = min(cells, u + dice)
        adj_list[u].append(v)

que = deque()
que.append(1)
visited = set()
visited.add(1)
distance = [0] * (cells + 1)
while que:
    cn = que.popleft()
    if cn >= cells:
        continue
    for n in adj_list[cn]:
        if n not in visited:
            que.append(n)
            visited.add(n)
            distance[n] = distance[cn] + 1

#return -1 if distance[cells] == 0 else distance[cells]
