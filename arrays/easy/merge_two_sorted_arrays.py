from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1 = 0
        index_2 = 0
        nums1_copy = nums1[:m]

        for i in range(n + m):
            if index_2 >= n or (index_1 < m and nums1_copy[index_1] <= nums2[index_2]):
                nums1[i] = nums1_copy[index_1]
                index_1 += 1
            else:
                nums1[i] = nums2[index_2]
                index_2 += 1