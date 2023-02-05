from collections import deque

def bfs(pr):
    prev=pr.copy()
    cur=[0,0]
    cost=0
    
    visited=[[0 for _ in range(n)] for _ in range(n)]
    visited[0][0]=1
    q = deque([(prev, cur, cost)])
    
    while q:
        prev, cur, cost = q.popleft()
        
        if cur[0]==n-1 and cur[1]==n-1:
            answer.append(cost)
            
        options=[]
        for option in [[cur[0]-1,cur[1]],[cur[0]+1,cur[1]],[cur[0],cur[1]-1],[cur[0],cur[1]+1]]:
            if option[0]>=0 and option[0]<n and option[1]>=0 and option[1]<n:
                if new_board[option[0]][option[1]]==0:
                    options.append(option)

        for option in options:
            new_prev, new_cur = cur, option
            if abs(prev[0]-option[0])==1 and abs(prev[1]-option[1])==1:
                new_cost=cost+600
            else:
                new_cost=cost+100

            if visited[option[0]][option[1]]==0 or visited[option[0]][option[1]] > new_cost:
                visited[option[0]][option[1]]=new_cost
                q.append((new_prev, new_cur, new_cost))
            

def solution(board):
    global n, answer, new_board
    n=len(board)
    answer=[]
    new_board=board
    
    bfs([0,-1])
    bfs([-1,0])
    
    if len(answer)==0:  return 0
    else:   return min(answer)
