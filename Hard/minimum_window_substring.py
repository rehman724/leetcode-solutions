from collections import Counter
class Solution:
    def minWindow(self,s:str,t:str)->str:
        if not s or not t:
            return ""

        t_count=Counter(t)
        window={}

        have,need=0,len(t_count)
        res,res_len=[-1,-1], float("inf")
        l=0

        for r,ch in enumerate(s):
            window[ch]=window.get(ch,0)+1

            if ch in t_count and window[ch]==t_count[ch]:
                have+=1

            while have==need:
                # Update result
                if (r-l+1)<res_len:
                    res=[l,r]
                    res_len=r-l+1

                # Shrink from left
                window[s[l]]-=1
                if s[l] in t_count and window[s[l]]<t_count[s[l]]:
                    have-=1
                l+=1

        l,r=res
        return s[l:r+1] if res_len != float("inf") else ""
