'''
Workflow Timestamps
1. 0:00 - 4:05 Make Sure You Understand the Problem
2. 4:05 - 17:03 Design a Solution / Runtime and Space Complexity
3. 17:15 - 21:25 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 21:35 - Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
Loop through prices, and check each price against our current minimum price. 
If it's smaller set it to be the new minimum, 
otherwise if it's greater check the difference against the max_profit until that point. 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
if length is 1 
    return 0
min_price = inf
max_profit = 0

for price in prices:
    if price is less than min price
        set it as new minimum
    else:
        max_profit = max(max_profit, price - min_price)

return max_profit
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)== 1: 
            return 0
        
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
        