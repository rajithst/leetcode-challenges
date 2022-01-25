class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # initialize to be replace pointer as 1st index
        next_pointer = 1
        # initialize count as 1
        count = 1

        for i in range(1, len(nums)):
            # since array is sorted,if previous element == current element,increment count
            if nums[i] == nums[i - 1]:
                count += 1
            # else ,we found a new element,reset the counnt for 1
            else:
                count = 1

            """
            if count is greater than 2
                1) we found a unwanted element,this unwanted element should replace by next valid value
                2) so we stop moving next_pointer value because in future we want a reference to where should we  replace
            till count is less than or equal 2
                1) we are not dealing with unwanted values,so we can keep moving next_pointer forward
                2) while moving forward,we keep copying the current value to next_pointer
                    i) since we are stop moving next_pointer right after found the unwanted value
                    ii) copying ensure that,always next_pointer value will be replaced by next valid value
            """
            if count <= 2:
                nums[next_pointer] = nums[i]
                next_pointer += 1
        return next_pointer
