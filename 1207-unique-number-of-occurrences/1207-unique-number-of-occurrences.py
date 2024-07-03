class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        counts = {}
        
        for num in arr:
            counts[num] = counts.get(num,0) + 1
            
        seen = set(counts.values())
        
        return len(seen) == len(counts)