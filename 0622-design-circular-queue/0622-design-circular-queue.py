'''
4:50 Understand the problem
FIFO (First In First Out)

init2
e1
head = 0
size = 1

e2
head = 0
size = 2

[1,2] 
deque
head = 1
size = 1
[ ,2]
eq 3

[3, 2]
head = 1
size = 2
deque 
false


[1,2,3]
[1,2,3,4] want idx 3
h=0
size=4
cap=4
[None,2,3]
[None,2,3,4]


Design a solution
Using a list and % operator to circle back around


- init 
    q = [0]*k
    capacity = k
    size = 0
    head = 0 
    
    
- enqueue(val)
    - isFull return false
    - self.q[head + size % capacity] = val 
    - self.size += 1
    

- dequeue
    - if isEmpty return false
    -  head = head + 1 % cap
    - self.size -= 1

- isEmpty
    return size == 0
    
- isFull
    reutrn size == cap
    
- front
    - if isEmpty
        return -1
    return self.q[head]
    
- rear 
    if isEmpty
        return -1
    return self.q[head + size -1] % cap
    
    
    
[4,2,3]
cap=3
head=0,1
size=3,2,3

Runtime: O(N)
Space: O(N)

'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.head = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
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