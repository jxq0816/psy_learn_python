#今天我们还是学习斐波那契数列。有一个分数序列为 2/1，3/2，5/3，8/5，13/8，21/13……请用Python3编程，求出这个数列的前20项之和。
num=2
den=1
sum=0
for i in range(1,21):
    sum+=num/den
    num,den=num+den,num
print(sum)