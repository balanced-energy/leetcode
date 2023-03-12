
'''
1. Make Sure You Understand the Problem
s = 'AABCABA' k = 1
s = 'AABA', k = 0
2. Design a Solution / Runtime and Space Complexity
We use a sliding window approach. By tracking the max frequency of any newly added character in the window we
are able to check if a current window is valid. A valid window will maintain end + 1 - start - max_count <= k.
When this condition is false, we increment the start pointer and log the string size. 


3. Write a Template for Code in Logical Blocks. Aka Pseudocode

char_frequencies map
max_count 
max_length 

while end < len(s):
    update current char count in map
    update max frequency
    
    check if current window is valid
    if not valid, 
    reduce count of s[start] in map 
    increment start to become valid window
    
    log window size 
    
    increment end 

return max_length

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_frequencies = {}
        
        # Start end at -1 so first chat is added to map
        start = 0
        end = -1
        
        max_count = 0
        max_length = 0
        
        for end in range(len(s)):
            # Increment current char count. If doesn't exist sets as 1
            char_frequencies[s[end]] = char_frequencies.get(s[end], 0) + 1
            
            # Update max_count
            max_count = max(max_count, char_frequencies[s[end]])
            
            # Check if window [end + 1 - start] - max_count is greater than k
            # Results in invalid window
            is_valid = end + 1 - start - max_count <= k
                
            if not is_valid:
                char_frequencies[s[start]] -= 1
                start += 1
                
            # log current valid window size
            max_length = end + 1 - start
            
        return max_length