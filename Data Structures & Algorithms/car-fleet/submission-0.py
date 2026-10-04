class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        sorted_cars = sorted(cars, key=lambda x: x[0], reverse=True)
        stack = []
        for pos, sp in sorted_cars:
            time = (target - pos) / sp
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)
        