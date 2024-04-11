'''
Workflow Timestamps
1. Make Sure You Understand the Problem
 
    - Check for edge cases
    - Choose 3 more tests
    
    
    - items = [[1,0],[1,0],[1,0],[1,0],[1,0]]
    - result = [1,0]
    
    
2. Design and Verify a Solution

 + Check all id's and scores
     DS: Map to stores ID's and associate each ID with a minheap (negate values) to save top 5 scores
     Loop through items
    - If ID in map, 
        - add score to ID's minheap 
        - check ID's minheap size, pop if greater than 5
    - else ID has not been seen, then 
        - add ID to map and 
        - create new minheap and add current score
    

    
 + calculate average of top scores for each id
    - looping through dictionary using .items()
     - for each ID's minheap total scores and divide by 5 adding to results
 + sort result by id's
 
 
Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]


map {1:[-65,-87,-91,-92,-100],2:[77,93,97]}

k = 5 (size of heap)
n = number of items in list
Runtime: O(n log(k))
Space: O(n)
3. Write the Code And Pass Test Cases.
'''

import heapq 

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        id_map = {}
        results = []
        
        for student, score in items:
            if student in id_map:
                heapq.heappush(id_map[student], score)
                
                if len(id_map[student]) > 5:
                    heapq.heappop(id_map[student])
            else:
                id_map[student] = [score]
                
        for student, scores in id_map.items():
            average = sum(scores) // len(scores)
            results.append([student, average])
        
        
        return sorted(results) 