from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        """
        place the numbers on their correct indices and ignore all numbers that are out of the range of the array
        (i.e., all negative numbers and all numbers greater than or equal to the length of the array).
        Once we are done with the cyclic sort we will iterate the array and the
        first index that does not have the correct number will be the smallest missing positive number!

        """
        current_index = 0
        while current_index < len(nums):
            correct_index = nums[current_index] - 1
            if 0 < nums[current_index] < len(nums) and nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]
            else:
                current_index += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return nums[i] + 1
