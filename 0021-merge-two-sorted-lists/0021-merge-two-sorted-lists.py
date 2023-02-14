# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Workflow Timestamps
1. 0:00 - 3:30 Make Sure You Understand the Problem
2. 3:30 - 8:50 Design a Solution
3. 8:50 - 25:40 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 25:40 - 37:39 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
Test 1:
l1 = [1, 2], l2 = [2, 3, 4]
out = [1, 2, 2, 3, 4]

Test 2:
l1 = [0], l2 = [-1, 2, 3]
out = [-1, 0, 2, 3]


2. Design a Solution
if both empty return empty list
if one list is empty, return other list
Two pointers, one for each list. Compare each node value, appending lower value to output list, incrementing node of the list that the lower value node was taken from. If equal take l1 node and increment. When one of the pointers is None, append rest of other list.

Test 1:
l1 = [1, 2], l2 = [2, 3, 4]
out = [1, 2, 2, 3, 4]

p1 = 1, 2, None
p2 = 2,3,4
out = None, [1, 2, 2, 3, 4]

Test 2:
l1 = [0], l2 = [-1, 2, 3]
out = [-1, 0, 2, 3]

p1 = 0, None
p2 = -1, 2
out = None, [-1, 0, 2, 3]


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
#if both empty return empty list
if not list1 and not list2:
    return []
# if one list is empty, return other list
elif not list1:
    return list2
elif not list2:
    return list1

p1 = list1
p2 = list2

# List 3 head and cur_node 
list3 = None
cur_3 = None

while p1 and p2:
    # p1 <= p2
    if p1 <= p2:
        new_node = ListNode(p1.val)
        if not list_3:
            list_3 = new_node
            cur_3 = new_node
        else:
            cur_3.next = new_node
        p1 = p1.next
    
    # p2 < p1
    else: 
    new_node = ListNode(p2.val)
     # Handle empty list_3
        if not list_3:
            list_3 = new_node
            cur_3 = new_node
    # Add node to end of list_3
        else:
            cur_3.next = new_node
        p2 = p2.next
    
    

# handle remaining list 

if p1:
    append rest of list

else:
    append rest of p2


4. Write the Code And Pass Test Cases.

l1 = [1,2,4]
l2 = [1,3,4]

p1 = 1,2
p2 = 1,
list_3 = None, Node(1)
cur_3 = None, Node(1)
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if both empty return empty list
        if not list1 and not list2:
            return 
        # if one list is empty, return other list
        elif not list1:
            return list2
        elif not list2:
            return list1

        p1 = list1
        p2 = list2

        # List 3 head and cur_node 
        list_3 = None
        cur_3 = None

        while p1 and p2:
            # p1 <= p2
            if p1.val <= p2.val:
                new_node = ListNode(p1.val)
                if not list_3:
                    list_3 = new_node
                    cur_3 = new_node
                else:
                    cur_3.next = new_node
                    cur_3 = new_node
                p1 = p1.next
            
            # p2 < p1
            else: 
                new_node = ListNode(p2.val)
            # Handle empty list_3
                if not list_3:
                    list_3 = new_node
                    cur_3 = new_node
            # Add node to end of list_3
                else:
                    cur_3.next = new_node
                    cur_3 = new_node
                p2 = p2.next
            
            

        # handle remaining list 

        if p1:
            while p1:
                new_node = ListNode(p1.val)
                cur_3.next = new_node
                cur_3 = new_node
                p1 = p1.next

        else:
            while p2:
                new_node = ListNode(p2.val)
                cur_3.next = new_node
                cur_3 = new_node
                p2 = p2.next

        return list_3