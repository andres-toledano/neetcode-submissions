class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target and nums[l] <= nums[mid] and target < nums[l]:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target and nums[mid] <= nums[r] and target > nums[r]:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1 
        