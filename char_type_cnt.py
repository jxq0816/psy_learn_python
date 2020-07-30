#输入任意一个字符串，如何才能得到空格、数字、字符和“其他”的个数？
abc=input("string=")
abc_dict={"space":0,"digit":0,"alpha":0,"others":0}
for i in abc:
    if i.isspace() == True:
        abc_dict["space"] += 1
    elif i.isdigit() == True:
        abc_dict["digit"] += 1
    elif i.isalpha() == True:
        abc_dict["alpha"] += 1
    else:
        abc_dict["others"] += 1
print(abc_dict)