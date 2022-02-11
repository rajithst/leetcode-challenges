class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # define initial pointers
        i = 0
        # variables for start and end positions
        start = 0
        end = 1
        result = []

        # since intervals are sorted,first we need to find where is the starting position of newInterval
        # iterate through intervals array till find the first overlapping position
        # after we found first overlapping position,we start to merge intervals

        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            result.append(intervals[i])
            i += 1

        # at this point,interval's end is greater than newInterval's start value
        # after found,first overlapping position,start merging remaining intervals if they overlapping
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result