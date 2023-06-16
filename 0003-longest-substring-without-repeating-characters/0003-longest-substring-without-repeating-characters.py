'''
Make Sure You Understand the Problem
Design a Solution / Runtime and Space Complexity
Write a Template for Code in Logical Blocks. Aka Pseudocode
Write the Code And Pass Test Cases.

- Two pointer approach
- While end pointer is less than length s - 1
- Move end pointer forward 
- compare current length to max
- if char not in set
    - add to set
- if char is in set
 - move start pointer forward until duplicate char
     - remove letters if not equal to duplicate char
     - once at index of duplicate char move one more index

Two pointers l,r
while r < len(s) - 1
    start = s[l]
    end = s[r]
    if end not in map 
        end to map
        increment r
    
    else
        increment l until (s[l] == s[r])
        if s[l] not equalto s[r] 
        remove sfrom map
        then move l + 1 index 
        compare r - l to current max

{a,b,c}
   l  r 
abcabcbb

{w,k}
   lr
 pwwkew

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = -1
        seen = set()
        max_length = 0
        
        while r < len(s) - 1:
            r += 1
            start = s[l]
            end = s[r]
            
            # Add chars that aren't duplicates
            if end not in seen:
                seen.add(end)
                max_length = max(max_length, r-l + 1)
            else:
                # Move l pointer forward and remove chars
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                # Move l to one index past duplicate
                l += 1
                    
        return max_length
                    
        