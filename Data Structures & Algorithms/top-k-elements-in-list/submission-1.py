import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        heap = []
        for num, count in nums_dict.items():
            heapq.heappush(heap, (-count, num))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result



        