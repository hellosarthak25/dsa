class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range (len(arr)):
            if arr[i]<=k:
                k+=1
            else:
                break
        return k
class Solution:
    def findKthPositive(self, arr, k):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            missing = arr[mid] - mid - 1

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return high + k + 1