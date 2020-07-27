# 最小公倍数是一个小学算术的概念，两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数。
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
