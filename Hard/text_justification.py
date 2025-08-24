from typing import List

class Solution:
    def fullJustify(self,words:List[str],maxWidth:int)->List[str]:

        res=[]
        cur_line=[]
        num_of_letters=0

        for word in words:
            # If adding next word exceeds line width -> justify current line
            if num_of_letters+len(word)+len(cur_line)>maxWidth:
                for i in range(maxWidth-num_of_letters):
                    cur_line[i%(len(cur_line)-1 or 1)]+=' '
                res.append(''.join(cur_line))
                cur_line,num_of_letters=[],0

            cur_line.append(word)
            num_of_letters+=len(word)

        # Last line (left-justified, spaces at end)
        res.append(' '.join(cur_line).ljust(maxWidth))
        return res


if __name__=="__main__":
    sol=Solution()

    # Example 1
    words1=["This", "is", "an", "example", "of", "text", "justification."]
    print("Example 1 Output:")
    print(sol.fullJustify(words1, 16))
    # Expected:
    # ["This    is    an",
    #  "example  of text",
    #  "justification.  "]

    # Example 2
    words2=["What", "must", "be", "acknowledgment", "shall", "be"]
    print("\nExample 2 Output:")
    print(sol.fullJustify(words2, 16))
    # Expected:
    # ["What   must   be",
    #  "acknowledgment  ",
    #  "shall be        "]

