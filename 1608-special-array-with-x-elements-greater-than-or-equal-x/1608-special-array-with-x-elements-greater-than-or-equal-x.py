'''
- find min starting option for x comparing length nums and max(nums)
- from min_start int check if count of nums >= min_start 
    - if min_start == count return min_start 
    - else reduce min_start 




'''
def get_greater(n, nums):
    count = 0
    for num in nums:
        if num >= n:
            count += 1
    return count

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        n = len(nums)
        start_options = min(n, max(nums))

        start = start_options

        while start >= 0:
            count = get_greater(start, nums)
            #print(f'start:{start}, count:{count}')
            if count == start:
                return start
            start -= 1

        return -1