for i in range(100,1001):
    if i>1:
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag:
            print(i,end=" ")
    else:
        break