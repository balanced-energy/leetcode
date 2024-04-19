'''
2:00 Understand the problem



24:00 Design a solution
h[1,2]t

Node:
    key
    val
    next
    prev
    
Cache
init
    cap
    nodes = {}
    head
    tail
    point head and tail to each other
    
# Remove node from list
(1)-><-(2)-><-(3)

delete(node)
    node.prev.next = node.next
    node.next.prev = node.prev

# add to end of list
h[1,2]t
add(node)
    tail.prev.next = node
    node.next = tail
    node.prev = tail.prev 
    tail.prev = node
    
get 
    if key in nodes:
        node = self.node[key]
        delete(node)
        
        add(node)
        return node.val
    return -1
    
put
    if key in nodes:
        node = self.nodes[key]
        delete(node)
        
        new_node = Node(key, val)
        self.node[key] = new_node
        add(node)
        
    else:
        node = Node(key,val)
        self.nodes[key] = node
        add(node)
        
        if len(self.nodes) > self.cap:
            node = head.next
            delete(node)
            del self.nodes[node.key]
            
{3:3, 4:4}
h[3,4]t

Runtime: O(1)
Space: O(capacity)

Implement
'''

class Node():
    def __init__(self, key, val, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.nodes = {}
        self.head = Node('head','head')
        self.tail = Node('tail','tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    
    def add(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev 
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodes:
            node = self.nodes[key]
            self.delete(node)
            self.add(node)
            return node.val
        
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nodes:
            node = self.nodes[key]
            self.delete(node)

            new_node = Node(key, value)
            self.nodes[key] = new_node
            self.add(new_node)
        
        else:
            node = Node(key,value)
            self.nodes[key] = node
            self.add(node)

            if len(self.nodes) > self.capacity:
                node = self.head.next
                self.delete(node)
                del self.nodes[node.key]

{2:2,}
[2,]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)