for i in range(1,1001):
    if int(i**0.5)**2==i:
        print(i,end=" ")
# 3c:
a,b=0, 1
for i in range(1,100):
    print(a,end=" ")
    a,b=b,a+b
    if a>100:
        break    