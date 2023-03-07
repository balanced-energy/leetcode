'''
Workflow Timestamps
1. 0:00 - 12:25 Make Sure You Understand the Problem
2. 12:25 - 24:00 Design a Solution / Runtime and Space Complexity
3. 24:00 - 31:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
n = [1,2,3,4,5] bad = 4
left = 0, 3, 4
right = 5, 5, 5

n = [1,2,3,4,5] bad = 3

n = [1,2,3,4,5] bad = 2

n=[1]
2. Design a Solution / Runtime and Space Complexity
-Have two pointers used to calculate a mid value. Check mid to see if it's bad or not.
-If isBadVersion(mid) is true and isBadVersion(previous element) is false, then we can return mid as first bad version.
    otherwise we need to check previous elements for an earlier bad version by moving right to mid
-If isBadVersion(mid) is false then we know the first bad version is to the right of mid, move left to mid+1

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

left and right pointers starting at 0, n

while left less than or equal to right. 
calculate mid, 
# Mid is bad
if isBadVersion(mid)
    # Versions start at 1 
    if mid == 1:
        return 
    if not isBadVersion(mid-1): 
        return mid 
    else then set right as mid
# Mid is good 
else
    left = mid 

# Mid is not bad 
4. Write the Code And Pass Test Cases.

n = 1,2,3,4,5 - bad = 4
n = 1,2,3,4,5 - bad = 2
n = 1,2 - bad = 2
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
   
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            # mid is bad
            if isBadVersion(mid):
                # Mid is first element, therefore first bad version
                if mid == 1:
                    return mid
                
                # If previous element is good then mid is first bad
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1
            # mid is good so first bad to the right
            else:
                left = mid + 1
                
                