class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        vals = collections.Counter(arr).values()
        return len(vals) == len(set(vals))
            
