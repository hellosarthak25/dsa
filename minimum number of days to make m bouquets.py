class Solution:
    def fun(self, days: List[int], minbouqets: int, reqadjflowers: int, currentguess: int) -> bool:
        n = len(days)
        adjflowers = 0
        bouquets = 0

        for i in range(n):
            if days[i] <= currentguess:
                adjflowers += 1

                if adjflowers == reqadjflowers:
                    bouquets += 1
                    adjflowers = 0

            else:
                adjflowers = 0

        if bouquets >= minbouqets:
            return True

        return False

    def minDays(self, a: List[int], m: int, k: int) -> int:
        n = len(a)

        if m * k > n:
            return -1

        low = 0
        high = max(a)
        ans = -1

        while low <= high:
            guess = (low + high) // 2

            if self.fun(a, m, k, guess):
                ans = guess
                high = guess - 1
            else:
                low = guess + 1

        return ans