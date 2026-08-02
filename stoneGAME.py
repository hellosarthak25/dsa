from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        total = sum(piles)

        @lru_cache(None)
        def solve(i, j):
            if i > j:
                return 0

            if i == j:
                return piles[i]

            if i + 1 == j:
                return max(piles[i], piles[j])

            take_i = piles[i] + min(
                solve(i + 2, j),
                solve(i + 1, j - 1)
            )

            take_j = piles[j] + min(
                solve(i + 1, j - 1),
                solve(i, j - 2)
            )

            return max(take_i, take_j)

        alice = solve(0, n - 1)
        return alice > total // 2