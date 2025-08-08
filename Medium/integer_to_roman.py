# Medium/integer_to_roman.py

def intToRoman(num):
    val_map=[
        (1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
        (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
        (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")
    ]

    roman=""
    for val,symbol in val_map:
        while num>=val:
            roman+=symbol
            num-=val
    return roman

if __name__=="__main__":
    print(intToRoman(3))     # III
    print(intToRoman(58))    # LVIII
    print(intToRoman(1994))  # MCMXCIV
