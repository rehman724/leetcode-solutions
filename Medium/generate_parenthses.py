# generate_parentheses.py

def generate_parenthesis(n: int)->list[str]:

    result=[]

    def backtrack(current,open_count,close_count):
        if len(current)==2*n:
            result.append(current)
            return

        if open_count<n:
            backtrack(current+"(",open_count+1,close_count)
        if close_count<open_count:
            backtrack(current+")",open_count,close_count+1)

    backtrack("", 0, 0)
    return result


if __name__=="__main__":
    # Test cases
    print("Test Case 1: n = 3")
    print(generate_parenthesis(3))
    # Expected: ["((()))","(()())","(())()","()(())","()()()"]

    print("\nTest Case 2: n = 1")
    print(generate_parenthesis(1))
    # Expected: ["()"]

    print("\nTest Case 3: n = 2")
    print(generate_parenthesis(2))
    # Expected: ["(())","()()"]
