# cook your dish here
try:
    for T in range(int(input())):
        n,m=map(int, input().split())
        a=list(map(int, input().split()))
        b=list(map(int, input().split()))
        sa=sum(a)
        sb=sum(b)
        i=0
        a=sorted(a)
        b=sorted(b)[::-1]
        flag=0
        while(sb>=sa):
            if i==n:
                flag=1
                break
            if b[i]>a[i]:
                sa+=b[i]-a[i]
                sb-=b[i]-a[i]
            i+=1
        if flag==0:
            print(i)
        else:
            print(-1)
except Exception:
    pass