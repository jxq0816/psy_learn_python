#请输入一个奇数，打印出一个行数为奇数行的菱形
n=int(input("number=?"))
for i in range(1,n+1,2):
    string_1="*"*i
    print(string_1.center(n))
for i in range(n-2,0,-2):
    string_1="*"*i
    print(string_1.center(n))