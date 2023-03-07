from collections import deque

def findNextMove(cur1, cur2):
    cands=[]
    
    parallel=[[0, -1], [0, 1], [-1, 0], [1, 0]]
    for diff in parallel:
        this1=(cur1[0]+diff[0], cur1[1]+diff[1])
        this2=(cur2[0]+diff[0], cur2[1]+diff[1])
        
        if new_board[this1[0]][this1[1]]==0 and new_board[this2[0]][this2[1]]==0:
            cands.append((this1, this2))
            
    if cur1[0]==cur2[0]:
        diff=[-1, +1]
        for x in diff:
            if new_board[cur1[0]+x][cur1[1]]==0 and new_board[cur2[0]+x][cur2[1]]==0:
                cands.append((cur1, (cur1[0]+x, cur1[1])))
                cands.append((cur2, (cur2[0]+x, cur2[1])))
    else:
        diff=[-1, +1]
        for x in diff:
            if new_board[cur1[0]][cur1[1]+x]==0 and new_board[cur2[0]][cur2[1]+x]==0:
                cands.append((cur1, (cur1[0], cur1[1]+x)))
                cands.append((cur2, (cur2[0], cur2[1]+x)))
                        
    return cands
        
def solution(board):
    answer = 0
    n=len(board)
    global new_board
    new_board=[[1 for _ in range(n+2)]]
    
    for i in range(n):
        this_row=[1]+board[i]+[1]
        new_board.append(this_row)
        
    new_board.append([1 for _ in range(n+2)])
    
    que=deque([((1,1), (1,2), 0)])
    visited=set([((1,1), (1,2))])
    
    while que:
        cur1, cur2, times=que.popleft()
        
        if cur1==(n,n) or cur2==(n,n):
            answer=times
            break
        
        for cand in findNextMove(cur1, cur2):
            if cand not in visited:
                que.append((cand[0], cand[1], times+1))
                visited.add(cand)

    return answer
