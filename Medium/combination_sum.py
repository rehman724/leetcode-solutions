
def combination_sum(candidates,target):
    """
    Returns all unique combinations of candidates where the chosen numbers sum to target.
    Each number in candidates may be chosen unlimited times.
    """
    result=[]

    def backtrack(remaining,start,path):
        if remaining==0:
            result.append(path[:])
            return
        elif remaining<0:
            return

        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtrack(remaining-candidates[i],i,path)  # allow same element again
            path.pop()

    backtrack(target, 0, [])
    return result


if __name__=="__main__":
    # Test cases
    candidates_list=[
        ([2,3,6,7],7),
        ([2,3,5],8),
        ([2],1),
        ([1],1),
        ([1],2)
    ]

    for candidates, target in candidates_list:
        print(f"Candidates: {candidates}, Target: {target}")
        print("Combinations:", combination_sum(candidates,target))
        print("-" * 40)
