class Solution:

    def possible(self, boards, max_time, painters):
        painters_used = 1
        current_time = 0
    
        for i in range(len(boards)):
            if current_time + boards[i] <= max_time:
                current_time += boards[i]
    
            else:
                painters_used += 1
                current_time = boards[i]
    
                if painters_used > painters:
                    return False
    
        return True
    
    def minTime(self, arr, k):
        n = len(arr)
    
        if n < k:
            return -1
    
        low = max(arr)
        high = sum(arr)
        answer = -1
    
        while low <= high:
            mid = (low + high) // 2
    
            if self.possible(arr, mid, k):
                answer = mid
                high = mid - 1
    
            else:
                low = mid + 1
    
        return answer