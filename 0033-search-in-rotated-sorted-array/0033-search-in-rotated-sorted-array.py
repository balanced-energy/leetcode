'''
Run a modified binary search on the input array s
    start = 0
    end = len(s) - 1
    While start <= end 
        Calculate mid = (start + end) // 2
        If s[mid] == target
            Return mid
        We need to check for two cases to find which half of the array is still sorted
        Case 1: s[start] < s[mid] 
            First half is still sorted 
            If target greater than s[start] and less than s[mid].
                We know the target is between start…mid indices.
                Set end to mid - 1
            Else 
                Set start to mid + 1
        Case 2: s[start] > s[mid]
            Second half still sorted
            If target greater than s[mid] and less than s[end].
                We know the target is between mid..end indices.
                Set start to mid + 1

            Else 
                Set end to mid - 1

Return - 1. Target was not found

[1], target = 0

start = 0 
end = 1 - 1 = 0

mid = 0



'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            # Check for found target
            if nums[mid] == target:
                return mid
            
            # Otherwise continue search, two cases
            # First half still sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            # Second half is still sorted
            elif nums[start] >= nums[mid]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1