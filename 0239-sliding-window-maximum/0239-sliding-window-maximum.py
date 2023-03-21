
'''
1. Make Sure You Understand the Problem
[1  3  -1] -3  2  4  6  1       3,3,2,4,6,6


2. Design a Solution / Runtime and Space Complexity
Use a monotonic deque. This allows us to process elements in order and compare each element to top of deque. 
Check if new element to add is greater than or eqaul last element in deque. Pop elements while this is true. append new element

This keeps the invariant of decreasing values on the deque, allowing us to access the max value.
We store the elements index in the deque and then can access the value from the input array.

check if we need to remove max element because it's now outside window.
we do this by comparing d[0] == i - k, if so then d.popleft()

Check if the window is at least size k. Once it is and previous checks have been done we add first element of deck to output.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    d = deque
    
    for i, num in nums:
        while d and nums[d[-1]] <= num:
            remove last element
        add new num index to deque
        
    check if max element is outside window
    if first element on deque == i - k:
        pop left from deque
        
    If we have at least k elements add first element to output
    
    if i >= k - 1:
        out.append(nums[d[0]])
        
4. Write the Code And Pass Test Cases.
'''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        
        out = []
        
        for i, num in enumerate(nums):
            # keep monotonic deque invariant by ensuring decreasing order
            while d and nums[d[-1]] <= num:
                d.pop()
                
            # Add index of next order element
            d.append(i)
        
            # Check if max element is removed from window
            if d[0] == i - k:
                d.popleft()
                
            # Check if at least k elements then add max to output
            if i >= k - 1:
                out.append(nums[d[0]])
                
        return out