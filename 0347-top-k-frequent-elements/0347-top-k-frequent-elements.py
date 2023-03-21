'''
Workflow Timestamps
1. 0:00 - 1:50 Make Sure You Understand the Problem
2. 1:50 - 26:45 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[1,1,1,2,2,3], k = 2

{1:3, 2:2, 3:1}

items (1,3),(2,2),(3,1)

swap elements
(3,1), (2,2), (1,3)

minheap = (1,3)
      (3,1)   (2,2)
                
2. Design a Solution / Runtime and Space Complexity
- Create frequency count map.
- Take items list and swap tuple values to get first tuple to be count. 
- Heapify list, and remove end first element until len(heap) == k
- iterate heap appending second element of tuple to output list

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
counts = {}

for num in nums:
    counts[num] = counts.get(num, 0) + 1
    
get list of items
swap tuple values

heapify list
remove while length of list > k

add all elements in heap to output

4. Write the Code And Pass Test Cases.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        answer = []
        
        # Creates counts map
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        num_counts = counts.items()
        
        counts_num = []
        # Swap tuple values
        for item in num_counts:
            counts_num.append((item[1], item[0]))
            
        heapq.heapify(counts_num)
        
        while len(counts_num) > k:
            heapq.heappop(counts_num)
            
        # append all of second tuple values
        for item in counts_num:
            answer.append(item[1])
            
        return answer
        