'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
[1] -> [1]

 f   e
[1,3,2]
  f   e
[(1),(2),(3)]



Even number of nodes
 f         e
[1,2,3,4,5,6] -> [1,6,2,5,3,4]
         f 
[1,6,2,5,3,4]
          f   e
[(1),(2),(3),(4),(5),(6)]

 f          
[1,2,3,4,5]

Get current end node
decrement end pointer
Detach end node in linked list
Insert after front pointer node in linked list
increment front in nodes aux list 
loop ends when front.next = end pointer

Odd number of nodes
[1,2,3,4,5] -> [1,5,2,4,3]
     f
[1,5,2,4,3]
          f               e
nodes = [(1),(2),(3),(4),(5)]
Get current end node
decrement end pointer
Detach end node in linked list
Insert after front pointer node in linked list
increment front in nodes aux list 
loop ends when front == end pointer 

end when front.next == end or front == end 


2. Design a Solution / Template / Runtime and Space Complexity
 - Traverse linked list create aux nodes list with pointers to each node
    - set front and end pointers 
 - while front.next != end pointer and front != end ponter in aux nodes list 
    - get current end node
    - decrement end pointer in aux nodes list
    - insert end node after front pointer in linked list
    - increment front node pointer in aux nodes list

- return head 

[1,34,2,]
3. Write the Code And Pass Test Cases.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Create aux nodes list with pointers to each node, set front, end pointers
        # Initialize aux nodes list and set front pointer
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next 
            
        front = 0
        end = len(nodes) - 1
        
        while front != end and front + 1 != end:
            # Get end node and decrement 
            end_node = nodes[end]
            end  -= 1
            
            # Detach removed node 
            nodes[end].next = None
            
            # Insert after front node pointer
            front_node = nodes[front]
            end_node.next = front_node.next
            front_node.next = end_node
            front += 1
            
        return head
            
        
        