import heapq
class Solution:
    def kthSmallest(self, arr, k):
        n=len(arr)
        pq=[]
        for i in range(0,k):
            heapq.heappush(pq,-arr[i])
        for i in range(k,n):
            if arr[i]<(-pq[0]):
                heapq.heappop(pq)
                heapq.heappush(pq,-arr[i])
        return -pq[0]
                
        
        

