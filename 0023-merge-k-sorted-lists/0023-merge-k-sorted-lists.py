'''
Workflow Timestamps
1. 0:00 - 2:00 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[[1,4,5],[1,3,4],[2,6]]

2. Design a Solution / Runtime and Space Complexity
Add all elements to min heap. then pop off adding to output list
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
minheap = []
out = []
for list in lists:
    for num in lists:
    heapq.heappush(minheap, num)
    
while minheap:
    out.append(heapq.heappop(minheap))
4. Write the Code And Pass Test Cases.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        dummy = ListNode(float('inf'))
        
        for l in lists:
            if l:
                cur = l
                while cur:
                    heapq.heappush(minheap, cur.val)
                    cur = cur.next
        # All values in heap
        prev_node = dummy
        
        # Create new list in ascending order
        while minheap:
            cur = ListNode(heapq.heappop(minheap))
            prev_node.next = cur
            prev_node = cur                               
        
        return dummy.next