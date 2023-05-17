'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

[[1,3],[-2,2],[1,2]] k = 2

[1,3]
sqrt((1-0)^2 + (3-0)^2) = sqrt(10)

[-2,2] = sqrt(8)

[1,2] = sqrt(5)

minheap of size k 
[(sqrt(5), [1,2]), (sqrt(8), [-2,2])]

2. Design a Solution / Template / Runtime and Space Complexity
- Compute distance of each point
    - add (distance, point) to points list
- sort list
- return list[:k] 

3. Write the Code And Pass Test Cases.
'''
import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            cur_distance = sqrt(point[0]**2 + point[1]**2)
            distances.append((cur_distance, point))
            
        distances.sort()
        
        answer = []
        
        for i in range(k):
            answer.append(distances[i][1])
            
        return answer 
        