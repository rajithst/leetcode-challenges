from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        adj_list = {}
        for word in wordList:
            for char in range(len(word)):
                pattern = word[:char] + "_" + word[char + 1:]
                if pattern not in adj_list:
                    adj_list[pattern] = []
                adj_list[pattern].append(word)

        # bfs for shortest path
        from collections import deque
        que = deque()
        que.append(beginWord)
        visited = {beginWord: 1}
        depth = 1
        while que:
            current = len(que)
            for _ in range(current):
                cw = que.popleft()
                if cw == endWord:
                    return depth
                for i in range(len(cw)):
                    possible_pattern = cw[:i] + "_" + cw[i + 1:]
                    if possible_pattern in adj_list:
                        for adj in adj_list[possible_pattern]:
                            if adj not in visited:
                                que.append(adj)
                                visited[adj] = 1
            depth += 1
        return 0
