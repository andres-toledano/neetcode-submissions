class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        
        for idx in range(len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                suma = nums[idx] + nums[left] + nums[right]

                if suma == 0:
                    result.add((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif suma < 0:
                    left += 1

                else:
                    right -= 1
        
        return [list(x) for x in result]