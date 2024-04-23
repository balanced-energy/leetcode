'''
6:20 Understand the problem

[-1,-2,-3] -> [-1,-2,-3]
[1,2,3] -> [1,2,3]
[-1, 1] -> [-1, 1]

[-1,-1]

[3,2,1,-3] -> []

[3,2,1,-2] -> [3]

[-1,2,-1]


38:45 Design a solution
Traverse list
Use a stack to store asteriods

stack = []

for ast in asteroids:
    if ast is positive 
        add to stack
    
    else:
        while stack and stack[-1] < abs(ast)
            stack.pop()
    
        if stack and stack[-1] == abs(ast) and stack[-1] > 0 and ast < 0:
            stack.pop()
        
        elif not stack or stack[-1] < 0 :
          stack.append(ast)  

return stack
[-1, 1] -> [-1, 1]

[-1,]
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids: 
            if ast > 0:
                stack.append(ast)

            else:
                while stack and stack[-1] < abs(ast) and stack[-1] > 0:
                    stack.pop()

                if stack and stack[-1] == abs(ast) and (stack[-1] > 0 and ast < 0):
                    stack.pop()

                elif not stack or stack[-1] < 0:
                    stack.append(ast)  

        return stack