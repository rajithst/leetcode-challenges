from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0
        start = 0
        end = 1
        result = []
        while i < len(firstList) and j < len(secondList):
            lap_f = firstList[i]
            lap_s = secondList[j]

            '''
             lp-f(s)     lp-f(e)
                |----------|
           lp-s(s)    lp-2(e)
            |----------|

            '''
            first_overlaps_second = lap_s[start] <= lap_f[start] <= lap_s[end]

            '''
             lp-f(s)     lp-f(e)
                |----------|
                   lp-s(s)    lp-s(e)
                    |----------|
            '''
            second_overlaps_first = lap_f[start] <= lap_s[start] <= lap_f[end]

            # if any overlapping found
            if first_overlaps_second or second_overlaps_first:
                # find the overlapping area
                overlap_start = max(lap_f[start], lap_s[start])
                overlap_end = min(lap_f[end], lap_s[end])
                result.append([overlap_start, overlap_end])

            # move pointer of list,which finish first
            if lap_f[end] < lap_s[end]:
                i += 1
            else:
                j += 1
        return result