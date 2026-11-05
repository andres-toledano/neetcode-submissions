class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for num in nums[1:]:
            new_max = max(num, max_product * num, num * min_product)
            new_min = min(num, num * max_product, num * min_product)

            max_product = new_max
            min_product = new_min

            result = max(result, max_product)
        return result



        