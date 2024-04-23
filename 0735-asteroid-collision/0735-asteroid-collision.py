'''
6:00 Understand our problem

[-1,-1] -> [-1,-1]
[1,1] -> [1,1]
[-1, 1] -> [-1, 1]

[-1,2,-1] -> [-1, 2]
[-1, 2] -> [-1, 2]


[1,-1]
[]

Design a solution
Traverse asteroids utilizing stack to store asteroids that may later collide

stack = []

for ast in asteroids:
    if ast > 0:
        append to stack
    else:    
        # Handle collisions when ast > ast's on stack
        while stack and stack[-1] > 0 and stack[-1] < abs(ast):
            stack.pop()
        
        # 
         if not stack or stack[-1] < 0:
            stack.append(ast)

        elif stack[-1] == abs(ast):
            stack.pop()

return stack

Runtime: O(N)
Space: O(N)

15:50 Implement
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
                
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                    stack.pop()
                    
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                
                elif stack[-1] == abs(ast):
                    stack.pop()
                    
        return stack