import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = {}
        res = ""

        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Max heap using negative frequency
        heap = []

        for ch in freq:
            f = freq[ch]
            heapq.heappush(heap, (-f, ch))

        prev = None

        while heap:

            f, ch = heapq.heappop(heap)

            # If same character as previous, use another character
            if ch == prev:

                if not heap:
                    return ""

                f2, ch2 = heapq.heappop(heap)

                # Use ch2
                res += ch2
                f2 += 1

                # Put ch2 back if characters are remaining
                if f2 != 0:
                    heapq.heappush(heap, (f2, ch2))

                # Put the previous character back
                heapq.heappush(heap, (f, ch))

                prev = ch2

            else:

                # Use current character
                res += ch
                f += 1

                # Put it back if characters are remaining
                if f != 0:
                    heapq.heappush(heap, (f, ch))

                prev = ch

        return res