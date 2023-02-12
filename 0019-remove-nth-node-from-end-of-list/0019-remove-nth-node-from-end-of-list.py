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
- Use two pointers to traverse through linked list. First pointer is n distance from second pointer.
- When the second pointer reaches the end of the list (value of None), first pointer will be at node to remove.
- Remove node by updating cur.prev = cur.next and cur.next = cur.prev.

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


Example 4:
Input: head = [], n = 1
Output: []

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


Edge Cases: 
head = [] return []

Runtime Complexity: O(N) traversing list once
Space Complexity: O(1) updating pointers

Step 3: Write template
# In step 4 running code found out can't check for list length because head is Node object not a list.
if len(head) <= 1: 
    return []

# point to Node objects
p1 = 0
p2 = head[n]

# Traverse to end of list until p2 is None
while p2:
    p1 += 1
    p2 = p2.next

# Remove p1 Node, need p1 to be int to then access previous node, check index
if p1.next:
    head[p1 - 1].next = head[p1].next
# Handle 1 Node head = [1], p1 = 0, return []. Handle in check at beginning?
else:    
# If p1.next is None, point p1-1 to None
    head[p1 -1].next = None

return head


[1, 2, 3], n = 2
p1 = 0
p2 = head[2]

while loop:
    end
p1 = 1
head[0].next = head[2]
return [1, 3]

Example 2:
Input: head = [1], n = 1
Output: []

p1 = 0
p2 = 1
# Loop never runs
while p2:
    end
p1 = 0
# When removing, check length before assigning pointers
For this example, fixed check to return [] if length = 1

Example 3:
Input: head = [1, 2], n = 1
Output: [1]

p1 = 0
p2 = 1
while p2:
    end
p1 = 1

# Remove p1, check if p1.next, else point p1 - 1 to None
head[0].next = None
'''

'''
Implementation Notes:
head is a Node object not list.
Can't subscript head[]
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Check if LinkedList is empty or only has 1 Node
        if head is None or head.next is None:
            return
        
        # Initialize pointers with p2 n position ahead, track prev node
        p0 = head
        p1 = head
        p2 = head


        # Point p2 to nth Node
        for i in range(n):
            p2 = p2.next
        
        count = 0
        while p2:
            if count == 0:
                p1 = p1.next
                p2 = p2.next
            else:
                p0 = p0.next
                p1 = p1.next
                p2 = p2.next
            count += 1

        # Edge case [1, 2], n = 2
        '''
        After for loop to Initialize p2 position
        n = 2
        p0 = head
        p1 = head
        p2 = None

        while loop doesn't run
        '''
        
        # p1 is Node to delete, check if next Node exists
        # p0 is pointer to prev Node to handle deletion
      
        print(f'p0:{p0.val}, p1:{p1.val}, p2:{p2}')
        
        # if p0 == p1 while loop didn't run
        # [1, 2], n = 2
        if p0 == p1:
            if n == 1:
                return p0
            # n == 2
            else:
                return p0.next

        if p1.next:
            p0.next = p1.next
        #[1, 2], n = 1 -> [1]
        else:
            p0.next = None
        
        return head
