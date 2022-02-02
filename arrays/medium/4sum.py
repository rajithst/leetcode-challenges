from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # sort array,this way we can safely ignore repeating values
        # because after sort,same values come one after one
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # solve 3sum problem with nums[i]
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # solve 2sum problem with nums[i]+nums[j]
                p = j + 1
                q = len(nums) - 1
                while p < q:
                    # if total sum of 4 numbers equal to target,append to result list
                    tot = nums[i] + nums[j] + nums[p] + nums[q]
                    if tot == target:
                        result.append([nums[i], nums[j], nums[p], nums[q]])

                        # move pointer-p forward and pointer-q backward to find another pair
                        p += 1
                        q -= 1
                        # before calculate next round sum,we need to make sure that values are not repeated
                        # we can do the check with previous value and current value and if they are equal
                        # move pointer-p forward till find a different value
                        # move pointer-q backward till find a different value
                        while p < q and nums[p] == nums[p - 1]:
                            p += 1
                        while p < q and nums[q] == nums[q + 1]:
                            q -= 1
                    # if total is less than target value,we need a bigger total
                    # move p pointer forward to make bigger total
                    elif tot < target:
                        p += 1
                    # if total is bigger than target value,we need a smaller total
                    # move q pointer backward to make small total
                    else:
                        q -= 1

        return result
