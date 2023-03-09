'''
Workflow Timestamps
1. 0:00 - 4:15 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
 l     m   r
 l m   r
[0,1,1,1,1,2] target 1 -> 


 l   m     r
     l m   r
       l m r
[0,1,2,2,2,3] target 2 -> 

 l     m       r
 l m   r
   l m r
[0,0,1,1,1,1,1,2] target 1 -> 

2. Design a Solution / Runtime and Space Complexity
Run bs twice
# Left bound
Run it to find left bound. Once mid == target, if it's 0 then return mid 
else if it's left neighbor is not target return mid

check if target <= mid, if so set right to mid else left to mid

# Right Bound from index returned from left bound check to end of array
Run it to find right bound. Once mid == target, if it's len(nums) - 1 then return mid 
else if it's right neighbor is not target return mid

check if target <= mid, if so set left to mid else right to mid

 l   m      r
     l m    r
                 left bound = 3
       l   m      r  
           l m    r
[5,7,7,8,8,8,8,9,10], target = 8
3. Write a Template for Code in Logical Blocks. Aka Pseudocode

left bound = -1
right bound = -1

# Find left bound range
Run binary search for left bound
while left <= right:
calculate mid 
if mid == target:
    if mid == 0:
        set left bound as mid 
    elif mid - 1 not target:
        set left bound mid

if target <= mid:
    right = mid
else:
    left = mid
    


# Find Right bound range 
if left bound != -1
Run binary search for left bound from left index to end
while left <= right
calculate mid
if mid == target:
    if mid == len(nums) - 1:
        set right bound as mid 
    elif mid + 1 not target:
        set right bound mid

if target <= mid:
    left = mid
else:
    right = mid


return [left bound, right bound]

 l     m     r
         l m r
             l  left = 6
             
[0,1,1,1,1,1,2] target 2


 l     m     r 
 l m r          left_bound = 2
     s   m   e 
           lm e  right_bound = 5
[0,0,1,1,1,1,2] target = 1
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_bound = -1
        right_bound = -1
        
        left = 0
        right = len(nums) - 1
        # Find left bound range
       
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0:
                    left_bound = mid
                elif nums[mid - 1] != target:
                    left_bound = mid

            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # No target bound found
        if left_bound == -1:
            return [left_bound, right_bound]

        # Find Right bound range 
        start = left_bound
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    right_bound = mid
                elif nums[mid + 1] != target:
                     right_bound = mid

            if target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1 


        return [left_bound, right_bound]
