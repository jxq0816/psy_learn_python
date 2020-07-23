# 今天跟朋友们一起学习“企业根据利润提成发奖金”的问题。
# 当利润(I)低于或等于10万元时，奖金可提10%；
# 当利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 当20万到40万之间时，高于20万元的部分，可提成5%；
# 当40万到60万之间时高于40万元的部分，可提成3%；
# 当60万到100万之间时，高于60万元的部分，可提成1.5%；
# 当高于100万元时，超过100万元的部分按1%提成。
# 问题是求应发放奖金总数是多少？


p_1=int(input("输入利润=（万元)"))
if p_1<10:
    c_1=p_1*0.1
elif p_1>10 and p_1<=20:
    c_1 = 10 * 0.1 + (p_1-10)*0.075
elif p_1>20 and p_1<=40:
    c_1 = 10 * 0.1 + 10 * 0.075 + (p_1-20)*0.05
elif p_1>40 and p_1<=60:
    c_1 = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 +(p_1-20)*0.03
elif p_1>60 and p_1<=100:
    c_1 = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 +(p_1-60)*0.015
elif p_1>100:
    c_1 = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 +(p_1-100)*0.01
print(c_1)