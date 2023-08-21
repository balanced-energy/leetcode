'''
Initialize variables prev and curr to 1 (1 way to decode empty string)
Loop through input s from index 1 to the end
    set new_value variable to 0
    Check if s[i] is valid or in other words, not 0 since it’s only 1 char.
        If it's valid then we assign our new_value to be curr. 
    Check if the two digits in position s[i - 1] and s[i] ( call them chars) are within the range 10 <= chars <= 26 meaning they’re a valid encoding.
        If chars is valid then we will add prev to our new_value variable. 
    Set prev equal to curr 
    Set curr equal to new_value. 
Returning curr

'''

class Solution:
    def numDecodings(self, s: str) -> int:
        # Encoding can't start with 0
        if s[0] == '0':
            return 0
        
        prev = 1
        curr = 1
        
        # Loop through input string
        for i in range(1, len(s)):
            new_value = 0
            
            # Check current integer for valid encoding
            if s[i] != '0':
                new_value = curr
                
            # Get two digits
            two_digits = int(s[i-1: i+1])
            
            # Check for valid two digit encoding 
            if 10 <= two_digits <= 26:
                new_value += prev
                
            # Reset and track total encodings to this point
            prev = curr
            curr = new_value 
            
        return curr