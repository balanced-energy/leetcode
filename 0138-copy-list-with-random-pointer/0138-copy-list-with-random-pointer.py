'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
random pointer represents the index of the node

[[7,null],[13,0],[11,4],[10,2],[1,0]]

[[7,None],[13],[11],[10],[1]]

node_index = {0:[7],1:[13],2:[10],3:[1]}


head_copy = Node(head.val)
cur_copy = head_copy

# First traversal copy values and save index 
set cur to head.next
idx = 0
while cur:
    # Create copy of cur.next if not null
    if cur.next is not None:
        cur_copy.next = Node(cur.next.val)
    else:
        cur_copy.next = None
        
    # save index 
    node_index[idx] = copy_cur
    idx += 1
   
   # move pointers
    cur = cur.next
    cur_copy = cur_copy.next 
    
# Traverse copied list setting random pointer
cur = head
cur_copy = head_copy
while cur:
    if cur.random is not None:
        cur_copy.random = node_index[cur.random]
    else:
        cur_copy.random = None
    # move pointers
    cur = cur.next
    cur_copy = cur_copy.next 
return copy_head
    
    
2. Design a Solution / Template / Runtime and Space Complexity
- map to store node index
- Create copy of head
- Traverse nodes creating new nodes with same values and saving index in map
- Second pass handle random pointer indices 
3. Write the Code And Pass Test Cases.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        head_copy = Node(head.val)
        cur_copy = head_copy
       
        node_to_node_copy = {head:head_copy}
        # First traversal copy values and save index 
        cur = head 
        while cur:
            node_to_node_copy[cur] = cur_copy
            # Create copy of cur.next if not null
            if cur.next is not None:
                cur_copy.next = Node(cur.next.val)
                
            else:
                cur_copy.next = None

           # move pointers
            cur = cur.next
            cur_copy = cur_copy.next 

        # Traverse copied list setting random pointer
        cur = head
        cur_copy = head_copy
        while cur:
            if cur.random is not None:
                cur_copy.random = node_to_node_copy[cur.random]
            else:
                cur_copy.random = None
            # move pointers
            cur = cur.next
            cur_copy = cur_copy.next 
        
        return head_copy