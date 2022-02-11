from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # if intervals length is less than 2,we can't merge any interval
        if len(intervals) < 2:
            return intervals

        # sort list by start time, this way we can find the starting slot
        # we need to compare current slot's end time with next slot's start time
        # if two values are overlap,we need to merge two intervals
        sorted_list = sorted(intervals, key=lambda x: x[0])
        results = []

        # get first slot's start and end time as initials
        start = sorted_list[0][0]
        end = sorted_list[0][1]

        # start looping from next interval
        for i in range(1, len(sorted_list)):
            current_start, current_end = sorted_list[i]

            # if current slot's start time <= to previous slot's end time
            # we need to merge two intervals
            # find the maximum end time between two slots and update end value
            if current_start <= end:
                end = max(end, current_end)

            # if intervals are not overlapping,add interval to result
            else:
                results.append([current_start, current_end])

                # update new start and end with  current interval's values
                start = current_start
                end = current_end

        # end of the loop,add whatever merged interval
        results.append([start, end])
        return results
