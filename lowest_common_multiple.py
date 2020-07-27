# 最小公倍数是一个小学算术的概念
# 如何用程序来求任意两个数的最小公倍数
num_1=int(input("number_1=?"))
num_2=int(input("number_2=?"))
lcm=max(num_1,num_2)
while True:
    if lcm%num_1==0 and lcm%num_2==0:
        break
    else:
        lcm+=1
print("{}和{}的最小公倍数是{}".format(num_1,num_2,lcm))
