# Medium/zigzag_conversion.py

def convert(s:str,numRows:int)->str:
    if numRows==1 or numRows>=len(s):
        return s

    rows=['']*numRows
    current_row=0
    going_down=False

    for c in s:
        rows[current_row] +=c
        if current_row==0 or current_row==numRows-1:
            going_down=not going_down
        current_row +=1 if going_down else -1

    return ''.join(rows)

if __name__=="__main__":
    print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
    print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
