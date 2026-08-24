class Solution:
    def search(self, a: List[int], target: int) -> bool:

        n = len(a)

        low = 0
        high = n - 1

        while low <= high:
            guess = (low + high) // 2

            if a[guess] == target:
                return True

            elif a[low] == a[guess] and a[guess] == a[high]:
                low = low + 1
                high = high - 1

            elif a[guess] > a[high]:
                if a[guess] < target:
                    low = guess + 1
                else:
                    if a[low] > target:
                        low = guess + 1
                    else:
                        high = guess - 1

            else:
                if a[guess] > target:
                    high = guess - 1
                else:
                    if a[high] < target:
                        high = guess - 1
                    else:
                        low = guess + 1

        return False