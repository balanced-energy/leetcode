'''
Workflow Timestamps
1. 0:00 - 3:05 Make Sure You Understand the Problem
2. 3:05 - 14:25 Design a Solution / Runtime and Space Complexity
3. 14:25 - 19:05 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

2. Design a Solution / Runtime and Space Complexity
- Initialize a map of char: string 
- Turn pattern string into a list
- Get a list of strings from our input string calling s.split(). 
- For each char starting from end of pattern list: char will be cur popped off char from pattern list
check if map[char] exists:
if it does, confirm it's value == string from popped from string list
    else the pattern is wrong return false
if map[char] doesn't exist, add it to map with value of popped of string from string list

Runtime: O(N) 
Space: O(N)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize map
pattern_to_string = {}

pattern_list = list(pattern)
strings_list = s.split()

for each char in pattern_list:
    if char is mapped to a string
        if it is check value != strings_list.pop():
        return false
    else:
    add char to map with value of popped off current string
    

return True
        

4. Write the Code And Pass Test Cases.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Initialize map
        pattern_to_string = {}
        key_set = set()
        strings_list = s.split()

        # Traverse from back so can match popped string from strings_list
        for char in pattern[::-1]:
            
            if strings_list:    
                cur_string = strings_list.pop()
            # If can't pop, then patters is longer than strings 
            else:
                return False
            
            # Check for char:string map and that string hasn't already been mapped
            if char in pattern_to_string:
                if pattern_to_string[char] != cur_string:
                    return False
            elif cur_string not in key_set:
                pattern_to_string[char] = cur_string
                key_set.add(cur_string)
            else:
                return False
                
        # Make sure no extra strings missing from patters
        if strings_list:
            return False
        return True