
'''
1. Make Sure You Understand the Problem
num = [] -> 0

2. Design a Solution / Runtime and Space Complexity
Create a set containing all nums
Loop through each num and make sure current num isn't part of a longer sequence. 
If it's not then see how long that nums sequence is by increasing it's value and checking next incrementation
of that num is in the set. Once this process ends then log the length.


3. Write a Template for Code in Logical Blocks. Aka Pseudocode

max_streak
nums_set 

for num in nums_set:
    if num - 1 not in set:
        cur_num = num
        streak = 1
        
        while cur_num + 1 in nums_set:
            cur_num += 1
            streak += 1
        
        # Log length
        max_streak = max(max_streak, streak)
return max_streak


4. Write the Code And Pass Test Cases.
'''

'''
[1,2,3,4,5]
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0 
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_num = num
                streak = 1

                while cur_num + 1 in nums_set:
                    cur_num += 1
                    streak += 1

                # Log length
                max_streak = max(max_streak, streak)
        return max_streak

