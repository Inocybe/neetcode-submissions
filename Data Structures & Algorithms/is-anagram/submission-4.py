class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for char in s:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
        for char in t:
            if char not in seen:
                return False
            else:
                seen[char] -= 1
                if seen[char] < 0:
                    return False
            
        return True if len(s) == len(t) else False