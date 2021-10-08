from typing import List


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        self.heap.append(node)
        self.perlcoate_up(index=len(self.heap) - 1)

    def remove_min(self):
        if len(self.heap) == 1:
            min_val = self.heap[0]
            del self.heap[0]
            return min_val

        elif len(self.heap) > 1:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.heapify(index=0)
            return min_val
        else:
            return

    def is_empty(self):
        return len(self.heap) == 0

    def perlcoate_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return

        elif self.heap[parent_index][1] > self.heap[index][1]:
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = tmp
            self.perlcoate_up(parent_index)

    def heapify(self, index):
        smallest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if len(self.heap) > left_index and self.heap[smallest][1] > self.heap[left_index][1]:
            smallest = left_index
        if len(self.heap) > right_index and self.heap[smallest][1] > self.heap[right_index][1]:
            smallest = right_index
        if smallest != index:
            tmp = self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest] = tmp
            self.heapify(smallest)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj_list = {}
        for i in range(len(points)):
            if i not in adj_list:
                adj_list[i] = []
            for j in range(len(points)):
                if i != j:
                    weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    node = (j, weight)
                    adj_list[i].append(node)

        visited = {}
        for k in range(len(points)):
            visited[k] = False
        pq = MinHeap()
        pq.insert((0, 0))
        mst = 0
        while not pq.is_empty():
            best_edge = pq.remove_min()
            node_val = best_edge[0]
            weight = best_edge[1]
            if visited[node_val]:
                continue
            mst += weight
            visited[node_val] = True
            for n in adj_list[node_val]:
                if not visited[n[0]]:
                    pq.insert(n)
        return mst