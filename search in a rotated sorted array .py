class Solution:

    def search(self, a: List[int], target: int) -> int:

        n = len(a)

        low = 0
        high = n - 1

        while low <= high:
            guess = (low + high) // 2

            if a[guess] == target:
                return guess

            elif a[guess] > a[n - 1]:
                if a[guess] < target:
                    low = guess + 1
                else:
                    if a[0] > target:
                        low = guess + 1
                    else:
                        high = guess - 1

            else:
                if a[guess] > target:
                    high = guess - 1
                else:
                    if a[n - 1] < target:
                        high = guess - 1
                    else:
                        low = guess + 1

        return -1
class Solution:

    def search(self, nums: List[int], target: int) -> int:

        n=len(nums)

        low=0
        high=n-1
        res=-1

        while(low<=high):

            mid=(low+high)//2

            if(nums[mid]>nums[n-1]):
                low=mid+1

            else:
                res=mid
                high=mid-1

        if(target>=nums[res] and target<=nums[n-1]):
            low=res
            high=n-1

        else:
            low=0
            high=res-1

        while(low<=high):

            mid=(low+high)//2

            if(nums[mid]==target):
                return mid

            elif(nums[mid]<target):
                low=mid+1

            else:
                high=mid-1

        return -1