class Solution:
    def capable(self, weights: List[int], reqdays: int, capacity: int) -> bool:
        curr = 0
        nowdays = 1

        for i in range(len(weights)):
            if curr + weights[i] <= capacity:
                curr += weights[i]
            else:
                nowdays += 1
                curr = weights[i]

                if nowdays > reqdays:
                    return False

        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = -1

        while low <= high:
            guess = (low + high) // 2

            if self.capable(weights, days, guess):
                res = guess
                high = guess - 1
            else:
                low = guess + 1

        return res