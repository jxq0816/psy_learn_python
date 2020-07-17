fibonacci=[1,1]
for i in range(1,9):
    j=fibonacci[-1]+fibonacci[-2]
    fibonacci.append(j)
print(fibonacci)