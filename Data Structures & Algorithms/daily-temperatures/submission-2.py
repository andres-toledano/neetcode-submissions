class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for idx, temperature in enumerate(temperatures):

            while stack and temperature > stack[-1][0]:
                _, j = stack.pop()
                result[j] = idx - j

            stack.append((temperature, idx))

        return result


        