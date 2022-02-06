from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        # if length of array is 1 or 0,we don't need to sort any sub-array
        if len(nums) <= 1:
            return 0

        def isOutofOrder(nums, idx):
            # if current index is 0,we only need to check next value is larger or not
            if i == 0:
                return nums[i] > nums[1]
            # if current index is last value in array,we only need to check previous value smaller or not
            if i == len(nums) - 1:
                return nums[i] < nums[i - 1]
            # if current index is middle of the array,
            #  1. check if previous value is smaller than current value
            #  2. check if next value is greater than current value
            #  if any of this false,current index is out of order
            return nums[i] < nums[i - 1] or nums[i] > nums[i + 1]

        """find the smallest and largest value which out of order ,because based on the `smallest out of order` value 
        and `largest out of order value`, we may need to re-arrange entire array ex = [1, 3, 2, 0, -1, 7, 10] out of 
        order  range = [2,0,-1] sorting this range will not make entire array sorted ([1, -1, 0, 2, 3, 7, 10]) 

        """
        smallest_oo_value = float("inf")
        largest_oo_value = float("-inf")
        for i in range(len(nums)):
            # if current index is out of order,we need to change the position of that index
            if isOutofOrder(nums, i):
                # update smallest and largest values,which out of order
                smallest_oo_value = min(smallest_oo_value, nums[i])
                largest_oo_value = max(largest_oo_value, nums[i])

        # if entire array is sorted,we can return 0
        if smallest_oo_value == float("inf"):
            return 0

        # find what is the correct position we need to put `smallest out of order value`
        left_pointer = 0
        while smallest_oo_value >= nums[left_pointer]:
            left_pointer += 1

        # find what is the correct position we need to put `largest out of order value`
        right_pointer = len(nums) - 1
        while largest_oo_value <= nums[right_pointer]:
            right_pointer -= 1
        # finally we need to sort entire sub-array starting from left pointer to right pointer to make entire array sort
        return right_pointer - left_pointer + 1

