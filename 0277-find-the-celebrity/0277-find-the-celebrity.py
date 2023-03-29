'''
Mock-45m
Workflow Timestamps
1. 0:00 - 3:30 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
We first assume person 0 is a celebrity. Then by checking if this current potential celebrity
knows each of the other people we can identify both if they are no longer a potential celebrity
in which case we set the person they were checked against as the new potential celebrity 
or if they don't know the other person then we know that other person isn't a celebrity and continue on.

Then once we have our last potential celebrity, we check them against everyone else seeing if
either they know them, or the other person doens't know them. 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

# Find potential celebrity
potential_celeb = 0

for i in range(1, n):
    if potential_celeb knows i
        set i as potential celeb

if is_celebrity(potential_celeb):
    return potential_celeb

return -1 
# Check last potential celebrity against everyone else
def is_celebrity(n, people):
    for i in range(people):
        if i == n: continue
        if n knows i or i doesn't know n 
            return false
            
    return true
4. Write the Code And Pass Test Cases.
'''

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def is_celebrity(n, people):
    for i in range(people):
        if i == n: continue
            
        if knows(n,i) or not knows(i, n) :
            return False
            
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Find potential celebrity
        potential_celeb = 0

        for i in range(1, n):
            if knows(potential_celeb, i):
                potential_celeb = i
                
        # Current potential_celeb is only valid option
        if is_celebrity(potential_celeb, n):
            return potential_celeb
        
        return -1