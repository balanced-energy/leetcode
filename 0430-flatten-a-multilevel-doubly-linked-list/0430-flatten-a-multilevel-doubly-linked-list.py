"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

'''
1-None
|
2-None
'''

def _flatten(head):
    
    cur = head
    while cur:
        next_node = cur.next 
        if not next_node:
            tail = cur
            
        if cur.child:
            cur.next = cur.child
            cur.child.prev = cur
            
            child_tail = _flatten(cur.child)
            
            if next_node:
                next_node.prev = child_tail
            
            child_tail.next = next_node 
            
            cur.child = None
            
        cur = cur.next
        
    return tail
    
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        _flatten(head)
     
        return head