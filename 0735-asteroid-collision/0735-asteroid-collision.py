'''
Workflow Timestamps
1. 0:00 - 5:45 Make Sure You Understand the Problem
2. 5:45 - 29:00 Design a Solution / Runtime and Space Complexity
3. 29:00 - 32:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 32:00 - 55:40 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
Test Cases:

input = [-5, 2, -1]
= [-5,2]
= [-5]

input = [8, 6, 7, 4] -> [8, 6, 7, 4]

input = [-7, 6, 7,-5, 8, 9] -> 
=  [-8, 6, 7, -5, 8, 9]
=  [-8, 6, 7, 8, 9]
=  [-8, 7, 8, 9]
=  [9]

input = [-8, 6, 7] -> [-8]

2. Design a Solution / Runtime and Space Complexity
- Starting from end of asteroid list, push asteroid onto stack remove it from list. 
- Continue from right to left traversing list. If asteroid in list is different sign from top of stack asteroid, handle collision.
- Collision is handled by evaluating absolute value, smaller value is removed, equal both are removed. 
- Push asteroid onto stack that exists still 
- If list empty return

Runtime: O(N)
Space: O(N)


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Initialize stack with first asteroid
    stack = [asteroids.pop()]

    while asteroids:
        pop next asteroid from list
        compare it to top of stack asteroid
        if signs different 
            handle collisions
            if asteroid remains push to stack
        else:
            push to stack 


4. Write the Code And Pass Test Cases.
'''

def collision(asteroid_1, asteroid_2):
    if abs(asteroid_1) > abs(asteroid_2):
        return asteroid_1
    elif abs(asteroid_1) < abs(asteroid_2):
        return asteroid_2
   
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Initialize stack with first asteroid
        stack = [asteroids.pop()]

        while asteroids:
            cur_asteroid = asteroids.pop()
            if stack:
                prev_asteroid = stack[-1]
            else:
                stack.append(cur_asteroid)
                continue
            if cur_asteroid < 0 and prev_asteroid  < 0:
                stack.append(cur_asteroid)
            elif cur_asteroid > 0 and prev_asteroid > 0:
                stack.append(cur_asteroid)
            elif cur_asteroid < 0 and prev_asteroid > 0:
                stack.append(cur_asteroid)
            # Asteroids different signs, handle collision.
            else:
                old_asteroid = stack.pop()
                asteroid = collision(cur_asteroid, old_asteroid)
                if asteroid:
                    asteroids.append(asteroid)
        
        return stack[::-1] 
        