class Solution:
    def findMaxK(self, nums: List[int]) -> int:
       
        s = set(nums)
        largest_num = -1

        if len(nums) <= 1:
            return -1

        for i in nums:
            if -1 * i in s:
                if i > largest_num:
                    largest_num = i
        return largest_num