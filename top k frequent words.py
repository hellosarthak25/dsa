import heapq


class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):

        if self.freq != other.freq:
            return self.freq < other.freq

        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        heap = []

        for word in freq:
            f = freq[word]

            if len(heap) < k:
                heapq.heappush(heap, Pair(f, word))

            elif Pair(f, word) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, Pair(f, word))

        ans = []

        while heap:
            p = heapq.heappop(heap)
            ans.append(p.word)

        ans.reverse()

        return ans
