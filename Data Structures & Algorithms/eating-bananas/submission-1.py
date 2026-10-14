class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mid = (l + r) // 2
        total_h = 0
        while l <= r:
            for pile in piles:
                total_h += math.ceil(pile/ mid)
            if total_h > h:
                l = mid + 1
            else:
                r = mid - 1
            total_h = 0
            mid = (l + r) // 2
        return l
        
        


        