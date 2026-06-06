class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones2 = [-s for s in stones]
        heapq.heapify(stones2)

        while len(stones2) > 1:
            x = -heapq.heappop(stones2)
            y = -heapq.heappop(stones2)

            if x != y:
                heapq.heappush(stones2,-(x-y))
        if len(stones2) > 0 :
            return -stones2[0]
        else:
            return 0    