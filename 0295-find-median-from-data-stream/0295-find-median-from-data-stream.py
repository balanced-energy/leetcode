'''
Workflow Timestamps
1. 0:00 - 1:35 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[5,1,7,4,9] -> [1,4,5,7,9]


        


2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''

class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        # Add to max heap lo
        heapq.heappush(self.lo, -num)
        
        # Pop from low and add to hi
        heapq.heappush(self.hi, -heapq.heappop(self.lo))

        
        # If length hi > lo push back to lo to keep balanced
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
            
    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        
        return (-self.lo[0] + self.hi[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()