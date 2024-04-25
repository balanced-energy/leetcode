'''
Understand the problem
                     1
l1 = [9,9,9,9,9,9,9], 
l2 = [9,9,9,9]
res: [8,9,9,9,0,0,0,1]


[1,2,3]
[1]
[2,2,3]

[1]
[1,2,3]
[2,2,3]

   1 1 1
[9,9,9] -> 999
[1,1,1] -> 111
[0,1,1,1] -> 1110

     1
[9,9]
[1]
d>0,0>1
Design a solution
- carry variable init to 0, 
- dummy node to return resulting sum list
- curr pointer to build resulting sum list init to dummy

- Traverse l1 and l2 nodes until l1 != None or l2 != None or carry != 0
- check if l1 and l2 nodes, if nodes set l1_val and l2_val else make them 0
- nodes_sum will be set to l1_val + l2_val + carry
- carry = nodes_ sum // 10 
- Create new node with value nodes_sum % 10
- Set curr.next to the new node
- Move curr to new node
- check if l1.next and l2.next and move pointers, else set them to None

- return dummy.next 


l1 =  [2,4,3], 
l2 =  [5,6,4]
res= d[]

carry = 0,1,0
l1 = 2,4,3 
l2 = 5,6,4
curr = dummy,7,0,8
dummy = dummy>7>0>8

m = len(l1)
n = len(l2)

Runtime: O(max(m, n))
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode('Dummy')
        curr = dummy 
        
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            nodes_sum = l1_val + l2_val + carry
            carry = nodes_sum // 10
            
            new_node = ListNode(nodes_sum % 10)
            curr.next = new_node 
            curr = new_node
            
            # Move pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next 