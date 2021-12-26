from typing import List


class Node:
    def __init__(self, char):
        self.char = char
        self.childrens = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        temp = self.root
        for w in word:
            if w not in temp.childrens:
                temp.childrens[w] = Node(w)
            temp = temp.childrens[w]
        temp.is_end = True


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        t = Trie()
        t.insert(word)

        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for i in range(rows)]

        def dfs(x, y, root):

            char = board[x][y]
            if char not in root.childrens:
                return False

            visited[x][y] = True
            root = root.childrens[char]
            if root.is_end:
                return True

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols and visited[newx][newy] == False:
                    ret = dfs(newx, newy, root)
                    if ret:
                        return True

            visited[x][y] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, t.root):
                        return True
        return False

