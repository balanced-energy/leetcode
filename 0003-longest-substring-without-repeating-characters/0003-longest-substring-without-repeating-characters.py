'''
Workflow Timestamps
1. 0:00 - 2:45 Make Sure You Understand the Problem
2. 2:45 - 8:30 Design a Solution / Runtime and Space Complexity
3. 8:30 - 14:10Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
s = [] -> 0
s = ['a'] -> 1


2. Design a Solution / Runtime and Space Complexity
Start and end pointers
map to store char counts

Increment end until window is not valid, not valid meaning current char count > 1 in map
    not valid window 
        increment start pointer until cur_char count == 1 

save length of window 
increment end 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
start = 0
end = 0
max_length = 0
freq_map = {}

# Loop through each character
while end < len(s):
    increment char count in map
    
    while char count > 1:
        subtrack char count
        increment start until char count == 1
        
    compare current length to max and update
    increment end
    
return max_length
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Frequency map and max length
        freq_map = {}
        max_length = 0
        
        # Pointers for sliding window
        start = 0
        end = 0
        
        # Loop through all characters in s
        while end < len(s):
            # Increase current chars count
            char = s[end]
            
            # Set to 1 otherwise increase it's value
            freq_map[char] = freq_map.get(char, 0) + 1
            
            # While char count is above 1 increment start and reduce removed char's count in map
            while freq_map[char] > 1:
                freq_map[s[start]] -= 1
                start += 1
                
            # Valid window 
            max_length = max(max_length, end + 1 - start)
            
            end += 1
            
        return max_length