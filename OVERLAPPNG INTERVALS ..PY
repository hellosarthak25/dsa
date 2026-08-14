class Solution:
    def isIntersect(self, a):
        a.sort()
        n=len(a)
        start1=a[0][0]
        end1=a[0][1]
        for i in range(1,n):
            start2=a[i][0]
            end2=a[i][1]
            if end1>=start2:
                return True
            start1=start2
            end1=end2
        return False
       
       