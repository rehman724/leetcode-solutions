# Medium/reverse_integer.py

def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    res = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x!=0:
        digit=x%10
        x//=10

        # Check for overflow
        if res > (INT_MAX-digit)//10:
            return 0

        res=res*10+digit

    return sign*res

if __name__=="__main__":
    print(reverse(123))     # 321
    print(reverse(-123))    # -321
    print(reverse(120))     # 21
    print(reverse(0))       # 0
