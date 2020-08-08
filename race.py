a={"x","y","z"}
b={"x","y","z"}
c={"x","y","z"}
c=c-{"x","z"}
a=a-{"x"}
for i in a:
    for j in b:
        for k in c:
            if len(set([i,j,k]))==3:
                print('a:%s,b:%s,c:%s' %(i,j,k))