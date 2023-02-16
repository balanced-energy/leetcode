'''
Workflow Timestamps
1. 0:00 - 3:20 Make Sure You Understand the Problem
2. 3:20 - 8:05 Design a Solution / Runtime and Space Complexity
3. 8:05 - 12:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 12:00 - 16:37 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
s = [] -> []

s = ['a'] -> ['a']
s = ['aabc'] -> ['cbaa']

s = ['$!#'] -> ['#!$']

2. Design a Solution / Runtime and Space Complexity
Check if empty or length 1, return array.
Two pointers at the start and end of string. 
Swapping characters working towards the middle. 
If even perform while start < end. 
Increment start, decrement end.
If odd perform until start == end.

Runtime: O(N)
Space: O(1)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    #Check for empty or length 1 string
    if not s or len(s) == 1:
        return s
    
    # Initialize pointers
    start 
    end 
    
    if s == even:
        while start < end:
            swap start and end
            increment start
            decrement end
    # s Odd
    else:
        while start != end:
            swap start and end
            increment start
            decrement end
    
    
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Check for empty of length 1 string
        if not s or len(s) == 1:
            return s
        
        # Initialize pointers
        start = 0
        end = len(s) - 1
        
        # While characters to swap increment start, decrement end
        # If even length
        if len(s) % 2 == 0:
            while start < end:
                s[start], s[end] = s[end],s[start]
                start += 1
                end -= 1
        
        # Odd length
        else:
            while start != end:
                s[start], s[end] = s[end],s[start]
                start += 1
                end -= 1
        return s
                
        