def findBusNum(hour, miniute, n, t):
    timeDiff=(hour-9)*60+miniute
    busNum=0
    if timeDiff>0:
        if timeDiff>(n-1)*t:    busNum=n-1
        else:
            busNum=timeDiff//t+1
            if timeDiff%t==0:   busNum-=1
        
    return busNum

def makeAnswer(hour, miniute):
    hourStr=str(hour)
    minStr=str(miniute)
    
    if hour<10: hourStr='0'+hourStr
    if miniute<10: minStr='0'+minStr
    
    return hourStr+':'+minStr

def solution(n, t, m, timetable):
    answer = ''
    timetableList=[]
    busTime=[]
    
    for time in timetable:
        hour=int(time[0:2])
        miniute=int(time[3:5])
        timetableList.append([hour, miniute])
    
    timetableList.sort()
    
    for i in range(n):
        hour=9+(i*t)//60
        miniute=(i*t)%60
        busTime.append([hour, miniute, 0, []])
        
    for time in timetableList:
        busNum=findBusNum(time[0], time[1], n, t)
        busTime[busNum][2]+=1
        busTime[busNum][3].append([time[0], time[1]])
        
    for i in range(len(busTime)):
        if i<n-1:
            if busTime[i][2]>m:
                over=busTime[i][2]-m
                overBus=busTime[i][3][m:].copy()
                nextBus=busTime[i+1][3].copy()
                
                busTime[i][2]=m
                busTime[i][3]=busTime[i][3][:m].copy()
                busTime[i+1][3]=overBus+nextBus
                busTime[i+1][2]+=over
    
    LastBus=busTime[-1]
    if LastBus[2]<m:    answer=makeAnswer(LastBus[0], LastBus[1])
    else:
        if (LastBus[0]*60+LastBus[1])<(LastBus[3][0][0]*60+LastBus[3][0][1]):
            answer=makeAnswer(LastBus[0], LastBus[1])
        elif (LastBus[0]*60+LastBus[1])==(LastBus[3][0][0]*60+LastBus[3][0][1]):
            new_time=LastBus[0]*60+LastBus[1]-1
            new_hour=new_time//60
            new_min=new_time%60
            answer=makeAnswer(new_hour, new_min)
        else:
            bus=LastBus[0]*60+LastBus[1]
            new_time=LastBus[3][m-1][0]*60+LastBus[3][m-1][1]-1
            if new_time<=bus:
                new_hour=new_time//60
                new_min=new_time%60
                answer=makeAnswer(new_hour, new_min)
            else:
                answer=makeAnswer(LastBus[0], LastBus[1])
                
    return answer
