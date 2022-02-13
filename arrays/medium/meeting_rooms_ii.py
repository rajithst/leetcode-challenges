import heapq as heap
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # sort meetings by start time to find the first meeting
        intervals.sort(key=lambda x: x[0])
        start, end = 0, 1

        # to keep track of the meeting end time,we can use min-heap
        # min-heap top value provides the earliest finished meeting
        # if any meeting finished before start new meeting,we can check with the heap values
        rooms = []
        min_rooms = 0
        for meeting in intervals:

            # remove all meetings which finished before start current meeting
            # this way we can assign already used meeting room without allocating new meeting room
            while len(rooms) > 0 and meeting[start] >= rooms[0]:
                heap.heappop(rooms)
            # add current meeting to heap
            heap.heappush(rooms, meeting[end])

            # keep track of maximum length of heap at any time
            # heap length is the number of meeting rooms currently allocated
            min_rooms = max(min_rooms, len(rooms))
        return min_rooms
