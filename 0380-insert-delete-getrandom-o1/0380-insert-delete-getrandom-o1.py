
'''
Workflow Timestamps
1. 0:00 - 2:00 Make Sure You Understand the Problem
2. 2:00 - 9:00 Design a Solution / Runtime and Space Complexity
3. 9:00 - 14:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 14:00 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
- Create a map of values to index {val:idx} and a list of values 
- When inserting if value in map is return false, else add to map and values list 
- When removing, if value not in map return false, 
else get index from map and use it to swap last element in list with this index then pop from list.
- get random chooses random element from list


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize set and map
values_to_index = {}
values_list = []


# Insert
if val exists in values map, 
return false, 
else 
add to values_to_index
add to values_list

return true

# Remove
if not in values_to_index 
return false
else 
pop index of value from values_to_index
swap value at values_list[index] with ending element
pop from list

return true

# Get random
use random choice to choose from list


4. Write the Code And Pass Test Cases.
'''
import random

class RandomizedSet:

    def __init__(self):
        # Initialize set and map
        self.values_to_index = {}
        self.values_list = []
       

    def insert(self, val: int) -> bool:
        if val in self.values_to_index:
            return False
        
        # Add val:index to map
        self.values_to_index[val] = len(self.values_list)
        self.values_list.append(val)
        
        return True
   
    def remove(self, val: int) -> bool:
        if val not in self.values_to_index:
            return False

        # Get last value, pop from map and get index
        last_val = self.values_list[-1]
        del_index = self.values_to_index[val]
        
        # Place last value in index to delete, update index in map
        self.values_list[del_index] = last_val
        self.values_to_index[last_val] = del_index
        
        # Remove from map and list
        del self.values_to_index[val]
        self.values_list.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.values_list)
    
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()