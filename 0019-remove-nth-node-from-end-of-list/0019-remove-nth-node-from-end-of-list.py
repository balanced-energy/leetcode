# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Step 1: Understand the problem, create test cases
Test Cases:

Example 4:
Input: head = [], n = 1
Output: []

Example 5:
Input: head = [1, 2, 3], n = 3
Output: [2, 3]

Example 6:
Input: head = [1, 2, 3], n = 2
Output: [1, 3]

Step 2: Design a solution (no code)

Outline: 
- Use two pointers to traverse through linked list. First pointer is n + 1 distance from second pointer.
- When the second pointer reaches the end of the list (value of None), first pointer will be at node previous from node to remove.
- Remove node by updating cur.next = cur.next.next

Test solution:
Example 1:
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
p1 = 0, 1, 2, 3
p2 = 2, 3, 4, 5

p1 = Node 4, removing would return [1, 2, 3, 5]


Example 2:
Input: head = [1], n = 1
Output: []

p1 = 0
p2 = 1
p2 starting outside of list length so p2 starts = None

p1 = Node 1, removing would return []


Example 3:
Input: head = [1, 2], n = 1
Output: [1]

p1 = 0, 1, 2
p2 = 1, 2, 3

p1 = Node 2, removing would return [1]


Check for empty list: return []
p1 = 0
p2 = 1


Example 5:
Input: head = [1, 2, 3], n = 3
Output: [2, 3]

Example 6:
Input: head = [1, 2, 3], n = 2
Output: [1, 3]

p1 = 0, 1
p2 = 2, 3

p1 = Node 2, removing would return [1, 3]


Runtime Complexity: O(N) traversing list once
Space Complexity: O(1) updating pointers

Example 3:
Input: head = [d, 1], n = 1
Output: [1]
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize dummy node to help with edge cases of deleting head and only one node and two node pointers
        dummy = ListNode('Dummy')
        dummy.next = head
        front_node = dummy
        back_node = dummy
        
        # Move front_node n + 1 positions from back node
        for i in range(n+1):
            front_node = front_node.next
            
        # Move node_2
        while front_node:
            front_node = front_node.next
            
            back_node = back_node.next
            
        # Back node is at node previous to the node to be deleted
        back_node.next = back_node.next.next
        
        # Handle deleting head by returning dummy.next and not head
        return dummy.next
            
            
            
        
