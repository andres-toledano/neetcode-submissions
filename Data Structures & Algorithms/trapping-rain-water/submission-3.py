from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        left_heights = [0] * n
        right_heights = [0] * n

        for i in range(n):
            j = -i - 1
            
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            left_heights[i] = l_wall
            right_heights[j] = r_wall
        sumn = 0
        for i in range(n):
            pot = min(left_heights[i],right_heights[i])
            sumn += max(0, pot - height[i])
        return sumn
        

lista = [0,2,0,3,1,0,1,3,2,1]
solution = Solution()
solution.trap(height=lista)