count=0
for i in range(1,5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i!=j and j!=k and k!=i:
                print(i,j,k)
                count+=1
print("共有%d个数字符合条件" %count)