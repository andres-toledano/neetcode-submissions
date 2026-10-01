class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = "".join(c.lower() for c in s if c.isalnum())
        right = len(s) - 1
        print(s)
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True