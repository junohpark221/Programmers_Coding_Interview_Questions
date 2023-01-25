def solution(n):
    db=[0 for _ in range(n)]
    
    for i in range(n):
        if i==0:
            db[i]=1
        elif i==1:
            db[i]=2
        else:
            db[i]=(db[i-2]+db[i-1])%1000000007
    
    return db[-1]
