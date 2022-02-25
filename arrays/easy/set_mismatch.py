from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        current_index = 0
        while current_index < len(nums):
            correct_index = nums[current_index] - 1
            if nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]
            else:
                current_index += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return [-1, -1]
