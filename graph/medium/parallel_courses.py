from collections import deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegrees = {k: 0 for k in range(1, n + 1)}
        adj_list = {k: [] for k in range(1, n + 1)}

        for f, t in relations:
            indegrees[t] += 1
            adj_list[f].append(t)

        sem_courses = []
        for i in range(1, n + 1):
            if indegrees[i] == 0:
                sem_courses.append(i)

        semesters = 0
        finished_courses = 0
        while sem_courses:
            next_sem = []
            semesters += 1
            for cs in sem_courses:
                finished_courses += 1
                for ncs in adj_list[cs]:
                    indegrees[ncs] -= 1
                    if indegrees[ncs] == 0:
                        next_sem.append(ncs)
            sem_courses = next_sem

        if finished_courses == n:
            return semesters
        return -1