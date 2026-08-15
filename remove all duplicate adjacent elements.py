class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in range (len(s)):
            if not st:
                st.append(s[i])
            elif st[-1]==s[i]:
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)


        