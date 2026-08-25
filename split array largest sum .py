class Solution:
    def possible(self, nums: List[int], max_sum: int, max_partitions: int) -> bool:
        partitions_used = 1
        current_sum = 0

        for i in range(len(nums)):
            if current_sum + nums[i] <= max_sum:
                current_sum += nums[i]
            else:
                partitions_used += 1
                current_sum = nums[i]

                if partitions_used > max_partitions:
                    return False

        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < k:
            return -1

        low = max(nums)
        high = sum(nums)
        answer = -1

        while low <= high:
            mid = (low + high) // 2

            if self.possible(nums, mid, k):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer