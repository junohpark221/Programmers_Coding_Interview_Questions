def checkPossible(x, y, n, arch):
    poss=False
    
    if arch==0:
        if y==0 or (y>0 and grid[x][y-1][0]==1) or (grid[x][y][1]==1) or (x>0 and grid[x-1][y][1]==1):
            poss=True
    elif arch==1:
        if (y>0 and grid[x][y-1][0]==1) or (x<n and y>0 and grid[x+1][y-1][0]==1):
            poss=True
        elif (x>0 and grid[x-1][y][1]==1) and (x<n and grid[x+1][y][1]==1):
            poss=True
            
    return poss

def solution(n, build_frame):
    answer = []
    
    global grid
    grid=[[[0,0] for _ in range(n+1)] for _ in range(n+1)]
    
    for build in build_frame:
        x, y, arch, option=build[0], build[1], build[2], build[3]
        
        if option==1:
            if checkPossible(x, y, n, arch):   grid[x][y][arch]=1
        else:
            grid[x][y][arch]=0
            poss=True
            
            if arch==0:
                for cor in [(x, y+1), (x-1, y+1)]:
                    for arch_type in [0, 1]:
                        if grid[cor[0]][cor[1]][arch_type]!=0:
                            if not checkPossible(cor[0], cor[1], n, arch_type):
                                poss=False
                                break
            elif arch==1:
                for cor in [(x, y), (x-1, y), (x+1, y)]:
                    for arch_type in [0, 1]:
                        if grid[cor[0]][cor[1]][arch_type]!=0:
                            if not checkPossible(cor[0], cor[1], n, arch_type):
                                poss=False
                                break
            
            if not poss:   grid[x][y][arch]=1
            
    for i in range(n+1):
        for j in range(n+1):
            if grid[i][j][0]>0:   answer.append([i, j, 0])
            if grid[i][j][1]>0:   answer.append([i, j, 1])

    return answer
