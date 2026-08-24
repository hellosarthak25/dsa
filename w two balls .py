class Solution:
    def fun(self, arr, reqballs, currentguess):
        placedballs = 1
        recentballposition = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - recentballposition >= currentguess:
                placedballs += 1
                recentballposition = arr[i]

                if placedballs == reqballs:
                    return True

        return False


    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)

        position.sort()

        low = 1
        high = position[n-1] - position[0]
        res = -1

        while low <= high:
            guess = (low + high) // 2

            if self.fun(position, m, guess):
                res = guess
                low = guess + 1
            else:
                high = guess - 1

        return res