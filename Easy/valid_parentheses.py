# 20. Valid Parentheses


class Solution(object):
    def isValid(self,s):
        stack=[]
        mapping={')':'(','}':'{',']':'['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if stack==[] or mapping[char]!=stack.pop():
                    return False
            else:
                # Invalid character in input
                return False

        return stack==[]


if __name__=="__main__":
    sol=Solution()
    # Example test cases
    print(sol.isValid("()"))       # True
    print(sol.isValid("()[]{}"))   # True
    print(sol.isValid("(]"))       # False
    print(sol.isValid("([)]"))     # False
    print(sol.isValid("{[]}"))     # True
