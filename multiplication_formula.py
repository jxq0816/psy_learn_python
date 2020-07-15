# https://weibo.com/1182391231/IpRHW2EV9?type=comment#_rnd1593963281720
# 乘法口诀
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%-2d"%(i,j,i*j),end=" ")
    print(" ")