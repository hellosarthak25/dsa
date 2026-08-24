class Solution:
    def fun(self, stalls: [int], reqcows, currguess) -> [bool]:
        cows = 1
        pos = stalls[0]

        for i in range(1, len(stalls)):
            dist = stalls[i] - pos

            if dist < currguess:
                continue
            else:
                cows += 1
                pos = stalls[i]

            if cows >= reqcows:
                return True

        return False

    def aggressiveCows(self, arr, k):
        n = len(arr)

        arr.sort()

        low = 1
        high = arr[n-1] - arr[0]
        res = -1

        while low <= high:
            guess = (low + high) // 2

            if self.fun(arr, k, guess):
                res = guess
                low = guess + 1
            else:
                high = guess - 1

        return res

