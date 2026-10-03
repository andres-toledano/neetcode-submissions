class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most_water = 0
        while left < right:
            curr_height = min(heights[left], heights[right])
            curr_width = right - left
            most_water = max(most_water, curr_height * curr_width)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return most_water

        