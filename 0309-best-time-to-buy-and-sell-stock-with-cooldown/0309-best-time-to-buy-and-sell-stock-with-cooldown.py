'''
Mock - 45m
Workflow Timestamps
1. 1:30 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
If only 1 price, 0 profit
can sell on last day

 prices[1,3,7,0,1,8]
profit [2,4,-7,1,7,0]
 

prices [ 2,0, 3,0,5]
profit [-2,3,-3,5,0]

[2,0,3,0,5]
[0,0,0,b,s]
  
mp      [0,0,2,0,0,0,0]
prices  [1,2,4,0,5]
profits = 1 + 0
 


traversing i in prices

if not holding can buy and profit[i] is positive
        then find opportunity cost from buying that day means profit[i] vs profit[i+2]

if holding can sell or continue to hold
    if profit[i] > profit[i+2] then hold
    else sell

2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float('-inf'), float('-inf'), 0
        
        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)
            
        return max(sold, reset)
        