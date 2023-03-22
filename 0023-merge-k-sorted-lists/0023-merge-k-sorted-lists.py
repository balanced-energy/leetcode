'''
Workflow Timestamps
1. 0:00 - 2:00 Make Sure You Understand the Problem
2. 2:00 - 19:51 Design a Solution / Runtime and Space Complexity
3. 19:51 - 22:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 22:00 - 34:31 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[[1,4,5],[1,3,4],[2,6]]

2. Design a Solution / Runtime and Space Complexity
Add all node values to min heap. Then pop off and create new linked list from each value.
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
minheap = []
dummy = node
for l in lists:
    if l:
        cur = l 
        while cur:
            push node value to heap
            move to next node

# All node values in heap so pop them while creating new linked list
prev = dummy
while minheap:
    cur = Node(heapq.heappop(minheap))
    prev.next = cur
    prev = cur
    
return dummy.next
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