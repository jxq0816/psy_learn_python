# 最大公约数是一个小学算术的概念，还常常被用在社会学中，用来形容人们之间形成的最大共识，如“共通的意义空间”等说法。
# 如何用程序来求任意两个数的最大公约数？我会在下一条公布答案。
num_1=int(input("number_1=?"))
num_2=int(input("number_2=?"))
gcd=1
a=min(num_1,num_2)
for i in range(1,a+1):
    if num_1%i==0 and num_2%i==0:
        gcd=i;
print("{}和{}的最大公约数是{}".format(num_1,num_2,gcd))
