class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last_element = len(matrix[0]) - 1
        for lista in matrix:
            if target <= lista[last_element]:
                return self.binary_search(lista, target)
        return False

    def binary_search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l <= r:
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return True
            mid = (l + r) // 2
        return False