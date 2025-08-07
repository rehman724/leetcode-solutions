# Medium/string_to_integer.py

def myAtoi(s:str)->int:
    s=s.lstrip()
    if not s:
        return 0

    i=0
    sign=1
    result=0
    INT_MAX,INT_MIN=2**31-1,-2**31

    # Handle sign
    if s[i]=='+' or s[i]=='-':
        sign=-1 if s[i]=='-' else 1
        i+=1

    # Convert digits
    while i<len(s) and s[i].isdigit():
        result=result*10+int(s[i])
        i+=1

    result*=sign

    # Clamp to 32-bit signed int range
    if result<INT_MIN:
        return INT_MIN
    if result>INT_MAX:
        return INT_MAX

    return result

if __name__=="__main__":
    print(myAtoi("42"))               # 42
    print(myAtoi("   -42"))           # -42
    print(myAtoi("4193 with words"))  # 4193
    print(myAtoi("words and 987"))    # 0
    print(myAtoi("-91283472332"))     # -2147483648
