class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        seen = set()
        max_substring = 0
        
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                seen.remove(s[l])
                l += 1
            max_substring = max(max_substring, len(seen))

        return max_substring
