class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st=[]
        n=len(temp)
        res=[0]*n
        for i in range(n-1,-1,-1):
            while st and temp[st[-1]]<=temp[i]:
                st.pop()
            if st:
                res[i]=st[-1]-i
            st.append(i)
        return res
        