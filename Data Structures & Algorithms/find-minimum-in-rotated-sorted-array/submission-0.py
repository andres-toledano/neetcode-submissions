class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = (r + l) // 2

        while l < r:
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

            mid = (r + l) // 2

        return nums[mid]

        
            

