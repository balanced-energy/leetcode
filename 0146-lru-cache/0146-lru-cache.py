'''
Mock - 45m
Workflow Timestamps
1. 3:00 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
Using a deque to store order of keys and hashmap for O(1) get/put access time.

(1)<->(2)

class Node:
    __init__(self, val):
        self.val = val
        next = None
        prev = None

class DoublyLinkedList:
    __init__(self):
        head = Node('Head')
        tail = Node('Tail')
        
    # Front least recently used
       
    (1)<->(2)<->(3)
    add_back(val):
        node = Node(val)
        tail.prev.next = node
        node.prev = tail.prev
        node.next = tail
        tail.prev = node
            
        (2)
    (1)<->(3)
    delete(node):
        prev_last = node.prev
        prev_last.next = node.next
        node.next.prev = prev_last
    
    move_to_back:
        delete(node)
        add_to_back(node)
    
intit:
    d = doublylinkedlist()
    keys = {key:node}

get:
    if key in keys:
        node = keys[keys]
        return node.val
    
    # Update order by moving to back
    move_to_back(node)
    
    return -1
    
    
put:
    # If key exists update nodes value
    if key in keys:
        node = keys[key]
        node.val = val
        
    
    else:
        create node with value
        add key:node to map
        add node to back of deque
    
    if capacity exceeded
    remove front node from deque
    

3. Write the Code And Pass Test Cases.
'''
class Node:
    def __init__(self, val):
        self.key = None
        self.val = val
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node('Head')
        self.tail = Node('Tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    # Front least recently used   
    #(1)<->(2)<->(3)
    def add_to_back(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
            
   #     (2)
   # (1)<->(3)
    def delete(self, node):
        #prev_last = node.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def move_to_back(self, node):
        self.delete(node)
        self.add_to_back(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.d = DoublyLinkedList()
        self.keys = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        # Get node and update position
        node = self.keys[key]
        self.d.move_to_back(node)
        
        return node.val
        
        
    def put(self, key: int, value: int) -> None:
        # If key exists update nodes value
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            # Update order by moving to back
            self.d.move_to_back(node)
    
        else:
            new_node = Node(value)
            new_node.key = key
            self.keys[key] = new_node
            self.d.add_to_back(new_node)
    
        
        if self.d.size > self.capacity:
            front_node = self.d.head.next
            self.d.delete(front_node)
            del self.keys[front_node.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)