def divide(dividend:int,divisor:int)->int:
    # Constants for 32-bit signed integer range
    INT_MAX=2**31-1
    INT_MIN=-2**31

    # Handle division by zero
    if divisor==0:
        raise ZeroDivisionError("Division by zero is undefined.")

    # Handle overflow case
    if dividend==INT_MIN and divisor==-1:
        return INT_MAX

    # Determine the sign of the result
    negative=(dividend<0)^(divisor<0)

    # Work with absolute values
    dividend,divisor=abs(dividend),abs(divisor)

    quotient=0
    while dividend>=divisor:
        temp,multiple=divisor,1
        while dividend>=(temp<<1):
            temp<<=1
            multiple<<=1
        dividend-=temp
        quotient+=multiple

    return -quotient if negative else quotient


# Example usage
if __name__=="__main__":
    print(divide(10, 3))   # Output: 3
    print(divide(7, -3))   # Output: -2
