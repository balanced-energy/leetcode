'''
7:00 Understand the problem

insertFront on empty deque
h><t
h><1><t

remove last element
h><1><t
h><t

delete front
h><1><2><3><t
h><2><3><t

34:00 Design a solution
Using doubly linked list to create deque

Node(val, prev=None, next=None)
    val
    next 
    prev
    
h><t
- init 
    capacity = k
    size = 0
    head = Node('Head')
    tail = Node('Tail')
    head.next = tail
    tail.prev = head

h><3><t
- insertFront(value)
    if isFull:
        return False
  
  new_node = Node(val)
  old_head_node = head.next 
  
  new_node.prev = head
  new_node.next = old_head_node
  head.next = new_node
  old_head_node.prev = new_node
  
  size += 1
  
  return True

h><1><2><t
-insertLast(val)
     insertFront(value)
        if isFull:
            return False
  
        new_node = Node(val)
        old_tail_node = tail.prev 

        new_node.next = tail
        new_node.prev = old_tail_node
        tail.prev = new_node
        old_tail_node.next = new_node
        
        size += 1
          
        return True
    
h><1><2><t
- deleteFront
    if isEmpty()
        return False
    
    old_head = head.next
    head.next = old_head.next 
    old_head.next.prev = head
    
    size -= 1
    
    return True

h><2><t
- deletelast
    if isEmpty()
        return False
    
    old_tail_node = tail.prev
    tail.prev = old_tail_node.prev 
    old_tail_node.prev.next = tail
    
    size -= 1
    
    return True
    
- getFront
    
    
- getRear()
    if isEmpty()
        reuturn -1
        
    return self.tail.prev.val
    
-isEmpty()
    return self.size == 0
    
- isFull()
    return self.size == self.capacity 


h><3><1><t
old_head = 3

Runtime: O(1)
Space: O(N)

Implement
'''

class Node():
    def __init__(self, val, prev=None, nxt=None):
        self.val = val 
        self.prev = prev
        self.next = nxt
    
class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = Node('Head')
        self.tail = Node('Tail')
        self.head.next = self.tail
        self.tail.prev = self.head


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
  
        new_node = Node(value)
        old_head_node = self.head.next 

        new_node.prev = self.head
        new_node.next = old_head_node
        self.head.next = new_node
        old_head_node.prev = new_node

        self.size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
  
        new_node = Node(value)
        old_tail_node = self.tail.prev 

        new_node.next = self.tail
        new_node.prev = old_tail_node
        self.tail.prev = new_node
        old_tail_node.next = new_node
        
        self.size += 1
          
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        old_head_node = self.head.next
        self.head.next = old_head_node.next 
        old_head_node.next.prev = self.head

        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        old_tail_node = self.tail.prev
        self.tail.prev = old_tail_node.prev 
        old_tail_node.prev.next = self.tail

        self.size -= 1
        
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()