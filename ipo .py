import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        capheap = []
        profheap = []

        # Min heap based on capital
        for i in range(len(capital)):
            heapq.heappush(capheap, (capital[i], profits[i]))

        for _ in range(k):

            # Move all affordable projects to profit max heap
            while capheap and capheap[0][0] <= w:
                cap, profit = heapq.heappop(capheap)
                heapq.heappush(profheap, -profit)

            # No project can be selected
            if not profheap:
                break

            # Select maximum profit
            w += -heapq.heappop(profheap)

        return w