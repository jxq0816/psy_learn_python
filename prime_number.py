number=0
for n in range(2,101):
    for j in range(2,n):
        if n%j==0:
            break
    else:
        number+=1
        print(n,end=' ')
print("1-100之间的素数是%d个" %number)
