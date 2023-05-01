'''
[1,3,5,6], 5
lo = 0
hi = 3
mid = 1

[1,3,5,6] , 2




[1,3,5,6], 0
lo = 0
hi = 3
mid = 1

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                hi = mid - 1
                
            else:
                lo = mid + 1
                
        return lo