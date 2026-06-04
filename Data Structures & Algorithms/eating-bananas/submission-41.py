class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = 1
        totaltime = 0
        while left <= right:
            mid = (left+right)//2
            for i in range(len(piles)):
                totaltime += math.ceil(piles[i]/mid)
            if totaltime <= h:
                right = mid -1 
                totaltime = 0
                k = mid
            else:
                left = mid + 1
                totaltime = 0
        return k