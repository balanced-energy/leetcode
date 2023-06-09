import math

class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        idx = 0
        while idx < len(s):
            if s[idx] == 'X':
                count += 1
                idx += 3
                continue
            idx += 1
        return count