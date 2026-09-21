def valid_pali(s):
    cleaned_text = ''.join([char for char in s if char.isalnum()])
    Str = cleaned_text.lower()
    
    if Str == "":
        return True
    else:
        left = 0
        right = len(Str) - 1

        while left < right :
            if Str[left] != Str[right]:
                return False

            left += 1
            right -= 1
    return True
        
    
s = " "
print(valid_pali(s))
