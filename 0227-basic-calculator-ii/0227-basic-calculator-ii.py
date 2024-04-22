'''
3:40 Understand the problem

Order of operations
1. Multiple and divide
2. Add and subtract

'1' -> 1
'12' -> 12
'0-1234' -> -123

'1+3*3-2*2+1'
'1+9-2*2+1'
'1+9-4+1'
'5'

Design a solution
- Use four variables cur_res, result, num, op
    - cur_res will store our last expression result
    - result is the final result variable
    - num is used for cases where we have multi-digit integers if char isDigit() 
    - op stores last operator 
    
res, cur_res, num = 0,0,0
op = '+'

- for each ch in s + '+'

- if ch.isDigit()  
    num = num * 10 + int(ch)

# we have an operator in ch
- if ch  in ('*','/','+','-'):
    - if op is */+- 
        - cur_res *+= num
        - cur_res -= num
        - cur_res = int(cur_res / num)
    

    - if ch is + or -
        res += cur_res
        cur_res = 0

    op = ch
    num = 0
    
return res


'1' -> 1
'12+' -> 12

'0-1234+' -> -123
res = 0,0, -1234
cur_res = 0,0, -1234 
num = 0,0,1234
op = +, -, +


'1+3*3-2*2+1+'
'1+9-2*2+1'
'1+9-4+1'
'5'

res=1,10,8,5
cur_res=0,1,0,3,9,0,-2,0,-2,-4,-3
num=1,0,3,0,3,0,2,0,2,1
op=+,+,*,-,*,+

Runtime: O(N)
Space: O(1)

Implement 

"3+2*2+"
res=3,7
cur_res = 2,4
num = 0,2
op = +, *
'''
class Solution:
    def calculate(self, s: str) -> int:
        res, cur_res, num = 0,0,0
        op = '+'
        
        for ch in s + '+':
            
            if ch.isdigit():
                num = num * 10 + int(ch)
                
            if ch in ('*','/','+','-'):
                if op == '+':
                    cur_res += num
                
                elif op == '-':
                    cur_res -= num
                    
                elif op == '*':
                    cur_res *= num
                    
                elif op == '/':
                    cur_res = int(cur_res / num)
                    
                # If + or - move cur_res to result
                if ch in ('+', '-'):
                    res += cur_res
                    cur_res = 0
                   
                
                op = ch
                num = 0
            
        return res