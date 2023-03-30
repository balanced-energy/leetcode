'''
Mock-45m
Workflow Timestamps
1. 0:00 - 1:15 Make Sure You Understand the Problem
2. 1:15 - 7:15 Design a Solution / Runtime and Space Complexity
3. 7:15 - 15:30 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
Use top sort.
Preprocessing.
prerequisites [[1,0], [2,1],[3,2], [3,1]]
- Create outgoing edges list [[1],[2,3],[3],[]]
- Create an incoming edges int list [0,1,1,2]
- Add all courses with 0 prerequisites (0 incoming edges) to queue.
- For each course in queue, get their outgoing edges and reduce the incoming
    edges for each neighbor in their outgoing edges list.

    - Check if reduction of incoming edges for neighbor results in neighbor having
        0 incoming edges, if so add to queue. 

    - Add current course to taken courses list
    
- If taken courses list is equal to numCourses, return list

return []
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Create outgoing edges neighbors list and incoming edges int list
outgoing = [[]]
incomging = []

for edge in prerequisites:
    add neighbor ai to position bi outgoing neighbors 
    incremenet ai incoming edges 
    
add all courses with 0 incoming edges to queue

while queue
    get course
    
    for each neighbor
        reduce incoming edges
        if incoming edges is now 0
            add to queue
            
    add course to taken list

if taken list length is == numCourses
    return taken list
    
return []
4. Write the Code And Pass Test Cases.
'''
import queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize lists
        outgoing = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses
        taken = []
        q = queue.Queue()
        
        # Preprocessing to create outgoing, incoming edges list
        for edge in prerequisites:
            outgoing[edge[1]].append(edge[0])
            incoming[edge[0]] += 1
            
            
        for course in range(len(incoming)):
            if incoming[course] == 0:
                q.put(course)
        
        while not q.empty():
            course = q.get()
            
            for nbr in outgoing[course]:
                incoming[nbr] -= 1
                if incoming[nbr] == 0:
                    q.put(nbr)
                    
            taken.append(course)
        
        if len(taken) == numCourses:
            return taken
        
        return []