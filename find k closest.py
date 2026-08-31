import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        dist = [0] * n

        for i in range(n):
            dist[i] = abs(arr[i] - x)

        heap = []

        for i in range(n):
            if len(heap) < k:
                heapq.heappush(heap, (-dist[i], -arr[i]))

            elif (-dist[i], -arr[i]) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist[i], -arr[i]))

        ans = []

        while heap:
            d, val = heapq.heappop(heap)
            ans.append(-val)

        ans.sort()

        return ans