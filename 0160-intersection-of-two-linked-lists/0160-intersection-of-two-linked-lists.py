# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Workflow Timestamps
1. 0:00 - 6:45 Make Sure You Understand the Problem
2. 6:45 - 13:25 Design a Solution
3. 13:25 - 20:20 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 20:20 - 40:29 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
* = intersect value

Test 1:
listA = [1, 2, 3*]
listB = [3*, 4, 5]
output = node 3

Test 2:
listA = [3*]
listB = [1, 2, 3*]
output = node 3

Test 2:
listA = []
listB = [1, 2, 3]
output = null

2. Design a Solution
1.) Check if either list is empty. 
2.) Created a map of {node: node.id()} for first list. 
3.) Compare second list nodes against values in map. If found return node 


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Check if either list is empty. 
    if not l1 or not l2:
        return None 

    # Created a map of {node: node.id()} for first list. 
    node_id = {}
    cur_a = headA
    while cur_a:
        node_id[cur_a] = id(cur)
        cur_a = cur_a.next 
    
    # node_id contains node: id of nodes in list a
    # Traverse through nodes of list B
    # Compare second list nodes against values in map. If found return node 
    cur_b = headB
    while cur_b:
        if id(cur_b) in node_id:
            return cur_b
        cur_b = cur_b.next
    
    return None


len(list_a) = N
len(list_b) = M
Runtime: O(N + M)
Space complexity: O(1)

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # Created a map of {node: node.id()} for first list. 
        node_id = {}
        cur_a = headA
        while cur_a:
            node_id[id(cur_a)] = cur_a
            cur_a = cur_a.next 

        # Compare second list nodes against values in map. If found return node 
        cur_b = headB
        while cur_b:
            # Intersection node found
            if id(cur_b) in node_id:
                return cur_b
            cur_b = cur_b.next
        
        return None