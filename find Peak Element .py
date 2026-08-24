class Solution:
    def findPeakElement(self, a: List[int]) -> int:

        n = len(a)

        if n == 1:
            return 0

        if a[0] > a[1]:
            return 0

        if a[n-1] > a[n-2]:
            return n-1

        low = 1
        high = n-2

        while low <= high:

            mid = (low + high) // 2

            if a[mid] > a[mid+1] and a[mid] > a[mid-1]:
                return mid

            elif a[mid] > a[mid-1]:
                low = mid + 1

            elif a[mid] > a[mid+1]:
                high = mid - 1

            else:
                low = mid + 1

        return -1