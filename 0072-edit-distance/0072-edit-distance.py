'''
Mock - 45m
1. Make Sure You Understand the Problem
check if word1 or word2 length 0
ros
horse

Initialize
  h o r s e
r[F,F,T,F,F]
o[F,T,F,F,F]
s[F,F,F,T,F]
 [F,F,F,F,F]
 [F,F,F,F,F]

Traverse to make diagnol T's
  h o r s e
r[T,F,T,F,F] 0,0
o[F,T,F,F,F] 1,1
s[F,F,T,T,F] 2,2
 [F,F,F,F,F] 3,3
 [F,F,T,F,F] 4,4
 
 
   a b c
 b[F,T,F]
 a[T,F,F]
 t[F,F,F]
 
 
 base case is when chars are same and in same index
 
 case1: chars are equal but wrong index
 When is each operation optimal?
     insert -  when word1 < word2 
     delete - when word1 > word2 or next char is the same 
     replace - when equal and next char isn't the same
 
    if word1 > word2
        next column is T, delete
    elif word1 < word2
        insert
         
    
 case2: chars aren't equal
     insert - word1 < word2
     delete - word1 > word2
     replace - 
    if words are same length, want to replace vs delete
 

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