'''
Mock-45m
Workflow Timestamps
1. 0:00 - 2:00 Make Sure You Understand the Problem
2. 2:00 - 17:40 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
prereqs = [0,1],[1,2],[3,4]
outgoing = [[1],[2],[],[4],[]]
incoming edges = [0,1,0,0,0]
queue = [4,2]
cur_course = 1
neighbor = 1 reduce incoming count
taken = [0,3,1,4,2]
2. Design a Solution / Runtime and Space Complexity
- Create incoming edges list for every course. 
- Loop through list adding courses with no incoming edges to queue. 
- While queue for each course popped from queue
    for each neighbor of current course, reduce incoming edge count
    if edge count is then 0, add to queue
    add current course to taken list output
- If taken list length == numCourses return true
return false
3. Write a Template for Code in Logical Blocks. Aka Pseudocode

# Incoming and outgoing edges lists
incoming = [0] * numCourses
outgoing = [[] for _ in range(numcourses)]

for edge in prerequisistes:
    dependent = prerequisites[0]
    required = prerequisites[1]
    outgoing[required].append(dependent)
    incoming[dependent] += 1
    
# Add all courses with 0 incoming edges to queue
for i in incoming:
    if incoming[i] == 0:
        q.put(i)
        
while q:
    course = q.get()
    
    for nbr in outgoing[course]:
        incoming[nbr] -= 1
        if incoming[nbr] == 0:
            q.put(nbr)
    
    taken.append(course)
    
if len(taken) == numCourses:
    return True
    
return False
4. Write the Code And Pass Test Cases.

'''


import queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Incoming and outgoing edges lists
        incoming = [0] * numCourses
        outgoing = [[] for _ in range(numCourses)]
        q = queue.Queue()
        taken = []
        
        for edge in prerequisites:
            dependent = edge[0]
            required = edge[1]
            outgoing[required].append(dependent)
            incoming[dependent] += 1

        # Add all courses with 0 incoming edges to queue
        for i in range(len(incoming)):
            if incoming[i] == 0:
                q.put(i)

        while not q.empty():
            course = q.get()

            for nbr in outgoing[course]:
                incoming[nbr] -= 1
                if incoming[nbr] == 0:
                    q.put(nbr)

            taken.append(course)

        if len(taken) == numCourses:
            return True
        
        return False