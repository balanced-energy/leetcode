
'''
l      m     r

[4,5,6,1,2,3] target = 2

l      m     r
[4,5,6,1,2,3] target = 5

Comparing lo and mid elements we can check which half of the array is still sorted.
If start < mid then the first half is still sorted and we check if target is in that range
if start > mid then we know mid to end is sorted and check if target is in that range 

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid 

            # First half is still sorted
            if nums[mid] >= nums[start]:
                # Check if target within range
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # Second half is still sorted 
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
    

        return -1