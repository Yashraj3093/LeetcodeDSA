class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        result = inf

        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                result = min(result, d, n - d)
        
        return result if result != inf else -1