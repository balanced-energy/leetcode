'''
Understanding the problem 
    (1 - minval, -minval + 1)
    1.) [-2,-1,-3] -> 1 - minval -> 7
    2.) [0] -> 1
    3.) [-1] -> 2
    4.) [1,2,3]
Design the solution 
    minval = 0
    
    loop through each num in nums to find minval 
    total += num
    minval = min(minval, total)
    
    return 1 - minval
    
    [-3,2,-3,4,2]
    total = -3,-1,-4,0,2
    minval = -3,-3,-4,-4,-4 
    
Runtime: O(n)
Space: O(1)
'''

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minval = 0
        total = 0
        
        for num in nums: 
            total += num 
            minval = min(minval, total)
            
        return 1 - minval
        