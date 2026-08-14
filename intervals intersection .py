class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res=[]
        n=len(a)
        m=len(b)
        while(i<n and j<m):
            start1=a[i][0]
            end1=a[i][1]
            start2=b[j][0]
            end2=b[j][1]
            if (start1<=start2):
                if (end1>=start2):
                    s=max(start1,start2)
                    e=min(end1,end2)
                    res.append([s,e])
            else:
                if (end2>=start1):
                    s=max(start1,start2)
                    e=min(end1,end2)
                    res.append([s,e])
            if end1<=end2:
                i+=1
            else:
                j+=1
        return res



        