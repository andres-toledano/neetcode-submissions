class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for idx, temperature in enumerate(temperatures):
            if not stack:
                stack.append((temperature, idx))
                continue
            while stack and temperature > stack[-1][0]:
                _, j = stack.pop()
                days = idx - j
                result[j] = days
            stack.append((temperature, idx))
        return result



        