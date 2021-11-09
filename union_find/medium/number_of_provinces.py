from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    cities = len(isConnected[0])
    provinces = cities
    if cities == 0:
        return
    root = [i for i in range(cities)]
    rank = [1] * cities

    def find(i):
        if root[i] == i:
            return i
        root[i] = find(root[i])
        return root[i]

    def union(i, j, provinces):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                root[root_i] = root_j
                rank[root_j] += rank[root_i]
            else:
                root[root_j] = root_i
                rank[root_i] += rank[root_j]

            provinces -= 1
        return provinces

    for i in range(cities):
        for j in range(cities):
            if i != j and isConnected[i][j] == 1:
                provinces = union(i, j, provinces)

    return provinces
