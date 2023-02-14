# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Workflow Timestamps
1. 0:00 - 3:41 Make Sure You Understand the Problem
2. 3:41 - 7:50 Design a Solution / Runtime and Space Complexity
3. 7:50 - 13:50 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 13:50 - 36:55 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

Test cases:
1.) head = [1*, 2, 3*], 3 points to 1
return 0

2.) head = []
    return 

3.) head [1**], 1 points to 1
    return 0
2. Design a Solution / Runtime and Space Complexity
Pointer that increments by  1. Store each node in map as key:value pair id(node): node. 
If node is is ever in map return node, else return.

Runtime: O(N)
Space complexity: O(1)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Check for empty list
    if not head:
        return
    
    cur = head
    node_ids = {}

    while cur:
        #add cur node to map 
        map.add(cur.id)

        cur = cur.next 

        # Check if fast node id is in map
        if id(cur) in map:
            return map[cur]

    return None

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check for empty list 
        if not head:
            return 
        
        cur = head
        node_ids = {}

        while cur:
            # Add node to map
            node_ids[id(cur)] = cur

            cur = cur.next 
    
            if id(cur) in node_ids:
                return node_ids[id(cur)]
            
        return 