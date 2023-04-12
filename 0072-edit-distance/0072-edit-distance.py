'''
Mock - 45m
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
base cases: 
If word1 is empty, the edit distance is equal to the length of word2.
If word2 is empty, the edit distance is equal to the length of word1.

case 1:
    chars are same
    dp[word1Index - 1][word2Index - 1]

case 2: 
    add
    dp[word1Index][word2Index - 1] + 1
    
case 3: 
    delete
    dp[word1Index - 1][word2Index] + 1

case 4:
    replace
    dp[word1Index - 1][word2Index - 1] + 1
    

3. Write the Code And Pass Test Cases.
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Initialize first row and first columns
        for i in range(1, n+1):
            dp[0][i] = i
            
        for i in range(1, m+1):
            dp[i][0] = i
            
        for r in range(1, m+1):
            for c in range(1, n+1):
                # Chars are same
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r - 1][c - 1]
                    
                # minimize operation options
                else:                # add          # delete        # replace 
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1
                
        
        return dp[m][n]