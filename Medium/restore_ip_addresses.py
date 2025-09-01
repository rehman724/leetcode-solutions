from typing import List
class Solution:
    def restoreIpAddresses(self,s:str)->List[str]:
        res=[]

        def backtrack(start:int,path:List[str]):
            # If we have 4 parts and used all characters, it's valid
            if len(path)==4:
                if start==len(s):
                    res.append(".".join(path))
                return

            # Try segments of length 1 to 3
            for l in range(1,4):
                if start+l>len(s):
                    break
                segment=s[start:start+l]
                # Skip invalid cases: leading zero or >255
                if (segment.startswith("0") and len(segment)>1) or int(segment)>255:
                    continue
                backtrack(start+l,path+[segment])

        backtrack(0, [])
        return res


if __name__=="__main__":
    sol=Solution()

    # Example 1
    s1="25525511135"
    print("Input:", s1)
    print("Output:", sol.restoreIpAddresses(s1))
    # Expected: ["255.255.11.135", "255.255.111.35"]

    # Example 2
    s2="0000"
    print("\nInput:", s2)
    print("Output:", sol.restoreIpAddresses(s2))
    # Expected: ["0.0.0.0"]


