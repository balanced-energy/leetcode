'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

'a' -> 'a'
 
 p
  s
   e
"babxdx" -> 'bab' or 'aba'
{a:1, b:1, d:1, x:1}
max_pal = 'b'


 
'abzzca' -> 'zz'

{a:2, b:1, c:1, z:2}


'aaazcaaa'

  s
    e
"cbbd" -> 'bb'

{c:0, b:1, d:0}

2. Design a Solution / Template / Runtime and Space Complexity
 - From each char in s
 - expand outward checking for palindrome
    - even checks require check from index i, i+1
    - odd checks require check from index i, i
 - create a palindrome and comparing length to max
 
3. Write the Code And Pass Test Cases.

'aba'
'abba'
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        
        ans=''
        for i in range(len(s)):
            ans = max(ans, expand(s,i,i), expand(s,i,i+1), key=len)
        return ans

       