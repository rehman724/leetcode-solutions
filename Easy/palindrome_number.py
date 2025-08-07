# Easy/palindrome_number.py

def isPalindrome(x:int)->bool:
    if x<0 or (x%10==0 and x!=0):
        return False

    reversed_half=0
    while x>reversed_half:
        reversed_half=reversed_half*10+x%10
        x//=10

    # Even digits: x == reversed_half
    # Odd digits: x == reversed_half // 10
    return x==reversed_half or x==reversed_half//10

if __name__=="__main__":
    print(isPalindrome(121))     # True
    print(isPalindrome(-121))    # False
    print(isPalindrome(10))      # False
    print(isPalindrome(1221))    # True
