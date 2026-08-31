import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        distance = [0] * n

        for i in range(n):
            distance[i] = points[i][0] * points[i][0] + points[i][1] * points[i][1]

        heap = []

        for i in range(n):
            if len(heap) < k:
                heapq.heappush(heap, (-distance[i], i))

            elif distance[i] < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance[i], i))

        ans = []

        while heap:
            ans.append(points[heapq.heappop(heap)[1]])

        return ans