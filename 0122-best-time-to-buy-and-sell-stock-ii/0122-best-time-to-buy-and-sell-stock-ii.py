'''
Workflow Timestamps
1. 0:00 - 4:05 Make Sure You Understand the Problem
2. 4:05 - 13:20 Design a Solution / Runtime and Space Complexity
3. 13:20 - 25:25 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
prices = [7,2,1,3,1,6] - > 7
2. Design a Solution / Runtime and Space Complexity
- Loop through prices and check if we have a current position
- if there is a next price and its greater than or equal current. 
    - If not holding a position buy at current price
- else if holding a position, sell at current price
 
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Set profit
profit 0
# Current position
cur_holdings = None

# Loop through prices
for index, price in prices:
# Check if there's a next price to buy
    if index < len(prices) - 1 and price[index+1] >= price[index]:
        if cur_holdings is None:
            buy at current price
        
    elif cur_holdings:
        sell at current price and add to profit
        reset current holdings to none
     
return profit
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Set profit
        profit = 0
        # Current position
        cur_holdings = None

        # Loop through prices
        for index, price in enumerate(prices):
        # Check if there's a next price to buy
            if index < len(prices) - 1 and prices[index] <= prices[index+1] :
                if cur_holdings is None:
                    cur_holdings = price

            elif cur_holdings or cur_holdings == 0:
                # sell at current price and add to profit
                profit += price - cur_holdings
                cur_holdings = None

        return profit
        