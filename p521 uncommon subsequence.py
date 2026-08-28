def uncommon_subsequenece(a,b):
    if a==b:
        return -1
    else:
        return max(len(a),len(b))		
a = "aaa"
b = "aaa"
print(uncommon_subsequenece(a,b))
