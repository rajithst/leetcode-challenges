from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    cities = len(isConnected[0])
    if cities == 0:
        return
    root = [i for i in range(cities)]

    def find(i):
        if root[i] == i:
            return i
        return find(root[i])

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            root[root_i] = root_j

    for i in range(cities):
        for j in range(cities):
            if i != j and isConnected[i][j] == 1:
                union(i, j)

    cc = set()
    for r in range(cities):
        cc.add(find(root[r]))
    return len(cc)