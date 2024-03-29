a,b=0, 1
for i in range(1,100):
    print(a,end=" ")
    a,b=b,a+b
    if a>100:
        break    