'''
1. Make Sure You Understand the Problem

Test Cases:
MinStack() = []
push(1) = [1]
push(2) = [1, 2]
push(3) -> [1, 2, 3]
pop() = [1, 2]
top() - > [1, 2] top = 2 
getMin() -> 1
2. Design a Solution / Runtime and Space Complexity
Stack can be a list. 
Each push we will check added value against last min value
if new value is smaller than last min, then it's new min 
keeping a minimum invariant as second int in tuple then append() to list, 
pop() will pop() from list in O(1). 
Both operations in O(1). top returns last element list[-1].
Get min variable so will check last elements second tuple value for min 

Runtime: O(1)
Space Complexity: O(n)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
def __init__(self):
        min_stack = []

    def push(self, val: int) -> None:
        get min from last element
        if val < min:
            update min
        min_stack.append((val,min))

    def pop(self) -> None:
        removed_val = min_stack.pop()
        
    def top(self) -> int:
        min_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][1]
4. Write the Code And Pass Test Cases.
'''
# push(1)
# push(2)
# push(0)
# stack [(1,-1), (2,-1), (0,-2)]
class MinStack:

    def __init__(self):
        self.min_stack = []
       


    def push(self, val: int) -> None:
        # Check if stack has elements
        # Gets min from last element min position (val, min)
        old_min = None
        if self.min_stack:
            old_min = self.min_stack[-1][1]
        # First element
        else:
            self.min_stack.append((val, val))
            return 
        # Update min if needed 
        
        if val < old_min:
            self.min_stack.append((val, val))
        else:
            self.min_stack.append((val,old_min))
        
    def pop(self) -> None:
        removed_val = self.min_stack.pop()
     
        
    def top(self) -> int:
        return self.min_stack[-1][0]
         
        

    def getMin(self) -> int:
        return self.min_stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()