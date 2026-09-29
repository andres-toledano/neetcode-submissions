class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()

        for idx, num in enumerate(nums):
            solution = target - num
            if num in nums_map:
                return sorted([idx, nums_map[num]])
            else:
                nums_map[solution] = idx
        return []
            
        