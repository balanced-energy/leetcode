'''
Starting from end identify first character and then sequence of characters until space is found

while last character is space, decrement pointer

# now on a character
increment count until space or beginning of s
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Check last character for space
        end = len(s) - 1
        last_word_count = 0
        
        # Increment pointer to first char
        while s[end] == ' ' and end >= 0:
            end -= 1
        
        # Cound length of string until space
        while s[end] != ' ' and end >= 0:
            last_word_count += 1
            end -= 1
            
        return last_word_count