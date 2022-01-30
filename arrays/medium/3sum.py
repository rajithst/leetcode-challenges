from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            current_num = sorted_nums[i]
            diff = 0 - current_num
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                r1 = sorted_nums[p1]
                r2 = sorted_nums[p2]
                if diff == r1 + r2:
                    results.append([current_num, r1, r2])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and sorted_nums[p1] == sorted_nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and sorted_nums[p2] == sorted_nums[p2 + 1]:
                        p2 -= 1
                elif r1 + r2 < diff:
                    p1 += 1
                else:
                    p2 -= 1
        return results