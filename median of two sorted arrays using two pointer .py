class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2

        i = 0
        j = 0
        count = 0

        mid1 = -1
        mid2 = -1

        while i < n1 and j < n2:

            if nums1[i] <= nums2[j]:
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1

            count += 1

            if count == total // 2:
                mid1 = current

            if count == total // 2 + 1:
                mid2 = current
                break

        # If one array is exhausted
        while i < n1:
            current = nums1[i]
            i += 1
            count += 1

            if count == total // 2:
                mid1 = current

            if count == total // 2 + 1:
                mid2 = current
                break

        while j < n2:
            current = nums2[j]
            j += 1
            count += 1

            if count == total // 2:
                mid1 = current

            if count == total // 2 + 1:
                mid2 = current
                break

        if total % 2 == 0:
            return (mid1 + mid2) / 2

        return mid2