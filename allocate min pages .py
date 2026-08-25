class Solution:

    def possible(self, books, max_pages, students):
        allocated_students = 1
        current_pages = 0
    
        for i in range(len(books)):
    
            if current_pages + books[i] <= max_pages:
                current_pages += books[i]
    
            else:
                allocated_students += 1
                current_pages = books[i]
    
                if allocated_students > students:
                    return False
    
        return True
    
    def findPages(self, arr, k):
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