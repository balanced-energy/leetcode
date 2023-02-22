'''
Workflow Timestamps
1. 0:00 - 2:20 Make Sure You Understand the Problem
2. 2:30 - 8:35 Design a Solution / Runtime and Space Complexity
3. 8:35 - 14:50 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

acdab -> 1 
2. Design a Solution / Runtime and Space Complexity
- Traverse words in wordsDict. For each word check if it's either word1 or word2.
- If it's word1, set searching_for to be word2, else vise versa
- when we find opposite word, calculate distance, check against previous min and update
- set searching_for as opposite word, continue

Runtime: O(N)
Space: O(1)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Opposite word, and min_distance 
searching_for = None
min_distance = inf

# Traverse through words
for word in words:
    # Find first word
    if not searching_for and word is word1
        searching_for = word2
    elif not searching_for word is word2
        searching for is word1
        
    # Find second word
    found second word:
        cur_distance = calculate distance
        min_distance = min(cur_dist, min_distanct)
        searching set to other word
        
    
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # Opposite word and min distance
        searching_for = None
        prev_word_index = None
        min_distance = float('inf')
        
        # Check all words
        for index, word in enumerate(wordsDict):
            # Find first word
            if not searching_for and word == word1:
                searching_for = word2
                prev_word_index = index
            elif not searching_for and word == word2:
                searching_for = word1
                prev_word_index = index
                
            # Find second word and calculate distance
            if searching_for == word1:
                if word == word1:
                    cur_distance = index - prev_word_index
                    min_distance = min(cur_distance, min_distance)
                    searching_for = word2
                    prev_word_index = index
                # Update most recent index 
                elif word == word2:
                    prev_word_index = index
                
            elif searching_for == word2:
                if word == word2:
                    cur_distance = index - prev_word_index
                    min_distance = min(cur_distance, min_distance)
                    searching_for = word1
                    prev_word_index = index
                # Update most recent index 
                elif word == word1:
                    prev_word_index = index
                
        return min_distance 