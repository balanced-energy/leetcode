'''
Workflow Timestamps
1. 0:00 - 3:45 Make Sure You Understand the Problem
2. 3:45 - 17:56 Design a Solution / Runtime and Space Complexity
3. 17:56 - 25:35 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

digits = [9,9] -> [1,0,0]

digits = [5,8,9] -> [5,9,0]
2. Design a Solution / Runtime and Space Complexity
- Add 1 to end element. 
- If value is 10, set element to 0, carry flag to true, and index len(digits) - 2 since handled last element already
- While carry and index >= 0: increment element at index check if value is 10 reduce index value 
- Check if carry, add 1 to front 
- return digits list

Runtime: O(N)
Space: O(1)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Carry flag and index
carry = False
# Manually handling last element
index = len(digits) - 2

# Check last element plus one
value = digits[-1] + 1

if value == 10:
    carry = true
    digits[-1] = 0
else:
    digits[-1] = value
    
While we have to carry and index > 0
    calculate new_value by incrementing element at index
    
    if new_value not 10
        set list at index to be new_val
        carry = false
    else:
        set list at index to be 0
    index -= 1

# Check if carry
if carry:
    add 1 to front of list

return digits

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Carry flag 
        carry = False
        # Manually handling last digit
        index = len(digits) - 2
        
        # Handle least significant digit
        lsd = digits[-1] + 1
        
        if lsd == 10:
            carry = True
            digits[-1] = 0
        else:
            digits[-1] = lsd
        
        
        # While we need to carry and within bounds
        while carry and index >= 0:
            new_value = digits[index] + 1
            
            if new_value == 10:
                digits[index] = 0
            else:
                digits[index] = new_value
                carry = False
            
            index -= 1
            
        # Check for carry
        if carry:
            digits.insert(0,1)
        
        return digits