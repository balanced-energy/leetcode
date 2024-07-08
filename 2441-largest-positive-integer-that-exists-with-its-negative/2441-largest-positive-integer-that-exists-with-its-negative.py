class Solution:
    def findMaxK(self, nums: List[int]) -> int:
       
      
        num_set = set(nums)
        largest_num = -1

        for num in nums:
            if -num in num_set:
                largest_num = max(largest_num, num)

        return largest_num