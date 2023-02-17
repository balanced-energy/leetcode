'''
Workflow Timestamps
1. 0:00 - 4:00 Make Sure You Understand the Problem
2. 4:00 - 17:10 Design a Solution / Runtime and Space Complexity
3. 17:10 - 23:15 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 23:15 - 49:40 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

s = ['a'] -> True

s = ['daba'] -> True

s = ['daacbcaa'] -> True
2. Design a Solution / Runtime and Space Complexity
Two pointers, start and end.While start < end work towards the middle, checking each char s[start], s[end].
If we find characters that aren't equal. 
Remove the character at start index and check if the reversed string without this character is equal.
Do the same for the end index. 
If either reversed strings are equal return true else false.

Runtime: O(N)
Space: O(1)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize pointers
start = 0
end = len(s) - 1


while start < end:
    # If not equal. Check string without start against reversed value
    # Then check string without end, against reversed value
    # If either are equal return true else return False 
    if s[start] != s[end] and not deleted:
        check string without start and end against reversed values
        if equal continue
        else return false
        
    increment start and end

return True
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Initialize pointers
        start = 0
        end = len(s) - 1


        while start < end:
            # If not equal. Check string without start against reversed value
            # Then check string without end, against reversed value
            # If either are equal return true else return False 
            if s[start] != s[end]:
                # Need to cast and remove element from a copy of the string
                remove_start = list(s[:])
                remove_start.pop(start)
                remove_end = list(s[:])
                remove_end.pop(end)
                

                # Check if string with either removed are equal reversed
                #print(f'start: {s[start]}, end:{s[end]} -- remove_end:{remove_end}, reversed: {remove_end[::-1]}')
           
                if remove_start == remove_start[::-1]:
                    return True
                elif remove_end == remove_end[::-1]:
                    return True
                else: return False
                
            start += 1
            end -= 1

        return True
        