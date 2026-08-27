import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num in freq:
            f = freq[num]

            if len(heap) < k:
                heapq.heappush(heap, (f, num))

            elif f > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (f, num))

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
    
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num in freq:
            f = freq[num]
            heapq.heappush(heap, (-f, -num))

        ans = []

        for _ in range(k):
            f, num = heapq.heappop(heap)
            ans.append(-num)

        return ans
    
    