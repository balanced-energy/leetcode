'''
Workflow Timestamps
1. 0:00 - 2:55 Make Sure You Understand the Problem
2. 2:55 - 9:35 Design a Solution / Runtime and Space Complexity
3. 9:35 - 13:55 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 13:55 - 16:49 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
input = [], [] -> True

input = ['aabc'], ['caab'] -> True

input = ['%@#'], ['@#%'] -> True

2. Design a Solution / Runtime and Space Complexity
Loop through each string, incrementing character counts for first string, decrementing count for second. 
Position of count is determined by s[ord(c) - ord(a)]. 
If all values in count string are 0 return true, else false

Runtime: O(N)
Space: O(N)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Check if both or one are empty:
        if both empty 
            return true
        elif one is empty, other not:
            return false    
        elif len(s) != len(t):
            return false

    # Initialize count string
    counts = [len(s)]
    # Loop through string 1 incrementing count
    for c in s:
        increment s[ord(c) - ord(a)] 
    
    # Loop through string 2
    for c in t:
        decrement s[ord(c) - ord(a)] 

    # If any are not 0 return false
    if any(count):
        return False
    return True

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         # Check if both or one are empty:
        if not s and not t: 
            return True    
        elif len(s) != len(t):
            return False

        # Initialize count string
        # Change length if Unicode characters
        counts = [0] * 26
        # Loop through string 1 incrementing count
        for c in s:
            counts[ord(c) - ord('a')] += 1 
        
        # Loop through string 2
        for c in t:
            counts[ord(c) - ord('a')] -= 1

        # If any are not 0 return false
        if any(counts):
            return False

        return True
        
        
                