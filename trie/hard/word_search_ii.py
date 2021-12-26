from typing import List


class Node:
    def __init__(self, char):
        self.char = char
        self.childrens = {}
        self.is_end = False
        self.word = None


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
        temp.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        rows = len(board)
        cols = len(board[0])

        visited = [[False] * cols for _ in range(rows)]
        t = Trie()
        for word in words:
            t.insert(word)
        results = set()

        def dfs(x, y, root):

            char = board[x][y]
            if char not in root.childrens:
                return
            visited[x][y] = True
            root = root.childrens[char]
            if root.is_end:
                results.add(root.word)

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols and visited[newx][newy] == False:
                    dfs(newx, newy, root)
            visited[x][y] = False

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, t.root)

        return results