'''
Workflow Timestamps
1. 0:00 - 3:03Make Sure You Understand the Problem
2. 3:30 - 12:35 Design a Solution / Runtime and Space Complexity
3. 12:35 - 17:05 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 17:05 - 48:28 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

2. Design a Solution / Runtime and Space Complexity
Initialize a map starting with first string as key, with an itslef as first value in list strs[0]:strs[0]. 
Loop through remaining strings. Get map.keys() and compare current string to each keys
use Counter() object to check if counts are same and is an anagram, add to values list, else add as a new key
For each value in map.values() append to outpout list
Runtime:()
Space: O(N)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize anagrams map
anagrams = {first string:List[first string]}

for s in strs[1:]:
    check each string against anagrams.keys()
    Create two counter objects from s and cur_key
    if anagrams add s to anagrams key values list
    else add s as new key and add itself as first value in list

anagrams_groups = []
# Create output list 
for value in anagrams.values():
    anagrams_groups.append(value)
return anagrams_groups
4. Write the Code And Pass Test Cases.
'''
from collections import Counter

def str_counts(s):
    counts = [0] * 26

    for c in s:
        counts[ord(c) - ord('a')] += 1 


    # Convert to string to use as hashable key
    return str(counts)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize anagrams map with first string 
        anagrams = {str_counts(strs[0]):[strs[0]]}
       
        # Anagram found flag
        anagram_found = False
        for s in strs[1:]:
            s_counts = str_counts(s)
            # Convert to string to check against hashed keys
            
            # Check if any keys are an anagram of current s
            if s_counts in anagrams:
                anagrams[s_counts].append(s)
                anagram_found = True
                
            if not anagram_found:
                anagrams[s_counts] = [s]
            # Reset anagram flag for next string
            anagram_found = False
        
        anagrams_groups = []
        # Create output list 
        for value in anagrams.values():
            anagrams_groups.append(value)
        
        return anagrams_groups