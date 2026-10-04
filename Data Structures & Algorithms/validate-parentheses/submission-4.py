class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {')' : '(', '}': '{', ']' : '['}
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char not in parentheses_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                opened = stack.pop()
                if opened != parentheses_map[char]:
                    return False
        return not stack
                
                
        
        