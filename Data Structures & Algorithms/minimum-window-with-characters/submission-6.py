
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        t_map = Counter(t)
        s_map = Counter()

        required = len(t_map)
        have = 0

        shortest = float('inf')
        start = 0

        for r in range(len(s)):

            letter = s[r]
            s_map[letter] += 1

            # ¿Acabamos de completar la frecuencia
            # necesaria de este carácter?
            if letter in t_map and s_map[letter] == t_map[letter]:
                have += 1

            while have == required:

                curr = r - l + 1

                if curr < shortest:
                    shortest = curr
                    start = l

                left_letter = s[l]
                s_map[left_letter] -= 1

                # ¿Hemos dejado de cumplir algún requisito?
                if left_letter in t_map and s_map[left_letter] < t_map[left_letter]:
                    have -= 1

                l += 1

        if shortest == float('inf'):
            return ""

        return s[start:start + shortest]
