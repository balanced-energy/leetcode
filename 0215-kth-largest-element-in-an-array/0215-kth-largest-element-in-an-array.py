'''
Mock - 45m
Workflow Timestamps
1. 1:00 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

nums = [3,2,1,5,6,4], k = 2

heap [5,6]

2. Design a Solution / Template / Runtime and Space Complexity

    
- Add all nums to a minheap
- pop off elements until minheap is size k
- return top element of heap  


if len(nums) == 1:
    return nums[0]

elements = nums[::]

heapq.heapify(elements)

while len(minheap) > k:
    heappop(elements)
    
    n-1 log(n)
    
3. Write the Code And Pass Test Cases.
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        elements = nums[::]

        heapq.heapify(elements)

        while len(elements) > k:
            heapq.heappop(elements)
            
        return elements[0]