class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.k = k
        self.heap = []
        returnlist = []
        for point in points:
            t = (point[0]**2 + point[1]**2, (point[0],point[1]))
            heapq.heappush(self.heap,t)
        for i in range(k):
            t = self.heap[0]
            returnlist.append(t[1])
            heapq.heappop(self.heap)
        return returnlist