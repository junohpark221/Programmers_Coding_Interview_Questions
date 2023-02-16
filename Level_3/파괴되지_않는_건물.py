def solution(board, skill):
    n=len(board)
    m=len(board[0])
    answer=0
    rangeSum=[[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for this in skill:
        r1, c1, r2, c2 = this[1], this[2], this[3], this[4]
        if this[0]==1:  degree=-this[5]
        else:   degree=this[5]
        
        rangeSum[r1][c1]+=degree
        rangeSum[r1][c2+1]-=degree
        rangeSum[r2+1][c1]-=degree
        rangeSum[r2+1][c2+1]+=degree
    
    prev=0
    for i in range(n+1):
        for j in range(m+1):
            rangeSum[i][j]+=prev
            prev=rangeSum[i][j]
    
    prev=0        
    for j in range(m+1):
        for i in range(n+1):
            rangeSum[i][j]+=prev
            prev=rangeSum[i][j]
    
    for i in range(n):
        for j in range(m):
            if rangeSum[i][j]+board[i][j]>0:    answer+=1
            
    return answer
