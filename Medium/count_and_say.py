# count_and_say.py

def count_and_say(n:int)->str:
    """Generates the nth term in the count-and-say sequence."""
    if n==1:
        return "1"

    prev=count_and_say(n-1)  # get previous term
    result=""
    count=1

    for i in range(1,len(prev)):
        if prev[i]==prev[i-1]:
            count+=1
        else:
            result+=str(count)+prev[i-1]
            count=1

    result+=str(count)+prev[-1]
    return result


if __name__=="__main__":
    # Test cases
    test_values=[1, 2, 3, 4, 5, 6]
    for n in test_values:
        print(f"n = {n} -> {count_and_say(n)}")
