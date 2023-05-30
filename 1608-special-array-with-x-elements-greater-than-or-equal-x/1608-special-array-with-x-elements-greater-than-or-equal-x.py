'''
- create counter object of each num
- find max num in nums and from that point reduce to 0 
    - checking if count is ever equal to the count of nums in counter object




'''
def get_greater(n, nums):
    count = 0
    for num in nums:
        if num >= n:
            count += 1
    return count

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        count = 0
        nums_count = Counter(nums)
        
        for n in range(max(nums), -1, -1):
            count += nums_count[n]
            if count == n:
                return n
            
        return -1