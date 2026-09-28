class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            curr = 0
            if num - 1 not in nums_set:
                aux = num
                while aux in nums_set:
                    curr += 1
                    longest = max(longest, curr)
                    aux += 1
        return longest
                

nums = [0,3,2,5,4,6,1,1]
solution = Solution()
print(solution.longestConsecutive(nums))

