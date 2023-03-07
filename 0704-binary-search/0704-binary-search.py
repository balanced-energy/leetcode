'''
Workflow Timestamps
1. 0:00 - 1:45 Make Sure You Understand the Problem
2. 1:45 - 5:25 Design a Solution / Runtime and Space Complexity
3. 9:10 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 21:05 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[1] -> 0

2. Design a Solution / Runtime and Space Complexity
- Two pointers, left being 0 and right being length of nums - 1
- while left pointer is less than our right 
- Calculate a mid variable being left + right // 2 
    - if mid = target return mid 
    - if mid < target we set left bound to be mid+1
    - if mid > target we set right bound to mid-1
    - Reach this point, target not found and return -1

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize pointers 
left, right = 0, len(nums) - 1

while left < right:
    compute mid to be left + right // 2
    if nums[mid] = target:
        return mid
    if nums[mid] < target:
        set left to mid + 1
    if nums[mid] > target:
        set right to mid - 1
# Not found 
return -1 

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers 
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        
        # Target not found
        return - 1
        