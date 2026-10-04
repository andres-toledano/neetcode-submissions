class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            last_idx = idx

            while stack and height < stack[-1][1]:
                last_idx, last_height = stack.pop()

                area = last_height * (idx - last_idx)
                max_area = max(max_area, area)

            stack.append((last_idx, height))

        while stack:
            start, height = stack.pop()

            area = height * (len(heights) - start)
            max_area = max(max_area, area)

        return max_area


        