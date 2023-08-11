'''
Class constructor
    Intialize minheap as class member variable
    Push all elements onto minheap from input list 
    Pop off elements until heap is of size k 
    Heap now tracks the kth largest element being the first element in the heap
Add method
    Add element to heap
    If size of minheap is greater than k
    Pop off an element from minheap leading back to a minheap of size k 
    We know the add element only takes 1 element as input, however, if we wanted to adjust this to handle       multiple elements as input it would follow the same procedure during the initialization of the class and probably warrant creating a function that adds all elements to the minheap, and then pops off elements     until it’s equal to size k. I suppose we could still create this separate function and use it within         add, but that may add more complexity versus keeping things clean and simple since add only ever adds 1 element.
    Return top element from heap
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.size = k
        
        # add all elements onto heap
        for num in nums:
            heapq.heappush(self.minheap, num)
            
        # Reduce heap to size k
        while len(self.minheap) > self.size:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        
        if len(self.minheap) > self.size:
            heapq.heappop(self.minheap)
        
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)