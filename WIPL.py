# cook your dish here
try:
    for t in range(int(input())):
        n,k=map(int,input().split())
        h=list(map(int, input().split()))
        h=sorted(h)[::-1]
        res=[2**32-1]
        dp={}
        def sol(a,b,arr):
            if a>=k and b>=k:
                if res[0]>(len(h)-len(arr)):
                    res[0]=len(h)-len(arr)
                return res[0]
            if arr==[]:
                return -1
            if (a,b) in dp:
                return dp[(a,b)]
            dp[(a,b)]=sol(a+arr[0],b,arr[1::])
            dp[(b,a)]=sol(a,b+arr[0],arr[1::])
            return 0
        sol(0,0,h)
        if res[0]==2**32-1:
            print(-1)
        else:
            print(res[0])
except Exception:
    pass