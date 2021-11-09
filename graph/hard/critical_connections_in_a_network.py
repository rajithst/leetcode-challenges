from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list = {i: [] for i in range(n)}
        for i, j in connections:
            adj_list[i].append(j)
            adj_list[j].append(i)

        visited = {i: False for i in range(n)}
        discovery_time = {}
        lowest_time = {}
        t = 1
        bridges = []

        # find articulation points and bridges
        def dfs_tree(node, parent):
            nonlocal t
            visited[node] = True
            discovery_time[node] = lowest_time[node] = t
            t += 1
            for child_node in adj_list[node]:
                if not visited[child_node]:
                    dfs_tree(child_node, node)
                    # after finish exploring the child node ,update lowest time
                    # because low time of a node = lowest time of all child nodes
                    lowest_time[node] = min(lowest_time[node], lowest_time[child_node])
                    # FIND BRIDGES
                    if lowest_time[child_node] > discovery_time[node]:
                        bridges.append([node, child_node])

                elif child_node != parent:
                    # found backedge
                    # compare lowest time of current node and backedge node's discovery time
                    lowest_time[node] = min(lowest_time[node], discovery_time[child_node])

        dfs_tree(0, -1)
        return bridges

