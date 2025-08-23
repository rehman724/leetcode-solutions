
class Solution:
    def isNumber(self,s:str)->bool:
        s=s.strip()
        if not s:
            return False

        num_seen=False
        dot_seen=False
        e_seen=False

        for i,char in enumerate(s):
            if char.isdigit():
                num_seen=True
            elif char in ['+','-']:
                # Sign allowed only at start or after 'e'
                if i>0 and s[i-1] not in ['e','E']:
                    return False
            elif char=='.':
                # Dot not allowed after 'e' or if already seen
                if dot_seen or e_seen:
                    return False
                dot_seen=True
            elif char in ['e','E']:
                # 'e' must follow a number and only occur once
                if e_seen or not num_seen:
                    return False
                e_seen=True
                num_seen=False  # need number after e
            else:
                return False

        return num_seen


# --------------------------
# Test Cases
# --------------------------
if __name__=="__main__":
    sol=Solution()

    # Valid numbers
    assert sol.isNumber("2")==True
    assert sol.isNumber("0089")==True
    assert sol.isNumber("-0.1")==True
    assert sol.isNumber("+3.14")==True
    assert sol.isNumber("4.")==True
    assert sol.isNumber("-.9")==True
    assert sol.isNumber("2e10")==True
    assert sol.isNumber("-90E3")==True
    assert sol.isNumber("3e+7")==True
    assert sol.isNumber("+6e-1")==True
    assert sol.isNumber("53.5e93")==True
    assert sol.isNumber("-123.456e789")==True

    # Invalid numbers
    assert sol.isNumber("abc")==False
    assert sol.isNumber("1a")==False
    assert sol.isNumber("1e")==False
    assert sol.isNumber("e3")==False
    assert sol.isNumber("99e2.5")==False
    assert sol.isNumber("--6")==False
    assert sol.isNumber("-+3")==False
    assert sol.isNumber("95a54e53")==False
    assert sol.isNumber(".")==False
    assert sol.isNumber("e")==False
    assert sol.isNumber("  ")==False

    print("All test cases passed!")
