
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
'''
def collision(asteroid_1, asteroid_2):
    leftover = None
    if abs(asteroid_1) > abs(asteroid_2):
        leftover = asteroid_1
    elif abs(asteroid_1) < abs(asteroid_2):
        leftover = asteroid_2
    return leftover

class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Asteroids stack
        stack = []
        for asteroid in asteroids:
            # If stack is empty add asteroid to stack and continue to next asteroid
            if not stack:
                stack.append(asteroid)
                continue

            peek = stack[-1]
            # If asteroid is same sign as peek or traveling in opposite directions append
            if peek * asteroid > 0 or peek < 0 and asteroid > 0:
                stack.append(asteroid)
                continue

            while asteroid < 0 < peek and stack:
                leftover = collision(peek, asteroid)
                
                if leftover == peek:
                    break
                # If asteroid destroys peek, pop peek from stack and update peek
                elif leftover == asteroid:
                    stack.pop()
                    if stack:
                        peek = stack[-1]

                # Both destroyed
                else:
                    stack.pop()
                    break
                if not stack and leftover or leftover*peek > 0 or peek < 0 < leftover:
                    stack.append(asteroid)
                    break
        return stack   