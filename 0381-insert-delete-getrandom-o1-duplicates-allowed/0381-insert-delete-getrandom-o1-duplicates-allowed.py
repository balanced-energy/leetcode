'''
Mock - 45m
Workflow Timestamps
1. 2:10 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
Have a threshold when to refresh index and values map.

values = {val:index}
indices = {index:val} 

values = {1:0, 1:1, 2:2}
indices = {0:1, 1:1, 2:2}

init:
    values = {}
    indices = {}
    idx_count = 2
    
insert:
    add val:idx_count to values
    add idx_count:value to indices
    
    if val in values:
        return False
   
   return True
    
remove:
    if in values:  
        index = values[val]
        del indices[index]
        del val from values
        
        # Check threshold for refreshing
        if idx_count // len(indices) >= 2:
            
            # Refresh maps
            new_idx = 0
            for key,val in indices:
                indices[new_idx] = val
                values[val] = new_idx
                new_idx += 1
                
        return True
        
    return False

getRandom():
 while True:
    get random int from 0 -> n
    if int in indices:
        return indices[n]

 
 
3. Write the Code And Pass Test Cases.
'''
import random
class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]: return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True
    
    def getRandom(self) -> int:
         return choice(self.lst)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()