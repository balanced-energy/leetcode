'''
Workflow Timestamps
1. 0:00 - 2:35 Make Sure You Understand the Problem
2. 2:35 - 8:20 Design a Solution / Runtime and Space Complexity
3. 8:20 - 14:35 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 14:35 - 34:40 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
s = '' -> 0
s = 'IV' -> 4

special cases: 'IV', 'IX', 'XL', 'XC', 'CD', 'CM'
2. Design a Solution / Runtime and Space Complexity
If no s, return 0
Initialize an output int, map of symbols to values and a map of special case symbols to value 'string': int.
While string check last two if in special cases map, if in map then add mapped value
otherwise pop off last char and add value 
return output int

Runtime: O(1)
Space: O(1)


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # If no s return 0
    if not s:
        return 0
    # Initialize map of symbols:values, special cases: values and output int
    symbols_values = {}
    special_symbols = {}
    output_num = 0
    
    # While string check last two if in special cases map, if in map then add mapped value
    while s:
        if len(s) >= 2:
            cur_symbol = s[-2:]
        
        if cur_symbol in special_symbols:
            add value to output num from special symbols map
            s.pop()
            s.pop()
        else 
            cur_symbol = s.pop()
            get symbol from regular map 
            addd value
            
    return output_num
        
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
         # If no s return 0
        if not s:
            return 0
        
        # Initialize map of symbols:values, special cases: values and output int
        symbols_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        special_symbols = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        num = 0

        # While string check last two if in special cases map, else get symbol from symbols_values and add mapped value
        while s:
            # Check for special symbol
            if len(s) >= 2:
                cur_symbol = s[-2:]
            else:
                cur_symbol = s[-1]
                
            if cur_symbol in special_symbols:
                s = s[:-2]
                num += special_symbols[cur_symbol]
                
            else:
                cur_symbol = s[-1]
                s = s[:-1]
                num += symbols_values[cur_symbol]
                 

        return num
        