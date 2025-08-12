def longest_valid_parentheses(s:str)->int:
    stack=[-1]  # Base index for valid substring calculations
    max_len=0

    for i, char in enumerate(s):
        if char=='(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # New base for next valid sequence
            else:
                max_len=max(max_len,i-stack[-1])

    return max_len

if __name__=="__main__":
    test_cases=[
        ("(()",2),
        (")()())",4),
        ("",0),
        ("()(()",2),
        ("()(())",6)
    ]

    for s,expected in test_cases:
        result=longest_valid_parentheses(s)
        print(f"Input: '{s}' | Expected: {expected} | Got: {result}")