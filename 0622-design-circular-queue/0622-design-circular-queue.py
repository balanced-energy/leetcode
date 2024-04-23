'''
Understand the problem


Design a solution
Using list enqueue items making sure to % by capacity to handle circular functionality 
dequeue by moving head to next index also taking into account % capacity
isempty / isfull simply checks size attribute versus capacity 
rear / front returns item at head and tails

- init 
    q = [0] * k
    cap = k
    size = 0
    head = 0
    lock = Lock()
    
- enqueue
    - if isFull:
        return False
    
    with lock
        q[(head + size) % capacity] = value
        size += 1

        return True


- dequeue
    if isEmpty:
        return False
        
    head = (head + 1) % capacity 
    size -= 1
    
    return True
    
- front:
    if isEmpty:
        return -1
        
    return q[head]
    
- rear:
    if isEmpty
        return -1
    return q[(head + size - 1) % capcacity]
    
- isEmpty
    return size == 0
    
- isFull 
    return size == capacity


[4,2,3]
h=0,1
s=0,1,2,3,2,3
c=3

Runtime: O(1)
Space: O(N)
'''
from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.capacity = k
        self.size = 0
        self.head = 0
        self.lock = Lock()
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        with self.lock:
            self.q[(self.head + self.size) % self.capacity] = value
            self.size += 1
            
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[(self.head + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()