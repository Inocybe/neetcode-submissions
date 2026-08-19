class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        r = len(cleaned) - 1
        l = 0
        while True:
            if r <= l:
                break
            elif cleaned[r] != cleaned[l]:
                return False
            l += 1
            r -= 1
        
        return True