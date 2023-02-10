def rotateKey(key):
    new_key=[[0 for _ in range(m)] for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[i][j]=key[m-1-j][i]
            
    return new_key

def compare(key, lock, i ,j):
    new_key=[[0 for _ in range(n)] for _ in range(n)]
    for a in range(m):
        for b in range(m):
            if -m+1+j+a>=0 and -m+1+j+a<n:
                if -m+1+i+b>=0 and -m+1+i+b<n:
                    new_key[-m+1+j+a][-m+1+i+b]=key[a][b]
                    
    answer=True
    for a in range(n):
        for b in range(n):
            if lock[a][b]+new_key[a][b]!=1:
                answer=False
                break
                
    return answer

def unlock(key, lock):
    answer=False
    
    for i in range(n+m-1):
        for j in range(n+m-1):
            answer=compare(key, lock, i, j)
            if answer==True:    break
        if answer==True:    break
    
    return answer

def solution(key, lock):
    answer = False
    global n,m
    n=len(lock)
    m=len(key)
    
    answer=unlock(key, lock)
    
    if answer!=True:
        prev_key=key
        for _ in range(3):
            this_key=rotateKey(prev_key)
            answer=unlock(this_key, lock)
            prev_key=this_key
            
            if answer==True:
                break
    
    return answer
