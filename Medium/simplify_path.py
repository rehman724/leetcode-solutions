class Solution:
    def simplifyPath(self,path:str)->str:
        stack=[]
        parts=path.split("/")

        for part in parts:
            if part=="" or part== ".":
                continue
            elif part=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


if __name__=="__main__":
    sol=Solution()

    # Example cases
    print(sol.simplifyPath("/home/"))            # Output: "/home"
    print(sol.simplifyPath("/../"))              # Output: "/"
    print(sol.simplifyPath("/home//foo/"))       # Output: "/home/foo"

    # Additional cases
    print(sol.simplifyPath("/a/./b/../../c/"))   # Output: "/c"
    print(sol.simplifyPath("/a/../../b/../c//.//")) # Output: "/c"
    print(sol.simplifyPath("/a//b////c/d//././/..")) # Output: "/a/b/c"
