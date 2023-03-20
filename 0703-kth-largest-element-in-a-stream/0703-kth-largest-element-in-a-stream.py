'''
Workflow Timestamps
1. 0:00 - 1:30 Make Sure You Understand the Problem
2. 1:30 - 8:00 Design a Solution / Runtime and Space Complexity
3. 8:00 - 11:45 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[3, [4, 5, 8, 2]]

 2 [-1, 0], [-1]
 
    0
    
2. Design a Solution / Runtime and Space Complexity
Create a minheap of size k if we can, else if nums list is shorter add all elements

# Add
if len(heap) < k 
    heappush val
else
    if val greater than top element of heap. 
    Pop off smallest then add new value with heapreplace.

return first element
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
#init
    heap list
    add k lements to list with heappush
    
    for i in range k to end of nums list
        #add nums[i]
    
#add
    check if greater than top element
    if less than, heapreplace negative val
    return heap[0]
    
4. Write the Code And Pass Test Cases.
'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.max_size = k
        for num in nums:
            heapq.heappush(self.max_heap, num)
            
            if len(self.max_heap) > self.max_size:
                heapq.heappop(self.max_heap)  
    def add(self, val: int) -> int:
        
        heapq.heappush(self.max_heap, val)
        if len(self.max_heap) > self.max_size:
            heapq.heappop(self.max_heap)
        
        return self.max_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)