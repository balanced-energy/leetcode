'''
Mock-45m
Workflow Timestamps
1. 1:40 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[1,2,5] amount = 11

5+5+1

 j ->
i
  0 1 2 3 4 5 6 7 8 9 10 11
1[0,1,2,3,4,5,6,7,8,9,10,11] 
2[0,1,float,0,0,0,0,0,0,0, 0, 0]
5[0,0,0,0,0,0,0,0,0,0, 0, 0]

i coins
j amounts to n
compare [i-1][j] vs [i][j-coinvalue]+1



coins = [1,2,5]
coin = 1
x -> amount
  0 1 2 3 4 5 6 7 8 9 10 11
1[0,1,1,2,2,1,2,3,3,3,2,3] 

2. Design a Solution / Template / Runtime and Space Complexity
Initialize dp array of size amount

First idea
# Initialize first row
for i in range(amount):
    first_coin = coins[0]
    if i >= first_coin:
        dp[i] = dp[i][j - first_coin] + 1
        
# Fill in rest of coins 
    for i range(1, amount+1):
        for j in range(1, len(coins)):
          if j >= coins[j]
            dp[i] = min((dp[i-1][j]), (dp[i][j - coins[j]] + 1) )

return 

# Optimized approach with only using array of size amounts 
- Initialize dp array of size amounts + 1
- set dp[0] value to 0

for coin in coins:
    for i in range(coin, amount+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[amount] == float('inf'):
    return -1
    
return dp[amount]
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Intialize dp array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]