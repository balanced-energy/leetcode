'''
Understand the Problem
    - If all positive values, we can return 1
    1.) [1,4,6] -> 1
    
    - Only 1 number and it's negative  
    2.) [-4] -> 5
    
    - All negative numbers 
    3.) [-1, -4, -2, -3] - min value sum of all elements -10 -> 11
    
    min val greater than 1 
    [2,2]
    return 1
    
Design a solution 
    minval 
    psum = []
    insert first element into psum list
    
    Find prefix sum
    loop through array, summing values from left to right cumulatively 
    from 1 to end of list - 1
    psum[i] = psum[i-1] + num[i]
    
    if minval >= 0 then return 1
    else return 1 - minval
    
    
    [1,4,6]
    1 to end of list - 1
    psum[i] = nums[i-1] + num[i]
    
    i = 2
    psum[2] = nums[1] + num[2]
    
    psum [1,5,11]
    
    input[-3,2,-3,4,2]
    4 to end of list - 1
    psum[i] = psum[i-1] + num[i]
    psum [-3, -1,-4,0,2]
    
    input[-1,-4,-2,-3]
    1 to end of list - 1
    psum[i] = psum[i-1] + num[i]
    psum [-1,-5,-7,-10]
    
    
    input [1,4,6]
    psum  [1,5,11]
    
~24:30 Implement and code 
'''
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        psum = [nums[0]]
        
        # find prefix sum 
        for i in range(1, len(nums)):
            psum.append(psum[i-1] + nums[i])
        
        minval = min(psum)
        
        if minval >= 0:
            return 1
        
        return 1 - minval
        
        
        
        
        
        
        
        
        
        
        
        