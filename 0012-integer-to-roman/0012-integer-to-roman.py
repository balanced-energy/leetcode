'''
Workflow Timestamps
1. 0:00 - 5:25 Make Sure You Understand the Problem
2. 5:25 - 20:40 Design a Solution / Runtime and Space Complexity
3. 20:40 - 30:10 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 30:10 - 37:08 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

num = 44 -> 'XLIV' not 'IVIV'

num = 3999 -> 'MMMCMXCIX'
2. Design a Solution / Runtime and Space Complexity
- Create a mapping of value to symbols including special cases where subtraction is used. 
- Have a list of our values and find highest value we can use high_val. where input int <= next value in list
- Get the symbol for high_val and subtract that amount from int and repeat until int == 0


Runtime: O(1)
Space: O(1)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Initialize map and values list
    value_symbols = {}
    values_list = []
    roman_string = ''
    
    # While num > 0
    while num > 0:
        # Find highest usuable value
        i = 0
        while num >= values[i]:
            i += 1
        
        # i - 1 is index of highest value we can use
        high_val = values_list[i - 1]
        num -= high_val

        roman_high_val = values_symbol[high_val]
        roman_string = roman_string + roman_high_val
    
    return roman_string
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        # Initialize map and values list
        value_symbols = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman_string = ''

        # While num get highest possible symbol and add to string
        while num > 0:
            # Find highest usuable value
            i = 0
            while i < len(values) and num >= values[i]:
                i += 1

            # i - 1 is index of highest value we can use
            high_val = values[i - 1]
            num -= high_val

            roman_high_val = value_symbols[high_val]
            roman_string = roman_string + roman_high_val

        return roman_string
