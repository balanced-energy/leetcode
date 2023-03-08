
'''
Workflow Timestamps
1. 0:00 - 2:15 Make Sure You Understand the Problem
2. 2:15 - 8:45 Design a Solution / Runtime and Space Complexity
3. 8:45 - 14: 45 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

 l     m     r
         l m r
[4,5,6,7,0,1,2] target 0

 l     m     r
 l m r     
[4,5,6,7,0,1,2] target 6

2. Design a Solution / Runtime and Space Complexity
Perform binary search. We want to compare mid to the start element to determine which half of the array is still sorted.
Once we know which is still sorted we check if target is within that sorted half, if so move pointers to continue on that 
half, otherwise move pointers to other half.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
start = 0
end = length of array - 1

while start <= end

# Compare mid element to start 
calculate mid 

Check if mid == target 

# First half still sorted
If nums[mid] > nums[start]
    if nums[start] <= target < nums[mid] 
        right = mid - 1
    else 
        left = mid + 1
# Second half still sorted
if nums[mid] < nums[start]
    if nums[mid] <= target < nums[start] 
        left = mid + 1
    else 
        right = mid - 1
        
return - 1
4. Write the Code And Pass Test Cases.

[4,5,6,7,0,1,2] target 6

[5,1,3] target 3
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            # First half is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                    
                else:
                    start = mid + 1
                    
            # Second half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                    
                else:
                    end = mid - 1
        
        return - 1
        