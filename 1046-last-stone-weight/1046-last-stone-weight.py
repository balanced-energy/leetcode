'''
Workflow Timestamps
1. 0:00 - 4:15 Make Sure You Understand the Problem
2. 4:15 - 8:20 Design a Solution / Runtime and Space Complexity
3. 8:20 - 11:20 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 11:20 - 18:40 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

2. Design a Solution / Runtime and Space Complexity
- If one stone return that stone
- While there are at least two stones, get max two stones
- Compare values, if they're equal pop both 
- otherwise pop smaller and larger becomes differnece of  stone values
- return last stone
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
If one stone 
    return that stone
    
while there are at least two stones
    get max stone1 and pop from list
    get max stone2 and pop from list
    
    # Compare stones
    if they're equal both are removed
    otherwise get absolute value and append to list
    
return stones 
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Check if only one stone
        if len(stones) == 1:
            return stones[0]
        
        # While at least two stones compare the max stones
        while len(stones) > 1:
            # Remove max two stones 
            max_stone_1 = stones.pop(stones.index(max(stones)))
            max_stone_2 = stones.pop(stones.index(max(stones)))
            
            # Compare stones
            # If equal both removed else append difference
            if max_stone_1 != max_stone_2:
                difference = max_stone_1 - max_stone_2
                stones.append(abs(difference))
        
        if stones:
            return stones[0]
        return 0