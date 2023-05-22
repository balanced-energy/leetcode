'''
haystack empty return -1

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx, char in enumerate(haystack):
            if char == needle[0]:
                window = len(needle)
                if idx + window <= len(haystack) and haystack[idx:idx + window] == needle:
                    return idx
        return -1