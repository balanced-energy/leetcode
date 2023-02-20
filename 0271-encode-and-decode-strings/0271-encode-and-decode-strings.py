'''
Workflow Timestamps
1. 0:00 - 5:20 Make Sure You Understand the Problem
2. 23:52 - 28:08 Design a Solution / Runtime and Space Complexity
3. 28:08 - 51:54 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 51:54 - 105:49 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
input = ['hello', '', 'world'] -> ['hello', '', 'world']

encode input = ['Hello', 'World']
encode ouput = str = 'HelloWorld'
decode input =  'HelloWorld'
deconde output = ['Hello', 'World']

2. Design a Solution / Runtime and Space Complexity
Encode
Initialize list to process characters. 
While looping through input string, append ord('char') and append '256' between each char. If char is ending character of string append after 257. 

Decode
Then when decoding, look at three chars at a time if equal to 256 
process previous ints turning back into char 
else if equal to >= 257 we know it's the end of a string.

# Because of constraints otherwise both would be O(N)
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
Runtime: O(1)
Space: O(1)

? ord('c') char(int)


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
Encode
# Loop through all characters of each string adding delimeter value of chr(257)
chr(257).join(str)

Decode
    check if empty string code 
    if s == chr(258)

4. Write the Code And Pass Test Cases.
'''

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        
        return chr(257).join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        
        return s.split(chr(257))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))