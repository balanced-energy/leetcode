'''
Workflow Timestamps
1. 0:00 - 2:45 Make Sure You Understand the Problem
2. 2:45 - 6:40 Design a Solution / Runtime and Space Complexity
3. 6:40 - 8:10 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 8:10 - 12:05 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
Initialize the Solution class with a member variable self.nums = input list and self.original_state input list. When we call Solution.shuffle() shuffle and return self.nums. When calling Solution.reset(), will set self.nums = self.original_state.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Initialize
    self.nums = nums
    self.original_state = nums

    # reset
    self.nums = self.original_state
    return self.nums

    # shuffle
    return math.rand(self.nums)
4. Write the Code And Pass Test Cases.
'''
import random
class Solution:

    def __init__(self, nums: List[int]):
         # Initialize self.nums to a copy of list
        self.nums = nums[::]
        self.original_state = nums


    def reset(self) -> List[int]:
        # Copy list and set to self.nums
        self.nums = self.original_state[::]
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()