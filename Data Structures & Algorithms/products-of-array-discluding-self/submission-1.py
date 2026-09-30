from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        i = 1
        j = len(nums) - 2
        right = deque([nums[-1]])
        for _ in range(len(nums) - 1):
            left.append(left[-1] * nums[i])
            right.appendleft(right[0] * nums[j])
            i += 1
            j -= 1
        result = [right[1]]
        for i in range(1, len(nums) - 1):
            result.append(left[i - 1] * right[i + 1])

        result.append(left[-2])
        return result

            

        