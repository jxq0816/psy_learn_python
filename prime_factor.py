#如何将一个正整数分解质因数？例如输入90，打印出90=2*3*3*5
n=int(input("输入一个正整数=："))
for k in range(2,n+1):
    while n!=k:
        if n%k==0:
            print(k,end="*")
            n=n/k
        else:
            break
print(int(n))