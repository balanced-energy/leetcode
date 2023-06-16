# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Two pointers
Start both at a dummy node
Move first to n + 1 nodes ahead
Then once end pointer hits null 
first pointer is at node previous to the node to delete

n = 2
length = 5
move to 5 - 2 node = 3
remove
     p
[1,2,3,4,5]

n = 1
length = 1 
move to 1 - 1 = 0
remove  
[1]
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for i in range(n + 1):
            fast = fast.next
        
        # Move each pointer forward until fast == None
        while fast != None:
            slow = slow.next
            fast = fast.next
        
        # Remove node following slow pointer
        slow.next = slow.next.next
        
        return dummy.next
        