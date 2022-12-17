n=int(input())
res=1
if n>=100:
    for i in range(1,n+1):
        res=res*i
        x=str(res)
    print(x)