#已知数字a, s=a+aa+aaa+aaaa+aaaa，请用Python3进行编程求出s的值。例如：在2+22+222+2222+22222中，共有5个数相加，具体几个数相加由键盘输入。
num=input("number=?")
add=int(input("add=?"))
sum=0
for i in range(1,add+1):
    sum+=int(i*num)
print(sum)